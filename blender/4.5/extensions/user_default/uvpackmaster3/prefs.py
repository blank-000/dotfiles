# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import os
import multiprocessing
from pathlib import Path
from collections import namedtuple

from .utils import get_active_image_size, PanelUtilsMixin
from .prefs_scripted_utils import scripted_pipeline_property_group
from .labels import Labels 
from .grouping_scheme import UVPM3_GroupingScheme
from .box_utils import disable_box_rendering
from .register_utils import UVPM3_OT_SetEnginePath
from .multi_panel import UVPM3_SavedMultiPanelSettings
from .multi_panel_manager import UVPM3_SavedPanelSettings
from . import module_loader
from .app_iface import *
from .pgroup import standalone_property_group
from .panel import PanelUtilsMixin

from .scripted_pipeline import properties
scripted_properties_modules = module_loader.import_submodules(properties)
scripted_properties_classes = module_loader.get_registrable_classes(scripted_properties_modules,
                                                                    sub_class=PropertyGroup,
                                                                    required_vars=("SCRIPTED_PROP_GROUP_ID",))

@standalone_property_group
class UVPM3_DeviceSettings:

    enabled : BoolProperty(name='enabled', default=True)


DeviceMetadata = namedtuple('DeviceMetadata', ('enabled_default', 'help_url_suffix'), defaults=(None, None))


@standalone_property_group
class UVPM3_SavedDeviceSettings:

    DEVICE_METADATA = [
        ('vulkan_', DeviceMetadata(
                        enabled_default=False,
                        help_url_suffix='48-other-topics/20-vulkan-gpu-acceleration')
        )
    ]

    dev_id : StringProperty(name="", default="")
    settings : PointerProperty(type=UVPM3_DeviceSettings)
    
    def get_metadata(self):
        for id_prefix, metadata in self.DEVICE_METADATA:
            if self.dev_id.startswith(id_prefix):
                return metadata
            
        return DeviceMetadata()

    def init(self, dev_id):
        self.dev_id = dev_id
        metadata = self.get_metadata()

        if metadata.enabled_default is not None:
            self.settings.enabled = metadata.enabled_default


from .id_collection.main_props import UVPM3_MainPropIdCollection, UVPM3_MainProps
from .id_collection import UVPM3_IdCollectionAccessDescriptor

def _update_main_prop_sets_enable(self, context):
    if self.main_prop_sets_enable:
        from .id_collection.main_props import MainPropSetAccess
        main_prop_access = MainPropSetAccess(bpy.context, init_collection=True)

        if len(main_prop_access.get_items()) == 0:
            main_prop_access.create_item(set_active=True)

from .enums import GroupingMethod

class UVPM3_SceneProps(PropertyGroup):

    main_prop_access_desc : PointerProperty(type=UVPM3_IdCollectionAccessDescriptor)
    main_prop_sets : PointerProperty(type=UVPM3_MainPropIdCollection)

    main_prop_sets_enable : BoolProperty(
        name=Labels.MAIN_PROP_SETS_ENABLE_NAME,
        description=Labels.MAIN_PROP_SETS_ENABLE_DESC,
        default=False,
        update=_update_main_prop_sets_enable)
    default_main_props : PointerProperty(type=UVPM3_MainProps)

    saved_m_panel_settings : CollectionProperty(type=UVPM3_SavedMultiPanelSettings)
    saved_panel_settings : CollectionProperty(type=UVPM3_SavedPanelSettings)
    grouping_schemes : CollectionProperty(name="Grouping Schemes", type=UVPM3_GroupingScheme)

    editor_group_method : EnumProperty(
        items=GroupingMethod.to_blend_items(),
        name="{} (Editor)".format(Labels.GROUP_METHOD_NAME),
        description=Labels.GROUP_METHOD_DESC,
        default=GroupingMethod.MANUAL.code,
        update=disable_box_rendering)
    

@addon_preferences
class UVPM3_Preferences(PanelUtilsMixin):
    bl_idname = __package__

    MAX_TILES_IN_ROW = 1000
    INCONSISTENT_ISLANDS_HELP_URL_SUFFIX = '/48-other-topics/5-inconsistent-islands-error-handling/'

    modes_dict = None

    def pixel_margin_enabled(self, main_props):
        return main_props.pixel_margin_enable

    def extra_pixel_margin_to_others_enabled(self, main_props):
        return main_props.extra_pixel_margin_to_others > 0

    def pixel_border_margin_enabled(self, main_props):
        return main_props.pixel_border_margin > 0

    def heuristic_enabled(self, main_props):
        return main_props.heuristic_enable

    def heuristic_timeout_enabled(self, main_props):
        return self.heuristic_enabled(main_props) and main_props.heuristic_search_time > 0

    def advanced_heuristic_available(self, main_props):
        return self.FEATURE_advanced_heuristic and self.heuristic_enabled(main_props)

    def pack_ratio_supported(self):
        return self.FEATURE_pack_ratio and self.FEATURE_target_box

    def pack_ratio_enabled(self, main_props):
        return self.pack_ratio_supported() and main_props.tex_ratio

    def pixel_margin_tex_size(self, main_props, context):
        if self.pack_ratio_enabled(main_props):
            img_size = get_active_image_size(context)
            tex_size = img_size[1]
        else:
            tex_size = main_props.pixel_margin_tex_size

        return tex_size

    def fixed_scale_enabled(self, main_props):
        from .enums import UvpmScaleMode
        return UvpmScaleMode.fixed_scale_enabled(main_props.scale_mode)

    def normalize_scale_not_supported_msg(self, main_props):
        return None
    
    def texel_density_not_supported_msg(self, main_props):
        if not self.pixel_margin_enabled(main_props):
            return "Supported only with Pixel Margin enabled"
        
        return None
    
    def heuristic_allow_mixed_scales_not_supported_msg(self, main_props):
        return None
    
    def tile_filling_method_not_supported_msg(self, main_props):      
        return None

    def reset_box_params(self):
        self.box_rendering = False
        self.group_scheme_boxes_editing = False
        self.custom_target_box_editing = False
        self.boxes_dirty = False

    def reset_feature_codes(self):
        self.FEATURE_demo = False
        self.FEATURE_island_rotation = True
        self.FEATURE_overlap_check = True
        self.FEATURE_packing_depth = True
        self.FEATURE_heuristic_search = True
        self.FEATURE_pack_ratio = True
        self.FEATURE_pack_to_others = True
        self.FEATURE_grouping = True
        self.FEATURE_lock_overlapping = True
        self.FEATURE_advanced_heuristic = True
        self.FEATURE_self_intersect_processing = True
        self.FEATURE_validation = True
        self.FEATURE_multi_device_pack = True
        self.FEATURE_target_box = True
        self.FEATURE_island_rotation_step = True
        self.FEATURE_pack_to_tiles = True

    def reset_stats(self):

        for dev in self.device_array():
            dev.reset()

    def reset(self):
        self.engine_path = ''
        self.enabled = True
        self.engine_initialized = False
        self.engine_status_msg = ''
        self.thread_count = multiprocessing.cpu_count()
        self.operation_counter = -1
        self.write_to_file = False
        self.seed = 0

        self.enable_vulkan_saved = self.enable_vulkan

        self.reset_stats()
        self.reset_device_array()
        self.reset_box_params()
        self.reset_feature_codes()

    def draw_engine_status(self, layout):
        row = layout.row(align=True)
        self.draw_engine_status_message(row, icon_only=False)
        self.draw_engine_status_help_button(row)

    def draw_engine_status_message(self, layout, icon_only):
        icon = 'ERROR' if not self.engine_initialized else 'NONE'
        layout.label(text="" if icon_only else self.engine_status_msg, icon=icon)

    def draw_engine_status_help_button(self, layout):
        if not self.engine_initialized:
            from .help import UVPM3_OT_SetupHelp
            layout.operator(UVPM3_OT_SetupHelp.bl_idname, icon='QUESTION', text='')

    def draw_addon_preferences(self, layout):
        col = layout.column(align=True)
        col.label(text='General options:')

        row = col.row(align=True)
        row.prop(self, "thread_count")

        box = col.box()
        row = box.row(align=True)
        row.prop(self, 'orient_aware_uv_islands')

        from .panel import UVPM3_PT_Generic
        box = col.box()
        UVPM3_PT_Generic.prop_with_help(self, 'allow_inconsistent_islands', box, help_url_suffix=self.INCONSISTENT_ISLANDS_HELP_URL_SUFFIX)

        box = col.box()
        row = box.row(align=True)
        row.prop(self, 'dont_transform_pinned_uvs')

        if self.dont_transform_pinned_uvs:
            box = col.box()
            row = box.row(align=True)
            row.prop(self, 'pinned_uvs_as_others')
        
        col.separator()
        col.label(text='UI options:')

        box = col.box()
        row = box.row(align=True)
        row.prop(self, 'hori_multi_panel_toggles')

        box = col.box()
        row = box.row(align=True)
        row.prop(self, 'append_mode_name_to_op_label')

        box = col.box()
        row = box.row(align=True)
        row.prop(self, "disable_tips")

        row = col.row(align=True)
        row.prop(self, "font_size_text_output")

        row = col.row(align=True)
        row.prop(self, "font_size_uv_overlay")

        row = col.row(align=True)
        row.prop(self, "box_render_line_width")
        
        box = col.box()
        row = box.row(align=True)
        row.prop(self, "short_island_operator_names")

        self.draw_prop_saved_state(self, 'enable_vulkan', col.box())

        # adv_op_box = col.box()
        adv_op_layout = col # adv_op_box.column(align=True)
        adv_op_layout.separator()
        adv_op_layout.label(text='Expert options:')

        UVPM3_OT_ShowHideAdvancedOptions.draw_operator(adv_op_layout)
        if self.show_expert_options:
            box = adv_op_layout.box()
            box.label(text='Change expert options only if you really know what you are doing.', icon='ERROR')

            box = adv_op_layout.box()
            row = box.row(align=True)
            row.prop(self, 'disable_immediate_uv_update')

        col.separator()
        col.separator()

        col.label(text='Packing devices:')
        dev_main = col.column(align=True)

        dev_factors = (0.8,)
        dev_cols = self.create_split_columns(dev_main.box(), factors=dev_factors)

        dev_cols[0].label(text='Name')
        dev_cols[1].label(text='Enabled')

        dev_cols = self.create_split_columns(dev_main.box(), factors=dev_factors)

        for dev in self.device_array():
            settings = dev.settings
            row = dev_cols[0].row()
            row.label(text=dev.name)

            row = dev_cols[1].row()
            row.prop(settings, 'enabled', text='')

            help_url_suffix = dev.help_url_suffix()

            if help_url_suffix is not None:
                self._draw_help_operator(row, help_url_suffix)

        save_operator = AppInterface.save_preferences_operator()
        if save_operator:
            col.separator()
            col.operator(save_operator.bl_idname)

    def draw(self, context):
        layout = self.layout

        # main_box = layout.box()
        main_col = layout.column(align=True)
        main_col.label(text='Engine status:')
        box = main_col.box()
        self.draw_engine_status(box)

        col = box.column(align=True)
        row = col.row(align=True)
        row.label(text="Path to the UVPM engine:")
        row = col.row(align=True)
        row.enabled = False
        row.prop(self, 'engine_path')

        row = col.row(align=True)
        row.operator(UVPM3_OT_SetEnginePath.bl_idname)

        main_col.separator()
        main_col.separator()

        self.draw_addon_preferences(main_col)

    def get_engine_args(self):
        args = []

        if self.enable_vulkan:
            args.append('-v')

        return args

    def get_mode(self, mode_id, context):
        if self.modes_dict is None:
            raise RuntimeError("Mods are not initialized.")
        try:
            return next(m(context) for m_list in self.modes_dict.values() for (m_id, m) in m_list if m_id == mode_id)
        except StopIteration:
            raise KeyError("The '{}' mode not found".format(mode_id))

    def get_modes(self, mode_type):
        return self.modes_dict[mode_type]

    def get_active_main_mode(self, context):
        try:
            return self.get_mode(get_main_props(context).active_main_mode_id, context)
        except KeyError:
            pass

        from .scripted_pipeline.modes.pack_modes import UVPM3_Mode_SingleTile
        return self.get_mode(UVPM3_Mode_SingleTile.MODE_ID, context)

    def set_active_main_mode(self, context, mode_id):
        get_main_props(context).active_main_mode_id = mode_id

    # Supporeted features
    FEATURE_demo : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_island_rotation : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_overlap_check : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_packing_depth : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_heuristic_search : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_advanced_heuristic : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_pack_ratio : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_pack_to_others : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_grouping : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_lock_overlapping : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_self_intersect_processing : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_validation : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_multi_device_pack : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_target_box : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_island_rotation_step : BoolProperty(
        name='',
        description='',
        default=False)

    FEATURE_pack_to_tiles : BoolProperty(
        name='',
        description='',
        default=False)

    operation_counter : IntProperty(
        name='',
        description='',
        default=-1)

    box_rendering : BoolProperty(
        name='',
        description='',
        default=False)

    boxes_dirty : BoolProperty(
        name='',
        description='',
        default=False)

    group_scheme_boxes_editing : BoolProperty(
        name='',
        description='',
        default=False)

    custom_target_box_editing : BoolProperty(
        name='',
        description='',
        default=False)

    engine_retcode : IntProperty(
        name='',
        description='',
        default=0)

    engine_path : StringProperty(
        name='',
        description='',
        default='')

    engine_initialized : BoolProperty(
        name='',
        description='',
        default=False)

    engine_status_msg : StringProperty(
        name='',
        description='',
        default='')
        # update=_update_engine_status_msg)

    thread_count : IntProperty(
        name=Labels.THREAD_COUNT_NAME,
        description=Labels.THREAD_COUNT_DESC,
        default=multiprocessing.cpu_count(),
        min=1,
        max=multiprocessing.cpu_count())

    seed : IntProperty(
        name=Labels.SEED_NAME,
        description='',
        default=0,
        min=0,
        max=10000)

    test_param : IntProperty(
        name=Labels.TEST_PARAM_NAME,
        description='',
        default=0,
        min=0,
        max=10000)

    write_to_file : BoolProperty(
        name=Labels.WRITE_TO_FILE_NAME,
        description='',
        default=False)

    wait_for_debugger : BoolProperty(
        name=Labels.WAIT_FOR_DEBUGGER_NAME,
        description='',
        default=False)
    
    hori_multi_panel_toggles : BoolProperty(
        name=Labels.HORI_MULTI_PANEL_TOGGLES_NAME,
        description=Labels.HORI_MULTI_PANEL_TOGGLES_DESC,
        default=False)

    append_mode_name_to_op_label : BoolProperty(
        name=Labels.APPEND_MODE_NAME_TO_OP_LABEL_NAME,
        description=Labels.APPEND_MODE_NAME_TO_OP_LABEL_DESC,
        default=False)

    orient_aware_uv_islands : BoolProperty(
        name=Labels.ORIENT_AWARE_UV_ISLANDS_NAME,
        description=Labels.ORIENT_AWARE_UV_ISLANDS_DESC,
        default=False)

    allow_inconsistent_islands : BoolProperty(
        name=Labels.ALLOW_INCONSISTENT_ISLANDS_NAME,
        description=Labels.ALLOW_INCONSISTENT_ISLANDS_DESC,
        default=False)
    
    dont_transform_pinned_uvs : BoolProperty(
        name=Labels.DONT_TRANSFORM_PINNED_UVS_NAME,
        description=Labels.DONT_TRANSFORM_PINNED_UVS_DESC,
        default=True)
    
    pinned_uvs_as_others : BoolProperty(
        name=Labels.PINNED_UVS_AS_OTHERS_NAME,
        description=Labels.PINNED_UVS_AS_OTHERS_DESC,
        default=True)
    
    enable_vulkan : BoolProperty(
        name='Enable Vulkan',
        description='Enable Vulkan devices for packing (if available in the system)',
        default=True
    )

    enable_vulkan_saved : BoolProperty(
        name='',
        default=True
    )

    # UI options
    disable_tips : BoolProperty(
        name=Labels.DISABLE_TIPS_NAME,
        description=Labels.DISABLE_TIPS_DESC,
        default=False)

    font_size_text_output : IntProperty(
        name=Labels.FONT_SIZE_TEXT_OUTPUT_NAME,
        description=Labels.FONT_SIZE_TEXT_OUTPUT_DESC,
        default=15,
        min=5,
        max=100)

    font_size_uv_overlay : IntProperty(
        name=Labels.FONT_SIZE_UV_OVERLAY_NAME,
        description=Labels.FONT_SIZE_UV_OVERLAY_DESC,
        default=20,
        min=5,
        max=100)

    box_render_line_width : FloatProperty(
        name=Labels.BOX_RENDER_LINE_WIDTH_NAME,
        description=Labels.BOX_RENDER_LINE_WIDTH_DESC,
        default=4.0,
        min=1.0,
        max=10.0,
        step=5.0)
    
    short_island_operator_names : BoolProperty(
        name=Labels.SHORT_ISLAND_OPERATOR_NAMES_NAME,
        description=Labels.SHORT_ISLAND_OPERATOR_NAMES_DESC,
        default=False)

    # Expert options
    show_expert_options : BoolProperty(
        name=Labels.SHOW_EXPERT_OPTIONS_NAME,
        description=Labels.SHOW_EXPERT_OPTIONS_DESC,
        default=False
    )

    disable_immediate_uv_update : BoolProperty(
        name=Labels.DISABLE_IMMEDIATE_UV_UPDATE_NAME,
        description=Labels.DISABLE_IMMEDIATE_UV_UPDATE_DESC,
        default=False
    )

    # Dismissed warnings options

    pixel_margin_warn_dismissed : BoolProperty(
        name='Pixel Margin Warning Dismissed',
        default=False
    )

    multi_panel_manager = None

    script_allow_execution : BoolProperty(name='Allow Script Execution', default=False)

    def get_multi_panel_manager(self, context):
        if type(self).multi_panel_manager is None:
            from .multi_panel_manager import MultiPanelManager
            type(self).multi_panel_manager = MultiPanelManager()

        mp_manager = type(self).multi_panel_manager
        mp_manager.update_settings(get_scene_props(context))
        return mp_manager

    dev_array = []
    saved_dev_settings : CollectionProperty(type=UVPM3_SavedDeviceSettings)

    def device_array(self):
        return type(self).dev_array

    def reset_device_array(self):
        type(self).dev_array = []

    @classmethod
    def get_userdata_path(cls):
        from .os_iface import os_get_userdata_path
        os_userdata_path = os_get_userdata_path()
        path = os.path.join(os_userdata_path, AppInterface.APP_ID, 'engine3')
        Path(path).mkdir(parents=True, exist_ok=True)
        return path

    @classmethod
    def get_main_preset_path(cls):
        preset_path = os.path.join(cls.get_userdata_path(), 'presets')
        Path(preset_path).mkdir(parents=True, exist_ok=True)
        return preset_path

    @classmethod
    def get_g_schemes_preset_path(cls):
        preset_path = os.path.join(cls.get_userdata_path(), 'grouping_schemes')
        Path(preset_path).mkdir(parents=True, exist_ok=True)
        return preset_path

    @classmethod
    def get_preferences_filepath(cls):
        return os.path.join(cls.get_userdata_path(), 'prefs.json')
    

@scripted_pipeline_property_group("scripted_props",
                                  UVPM3_SceneProps, scripted_properties_classes,
                                  (UVPM3_SceneProps, UVPM3_Preferences))
class UVPM3_ScriptedPipelineProperties(PropertyGroup):
    pass


class UVPM3_OT_ShowHideAdvancedOptions(Operator):

    bl_label = 'Show Expert Options'
    bl_idname = 'uvpackmaster3.show_hide_expert_options'

    @staticmethod
    def get_label():
        prefs = get_prefs()
        return 'Hide Expert Options' if prefs.show_expert_options else 'Show Expert Options'

    @classmethod
    def draw_operator(cls, layout):
        layout.operator(cls.bl_idname, text=cls.get_label())

    def draw(self, context):
        layout = self.layout
        col = layout.column()

        for label in self.confirmation_labels:
            col.label(text=label)

    def execute(self, context):
        prefs = get_prefs()
        prefs.show_expert_options = not prefs.show_expert_options

        from .utils import redraw_ui
        redraw_ui(context)

        return {'FINISHED'}

    def invoke(self, context, event):
        prefs = get_prefs()

        if not prefs.show_expert_options:
            self.confirmation_labels =\
                [ 'WARNING: expert options should NEVER be changed under the standard packer usage.',
                  'You should only change them if you really know what you are doing.',
                  'Are you sure you want to show the expert options?' ]

            wm = context.window_manager
            return wm.invoke_props_dialog(self, width=700)

        return self.execute(context)
