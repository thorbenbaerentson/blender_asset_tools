import bpy
from bpy.props import StringProperty, EnumProperty, IntProperty

bl_info = {
    "name": "Set asset value",
    "author": "Thorben Baerentson",
    "description": "Sets a meta data field in the asset browser for all selected objects (e.g. Description, License, Author etc)",
    "blender": (4, 00, 0),
    "category": "Object",
}

class SetAssetValue(bpy.types.Operator):
    """Sets a meta data field in the asset browser for all selected objects (e.g. Description, License, Author etc)"""
    bl_idname = "object.set_asset_value"
    bl_label = "Set asset value"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects is not None
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        for o in context.selected_objects:
            if o.asset_data is None:
                print("Ignoring '" + o.name + "' since it is not marked as an asset.")
                continue

            if self.property_name == "description":
                o.asset_data.description = self.property_value
                continue

            if self.property_name == "license":
                o.asset_data.license = self.property_value
                continue  

            if self.property_name == "copyright":
                o.asset_data.copyright = self.property_value
                continue

            if self.property_name == "author":
                o.asset_data.author = self.property_value
                continue       
            
        return { "FINISHED" }
    
    def get_items(self, context):
        return (
            ("description",     "Description",  "Set a description"),
            ("license",         "License",      "Set a license"),
            ("copyright",       "Copyright",    "Set a copyright notice"),
            ("author",          "Author",       "Set author name"),
        )
    
    property_name : EnumProperty(items = get_items, name = "Name")
    property_value : StringProperty(default = "Test", name = "Value")


def menu_func(self, context):
    self.layout.operator(SetAssetValue.bl_idname, text = SetAssetValue.bl_label)


# Register and add to the "object" menu.
def register():
    bpy.utils.register_class(SetAssetValue)


def unregister():
    bpy.utils.unregister_class(SetAssetValue)