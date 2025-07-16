
from . import IdCollectionAccess, IdCollectionItemMixin
from ..utils import unique_name
from ..app_iface import PropertyGroup, StringProperty, PointerProperty, IntProperty, FloatProperty, BoolProperty
from ..labels import *
from ..props import *
from ..contansts import *

from ..grouping_scheme import UVPM3_GroupingSchemeAccessDescriptorContainer
from ..island_params import AlignPriorityIParamInfo, NormalizeMultiplierIParamInfo
from ..grouping import UVPM3_AutoGroupingOptions
from ..scripting import UVPM3_Scripting
from ..box import UVPM3_Box
from ..operator_islands import NumberedGroupIParamInfo
from ..box_utils import disable_box_rendering
from ..mode import ModeType



class MainPropSetAccess(IdCollectionAccess):

    ITEM_NAME = 'Option Set'
    ICON = 'OPTIONS'
    DRAW_LABEL = False
    HELP_URL_SUFFIX = '/20-packing-functionalities/15-basic-packing-and-options/#option-sets'

    def _get_collection(self):
        return get_scene_props(self.context).main_prop_sets
    
    def _get_access_desc(self):
        return get_scene_props(self.context).main_prop_access_desc
    
    def _pre_remove_item(self, idx):
        if len(self.get_items()) == 1:
            raise RuntimeError("Cannot remove the last set. Disable option sets globally in the Packing panel, if you don't want to use them")
    
    
def _update_main_props_name(self, context):
    access = MainPropSetAccess(context)
    items = access.get_items()

    if self.name.strip() == '':
        name = UVPM3_MainProps.DEFAULT_ITEM_NAME
    else:
        name = self.name

    self['name'] = unique_name(name, items, self)


def _update_active_main_mode_id(self, context):
    disable_box_rendering(None, context)


def _update_orient_3d_axes(self, context):
    if self.orient_prim_3d_axis == self.orient_sec_3d_axis:
        enum_values = AppInterface.object_property_data(self)["orient_sec_3d_axis"].enum_items_static.keys()
        value_index = enum_values.index(self.orient_sec_3d_axis)
        self.orient_sec_3d_axis = enum_values[(value_index+1) % len(enum_values)]


class UVPM3_NumberedGroupsDescriptor(PropertyGroup):

    enable : BoolProperty(
        name=Labels.GROUPS_ENABLE_NAME,
        description=Labels.GROUPS_ENABLE_DESC,
        default=False)

    group_num : IntProperty(
        name=Labels.GROUP_NUM_NAME,
        description=Labels.GROUP_NUM_DESC,
        default=NumberedGroupIParamInfo.MIN_VALUE+1,
        min=NumberedGroupIParamInfo.MIN_VALUE+1,
        max=NumberedGroupIParamInfo.MAX_VALUE)

    use_g_scheme : BoolProperty(
        name='Use Grouping Scheme',
        description='Use a grouping scheme to define groups',
        default=False
    )


class UVPM3_SplitOverlapProps(PropertyGroup):

    detection_mode : EnumProperty(
        items=UvpmOverlapDetectionMode.to_blend_items(),
        name=Labels.SPLIT_OVERLAP_DETECTION_MODE_NAME,
        description=Labels.SPLIT_OVERLAP_DETECTION_MODE_DESC)
    
    max_tile_x : IntProperty(
        name=Labels.SPLIT_OVERLAP_MAX_TILE_X_NAME,
        description=Labels.SPLIT_OVERLAP_MAX_TILE_X_DESC,
        default = 0,
        min = 0)
    
    dont_split_priorities : BoolProperty(
        name=Labels.SPLIT_OVERLAP_DONT_SPLIT_PRIORITIES_NAME,
        description=Labels.SPLIT_OVERLAP_DONT_SPLIT_PRIORITIES_DESC,
        default=False
    )

    def to_script_param(self):
        return {
            'detection_mode': int(self.detection_mode),
            'max_tile_x': int(self.max_tile_x),
            'dont_split_priorities': bool(self.dont_split_priorities)
        }


class UVPM3_NumberedGroupsDescriptorContainer(PropertyGroup):

    lock_group : PointerProperty(type=UVPM3_NumberedGroupsDescriptor)
    stack_group : PointerProperty(type=UVPM3_NumberedGroupsDescriptor)
    track_group : PointerProperty(type=UVPM3_NumberedGroupsDescriptor)


class UVPM3_MainProps(PropertyGroup, IdCollectionItemMixin):

    DEFAULT_ITEM_NAME = 'OptionSet'

    name : StringProperty(name="name", default="", update=_update_main_props_name)
    uuid : StringProperty(name="uuid", default="")


    grouping_scheme_access_descriptors : PointerProperty(type=UVPM3_GroupingSchemeAccessDescriptorContainer)

    numbered_groups_descriptors : PointerProperty(type=UVPM3_NumberedGroupsDescriptorContainer)

    track_groups_props : PointerProperty(type=UVPM3_TrackGroupsProps)
    scripting : PointerProperty(type=UVPM3_Scripting)

    pack_strategy_props : PointerProperty(type=UVPM3_PackStrategyProps)

    precision : IntProperty(
        name=Labels.PRECISION_NAME,
        description=Labels.PRECISION_DESC,
        default=500,
        min=10,
        max=10000)

    margin : FloatProperty(
        name=Labels.MARGIN_NAME,
        description=Labels.MARGIN_DESC,
        min=0.0,
        max=0.2,
        default=0.003,
        precision=3,
        step=0.1)

    pixel_margin_enable : BoolProperty(
        name=Labels.PIXEL_MARGIN_ENABLE_NAME,
        description=Labels.PIXEL_MARGIN_ENABLE_DESC,
        default=False)

    pixel_margin : def_prop__pixel_margin()
    pixel_border_margin : def_prop__pixel_border_margin()
    extra_pixel_margin_to_others : def_prop__extra_pixel_margin_to_others()
    pixel_margin_tex_size : def_prop__pixel_margin_tex_size()
    pixel_perfect_align : def_prop__pixel_perfect_align()
    pixel_perfect_vert_align_mode : EnumProperty(
        items=UvpmPixelPerfectVertAlignMode.to_blend_items(),
        name=Labels.PIXEL_PERFECT_VERT_ALIGN_MODE_NAME,
        description=Labels.PIXEL_PERFECT_VERT_ALIGN_MODE_DESC)

    rotation_enable : BoolProperty(
        name=Labels.ROTATION_ENABLE_NAME,
        description=Labels.ROTATION_ENABLE_DESC,
        default=PropConstants.ROTATION_ENABLE_DEFAULT)

    pre_rotation_disable : BoolProperty(
        name=Labels.PRE_ROTATION_DISABLE_NAME,
        description=Labels.PRE_ROTATION_DISABLE_DESC,
        default=PropConstants.PRE_ROTATION_DISABLE_DEFAULT)

    flipping_enable : BoolProperty(
        name=Labels.FLIPPING_ENABLE_NAME,
        description=Labels.FLIPPING_ENABLE_DESC,
        default=PropConstants.FLIPPING_ENABLE_DEFAULT)

    normalize_scale : BoolProperty(
        name=Labels.NORMALIZE_SCALE_NAME,
        description=Labels.NORMALIZE_SCALE_DESC,
        default=False)
    
    normalize_space : EnumProperty(
        items=UvpmCoordSpace.to_blend_items(),
        name=Labels.NORMALIZE_SPACE_NAME,
        description=Labels.NORMALIZE_SPACE_DESC)
    
    tdensity_enable : BoolProperty(
        name=Labels.TEXEL_DENSITY_ENABLE_NAME,
        description=Labels.TEXEL_DENSITY_ENABLE_DESC,
        default=False)
    
    tdensity_value : def_prop_tdensity_value()
    
    island_normalize_multiplier_enable : BoolProperty(
        name=Labels.ISLAND_NORMALIZE_MULTIPLIER_ENABLE_NAME,
        description=Labels.ISLAND_NORMALIZE_MULTIPLIER_ENABLE_DESC,
        default=False)
    
    island_normalize_multiplier : IntProperty(
        name=Labels.ISLAND_NORMALIZE_MULTIPLIER_NAME,
        description=Labels.ISLAND_NORMALIZE_MULTIPLIER_DESC,
        default=NormalizeMultiplierIParamInfo.DEFAULT_VALUE,
        min=NormalizeMultiplierIParamInfo.MIN_VALUE,
        max=NormalizeMultiplierIParamInfo.MAX_VALUE)

    scale_mode : def_prop__scale_mode()

    arrange_non_packed : BoolProperty(
        name=Labels.ARRANGE_NON_PACKED_NAME,
        description=Labels.ARRANGE_NON_PACKED_DESC,
        default=False
    )

    rotation_step : IntProperty(
        name=Labels.ROTATION_STEP_NAME,
        description=Labels.ROTATION_STEP_DESC,
        default=PropConstants.ROTATION_STEP_DEFAULT,
        min=PropConstants.ROTATION_STEP_MIN,
        max=PropConstants.ROTATION_STEP_MAX)

    island_rot_step_enable : BoolProperty(
        name=Labels.ISLAND_ROT_STEP_ENABLE_NAME,
        description=Labels.ISLAND_ROT_STEP_ENABLE_DESC,
        default=False)

    island_rot_step : IntProperty(
        name=Labels.ISLAND_ROT_STEP_NAME,
        description=Labels.ISLAND_ROT_STEP_DESC,
        default=90,
        min=0,
        max=180)

    tex_ratio : BoolProperty(
        name=Labels.TEX_RATIO_NAME,
        description=Labels.TEX_RATIO_DESC,
        default=False)
    
    def get_main_mode_blend_enums(scene, context):
        prefs = get_prefs()
        modes_info = prefs.get_modes(ModeType.MAIN)

        return [(mode_id, mode_cls.enum_name(), "") for mode_id, mode_cls in modes_info]
    
    active_main_mode_id : EnumProperty(
        items=get_main_mode_blend_enums,
        update=_update_active_main_mode_id,
        name=Labels.PACK_MODE_NAME,
        description=Labels.PACK_MODE_DESC)

    group_method : EnumProperty(
        items=GroupingMethod.to_blend_items(),
        name=Labels.GROUP_METHOD_NAME,
        description=Labels.GROUP_METHOD_DESC,
        update=disable_box_rendering)

    auto_group_options : PointerProperty(type=UVPM3_AutoGroupingOptions)

    use_blender_tile_grid : BoolProperty(
        name=Labels.USE_BLENDER_TILE_GRID_NAME,
        description=Labels.USE_BLENDER_TILE_GRID_DESC,
        default=False)

    lock_overlapping_enable : BoolProperty(
        name=Labels.LOCK_OVERLAPPING_ENABLE_NAME,
        description=Labels.LOCK_OVERLAPPING_ENABLE_DESC,
        default=False)

    lock_overlapping_mode : EnumProperty(
        items=UvpmOverlapDetectionMode.to_blend_items(),
        name=Labels.LOCK_OVERLAPPING_MODE_NAME,
        description=Labels.LOCK_OVERLAPPING_MODE_DESC)

    heuristic_enable : BoolProperty(
        name=Labels.HEURISTIC_ENABLE_NAME,
        description=Labels.HEURISTIC_ENABLE_DESC,
        default=False)

    heuristic_search_time : IntProperty(
        name=Labels.HEURISTIC_SEARCH_TIME_NAME,
        description=Labels.HEURISTIC_SEARCH_TIME_DESC,
        default=0,
        min=0,
        max=3600)

    heuristic_max_wait_time : IntProperty(
        name=Labels.HEURISTIC_MAX_WAIT_TIME_NAME,
        description=Labels.HEURISTIC_MAX_WAIT_TIME_DESC,
        default=0,
        min=0,
        max=300)
        
    heuristic_allow_mixed_scales : BoolProperty(
        name=Labels.HEURISTIC_ALLOW_MIXED_SCALES_NAME,
        description=Labels.HEURISTIC_ALLOW_MIXED_SCALES_DESC,
        default=False)
    
    advanced_heuristic : BoolProperty(
        name=Labels.ADVANCED_HEURISTIC_NAME,
        description=Labels.ADVANCED_HEURISTIC_DESC,
        default=False)

    fully_inside : BoolProperty(
        name=Labels.FULLY_INSIDE_NAME,
        description=Labels.FULLY_INSIDE_DESC,
        default=True)

    custom_target_box_enable : BoolProperty(
        name=Labels.CUSTOM_TARGET_BOX_ENABLE_NAME,
        description=Labels.CUSTOM_TARGET_BOX_ENABLE_DESC,
        default=False,
        update=disable_box_rendering)

    custom_target_box : PointerProperty(type=UVPM3_Box)

    tile_count_x : IntProperty(
        name=Labels.TILE_COUNT_X_NAME,
        description=Labels.TILE_COUNT_X_DESC,
        default=PropConstants.TILE_COUNT_XY_DEFAULT,
        min=PropConstants.TILE_COUNT_XY_MIN,
        max=PropConstants.TILE_COUNT_XY_MAX)

    tile_count_y : IntProperty(
        name=Labels.TILE_COUNT_Y_NAME,
        description=Labels.TILE_COUNT_Y_DESC,
        default=PropConstants.TILE_COUNT_XY_DEFAULT,
        min=PropConstants.TILE_COUNT_XY_MIN,
        max=PropConstants.TILE_COUNT_XY_MAX)
    
    tile_filling_method : EnumProperty(
        items=UvpmTileFillingMethod.to_blend_items(),
        name=Labels.TILE_FILLING_METHOD_NAME,
        description=Labels.TILE_FILLING_METHOD_DESC)


    split_props : PointerProperty(type=UVPM3_SplitOverlapProps)

    # ------ Aligning properties ------ #

    simi_mode : EnumProperty(
        items=UvpmSimilarityMode.to_blend_items(),
        name=Labels.SIMI_MODE_NAME,
        description=Labels.SIMI_MODE_DESC)

    simi_threshold : FloatProperty(
        name=Labels.SIMI_THRESHOLD_NAME,
        description=Labels.SIMI_THRESHOLD_DESC,
        default=0.1,
        min=0.0,
        precision=2,
        step=5.0)
    
    simi_check_holes : BoolProperty(
        name=Labels.SIMI_CHECK_HOLES_NAME,
        description=Labels.SIMI_CHECK_HOLES_DESC,
        default=False)

    simi_adjust_scale : BoolProperty(
        name=Labels.SIMI_ADJUST_SCALE_NAME,
        description=Labels.SIMI_ADJUST_SCALE_DESC,
        default=False)
    
    simi_non_uniform_scaling_tolerance : FloatProperty(
        name=Labels.SIMI_NON_UNIFORM_SCALING_TOLERANCE_NAME,
        description=Labels.SIMI_NON_UNIFORM_SCALING_TOLERANCE_DESC,
        default=0.0,
        min=0.0,
        max=1.0,
        precision=2,
        step=2.0)

    simi_match_3d_axis : EnumProperty(
        items=UvpmAxis.to_blend_items(include_none=True, only_positive=True),
        name=Labels.SIMI_MATCH_3D_AXIS_NAME,
        description=Labels.SIMI_MATCH_3D_AXIS_DESC)

    simi_match_3d_axis_space : EnumProperty(
        items=UvpmCoordSpace.to_blend_items(),
        name=Labels.SIMI_MATCH_3D_AXIS_SPACE_NAME,
        description=Labels.SIMI_MATCH_3D_AXIS_SPACE_DESC)

    simi_correct_vertices : BoolProperty(
        name=Labels.SIMI_CORRECT_VERTICES_NAME,
        description=Labels.SIMI_CORRECT_VERTICES_DESC,
        default=False)

    simi_vertex_threshold : FloatProperty(
        name=Labels.SIMI_VERTEX_THRESHOLD_NAME,
        description=Labels.SIMI_VERTEX_THRESHOLD_DESC,
        default=0.01,
        min=0.0,
        max=0.05,
        precision=4,
        step=1.0e-1)

    align_priority_enable : BoolProperty(
        name=Labels.ALIGN_PRIORITY_ENABLE_NAME,
        description=Labels.ALIGN_PRIORITY_ENABLE_DESC,
        default=False)

    align_priority : IntProperty(
        name=Labels.ALIGN_PRIORITY_NAME,
        description=Labels.ALIGN_PRIORITY_DESC,
        default=int(AlignPriorityIParamInfo.DEFAULT_VALUE),
        min=int(AlignPriorityIParamInfo.MIN_VALUE),
        max=int(AlignPriorityIParamInfo.MAX_VALUE))



    orient_prim_3d_axis : EnumProperty(
        items=UvpmAxis.to_blend_items(include_none=False, only_positive=True),
        default=PropConstants.ORIENT_PRIM_3D_AXIS_DEFAULT,
        update=_update_orient_3d_axes,
        name=Labels.ORIENT_PRIM_3D_AXIS_NAME,
        description=Labels.ORIENT_PRIM_3D_AXIS_DESC)

    orient_prim_uv_axis : EnumProperty(
        items=UvpmAxis.to_blend_items(include_none=False, only_2d=True),
        default=PropConstants.ORIENT_PRIM_UV_AXIS_DEFAULT,
        name=Labels.ORIENT_PRIM_UV_AXIS_NAME,
        description=Labels.ORIENT_PRIM_UV_AXIS_DESC)

    orient_sec_3d_axis : EnumProperty(
        items=UvpmAxis.to_blend_items(include_none=False, only_positive=True),
        default=PropConstants.ORIENT_SEC_3D_AXIS_DEFAULT,
        update=_update_orient_3d_axes,
        name=Labels.ORIENT_SEC_3D_AXIS_NAME,
        description=Labels.ORIENT_SEC_3D_AXIS_DESC)

    orient_sec_uv_axis : EnumProperty(
        items=UvpmAxis.to_blend_items(include_none=False, only_2d=True),
        default=PropConstants.ORIENT_SEC_UV_AXIS_DEFAULT,
        name=Labels.ORIENT_SEC_UV_AXIS_NAME,
        description=Labels.ORIENT_SEC_UV_AXIS_DESC)

    orient_to_3d_axes_space : EnumProperty(
        items=UvpmCoordSpace.to_blend_items(),
        name=Labels.ORIENT_TO_3D_AXES_SPACE_NAME,
        description=Labels.ORIENT_TO_3D_AXES_SPACE_DESC)

    orient_prim_sec_bias : IntProperty(
        name=Labels.ORIENT_PRIM_SEC_BIAS_NAME,
        description=Labels.ORIENT_PRIM_SEC_BIAS_DESC,
        default=PropConstants.ORIENT_PRIM_SEC_BIAS_DEFAULT,
        min=0,
        max=90)
    

class UVPM3_MainPropIdCollection(PropertyGroup):

    items : CollectionProperty(type=UVPM3_MainProps)
    access_class_path : StringProperty(default='')
