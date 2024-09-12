import bpy
from bpy.props import StringProperty, EnumProperty, IntProperty

bl_info = {
    "name": "Tag selected assets",
    "author": "Thorben Baerentson",
    "description": "Adds a tag to each selected item",
    "blender": (4, 00, 0),
    "category": "Object",
}

class TagSelectedAssets(bpy.types.Operator):
    """Adds a tag to each selected item"""
    bl_idname = "object.tag_selected_assets"
    bl_label = "Tag selected assets"

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
            
            o.asset_data.tags.new(self.tag_name, skip_if_exists = True)
            
        return { "FINISHED" }
        
    tag_name : StringProperty(default = "Road", name = "Tag Name")

def menu_func(self, context):
    self.layout.operator(
        TagSelectedAssets.bl_idname, 
        text = TagSelectedAssets.bl_label)

# Register and add to the "object" menu.
def register():
    bpy.utils.register_class(TagSelectedAssets)

def unregister():
    bpy.utils.unregister_class(TagSelectedAssets)