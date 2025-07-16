from ..app_iface import Operator, StringProperty, PropertyGroup
from ..utils import construct_from_class_path, type_from_class_path, get_class_path
from ..operator import OpConfirmationMsgMixin


class UVPM3_IdCollectionAccessDescriptor(PropertyGroup):

    active_item_uuid : StringProperty(default='')


import uuid

class IdCollectionItemMixin:

    @staticmethod
    def uuid_is_valid(uuid_to_test):
        try:
            uuid_obj = uuid.UUID(uuid_to_test, version=4)
        except ValueError:
            return False
        return uuid_obj.hex == uuid_to_test

    @staticmethod
    def uuid_generate():
        return uuid.uuid4().hex

    def init_defaults(self):
        if self.name == '':
            self.name = self.DEFAULT_ITEM_NAME

        if self.uuid == '':
            self.uuid = self.uuid_generate()



class IdCollectionAccess:

    def __init__(self, context, init_collection=False, desc=None, ui_drawing=False):
        self.context = context
        self.ui_drawing = ui_drawing
        self.coll = self._get_collection()

        access_class_path = get_class_path(self)

        if init_collection:
            self.coll.access_class_path = access_class_path
        
        else:
            assert self.coll.access_class_path == access_class_path

        if desc:
            self.desc = desc

        else:
            self.desc = self._get_access_desc()

        self.init_active_members()

    def init_active_members(self):
        self.active_item = self.init_active_item()

        if not self.ui_drawing and self.active_item is not None:
            self.active_item.init_defaults()

    def get_collection(self):
        return self.coll

    def get_coll_enum_items(self):
        items = []
        enumerated_items = list(enumerate(self.get_items()))
        enumerated_items.sort(key=lambda i: i[1].name)

        for idx, item in enumerated_items:
            items.append((str(item.uuid), item.name, "", idx))
        return items

    # @staticmethod
    # def get_coll_enum_items_callback(property_self, context):
    #     item_access = GroupingSchemeAccess()
    #     item_access.init_access(context, ui_drawing=True, desc_id='default')
    #     return item_access.get_items_enum_items()

    def create_item(self, set_active=True):
        new_item = self.get_items().add()
        new_item.init_defaults()

        if set_active:
            self.set_active_item_uuid(new_item.uuid)

        return new_item
    
    def _pre_remove_item(self, idx):
        pass
    
    def remove_item(self, idx):
        if idx < 0:
            return
        
        self._pre_remove_item(idx)
        self.get_items().remove(idx)

    def remove_active_item(self):
        active_idx = self.get_active_item_idx()
        self.remove_item(active_idx)

        new_idx = min(active_idx, len(self.get_items())-1)
        self.set_active_item_uuid(self.get_items()[new_idx].uuid if new_idx >=0 else '')


    def get_active_item_uuid(self):
        return  self.desc.active_item_uuid

    def get_active_item_idx(self):
        active_item_uuid = self.get_active_item_uuid()

        for idx, item in enumerate(self.get_items()):
            if active_item_uuid == item.uuid:
                return idx

        return -1

    def init_active_item(self):
        active_item_idx = self.get_active_item_idx()
        active_item = None

        if active_item_idx >= 0:
            active_item = self.get_items()[active_item_idx]

        return active_item
    
    def get_items(self):
        return self.coll.items
    
    def get_active_item_safe(self):
        if self.active_item is None:
            raise RuntimeError('No active item found')
        
        return self.active_item

    def set_active_item_uuid(self, uuid):
        self.desc.active_item_uuid = uuid
        self.init_active_members()



class IdCollectionOperatorAttrMixin:

    access_class_path : StringProperty(default='')


class UVPM3_OT_IdCollectionOperatorGeneric(Operator):

    bl_options = {'INTERNAL', 'UNDO'}

    def execute(self, context):
        try:
            self.access = construct_from_class_path(self.access_class_path, *[context])
            return self.execute_impl(context)

        except Exception as ex:
            self.report({'ERROR'}, str(ex))

        return {'CANCELLED'}


class UVPM3_OT_IdCollectionNewItem(UVPM3_OT_IdCollectionOperatorGeneric, IdCollectionOperatorAttrMixin):

    bl_idname = "uvpackmaster3.id_collection_new_item"
    bl_label = "Add New"
    bl_description = "Add a new item"

    @classmethod
    def description(cls, context, properties):
        return 'Add a new {}'.format(type_from_class_path(properties.access_class_path).ITEM_NAME.lower())

    def execute_impl(self, context):
        self.access.create_item()
        return {'FINISHED'}


class UVPM3_OT_IdCollectionRemoveItem(OpConfirmationMsgMixin, UVPM3_OT_IdCollectionOperatorGeneric, IdCollectionOperatorAttrMixin):

    bl_idname = "uvpackmaster3.id_collection_remove_item"
    bl_label = "Remove Active"
    bl_description = "Remove the active item"

    @classmethod
    def description(cls, context, properties):
        return 'Remove the active {}'.format(type_from_class_path(properties.access_class_path).ITEM_NAME.lower())
    
    def confirmation_msg(self):
        return 'Are you sure you want to remove the {}?'.format(type_from_class_path(self.access_class_path).ITEM_NAME.lower())
    
    def execute_impl(self, context):
        self.access.remove_active_item()
        return {'FINISHED'}
    