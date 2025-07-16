
from ..app_iface import *
from . import UVPM3_OT_IdCollectionNewItem, UVPM3_OT_IdCollectionRemoveItem, IdCollectionOperatorAttrMixin

from ..utils import get_class_path, construct_from_class_path


class UVPM3_OT_IdCollectionBrowseItems(Operator, IdCollectionOperatorAttrMixin):

    bl_options = {'INTERNAL'}
    bl_idname = 'uvpackmaster3.id_collection_browse_items'
    bl_label = 'Browse Items'
    bl_description = "Browse Items"

    active_item_uuid : StringProperty(name='', description='', default='')

    def execute(self, context):
        access = construct_from_class_path(self.access_class_path, *[context])
        access.set_active_item_uuid(self.active_item_uuid)
        return {'FINISHED'}


class UVPM3_MT_IdCollectionBrowseItems(Menu):

    bl_label = "Items"
    bl_idname = "UVPM3_MT_IdCollectionBrowseItems"

    def draw(self, context):
        access_class_path = context.uvpm3_id_collection.access_class_path
        access = construct_from_class_path(access_class_path, *[context])
        items = access.get_items()

        layout = self.layout
        layout.context_pointer_set('uvpm3_id_item_access_desc', context.uvpm3_id_item_access_desc)

        for item in items:
            operator = layout.operator(UVPM3_OT_IdCollectionBrowseItems.bl_idname, text=item.name)
            operator.access_class_path = access_class_path
            operator.active_item_uuid = item.uuid


class IdCollectionDrawer:

    def __init__(self,
                 access,
                 preset_panel_t=None):
        
        self.access = access
        self.preset_panel_t = preset_panel_t

    def draw_items_presets(self, layout):
        layout.emboss = 'NONE'
        layout.popover(panel=self.preset_panel_t.__name__, icon='PRESET', text="")

    def op_init(self, op, layout):
        layout.context_pointer_set('uvpm3_id_item_access_desc', self.access.desc)
        op.access_class_path = get_class_path(self.access)

    def draw(self, layout):
        main_col = layout.column(align=True)

        if self.access.DRAW_LABEL:
            main_col.label(text=self.access.ITEM_NAME + ':')

        row = main_col.row(align=True)

        row.context_pointer_set('uvpm3_id_collection', self.access.get_collection())
        row.context_pointer_set('uvpm3_id_item_access_desc', self.access.desc)
        row.menu(UVPM3_MT_IdCollectionBrowseItems.bl_idname, text="", icon=self.access.ICON)

        item_available = len(self.access.get_items()) > 0

        if self.access.active_item is not None:
            row.prop(self.access.active_item, "name", text="")
        elif item_available:
            box = row.box()
            box.scale_y = 0.5
            box.enabled = False
            box.label(text='← Select {}'.format(self.access.ITEM_NAME.lower()))

        op = row.operator(UVPM3_OT_IdCollectionNewItem.bl_idname, icon='ADD', text='' if item_available else UVPM3_OT_IdCollectionNewItem.bl_label)
        self.op_init(op, row)

        if self.access.active_item is not None:
            op = row.operator(UVPM3_OT_IdCollectionRemoveItem.bl_idname, icon='REMOVE', text='')
            self.op_init(op, row)

        if self.preset_panel_t is not None:
            box = row.box()
            box.scale_y = 0.5
            self.draw_items_presets(box)
