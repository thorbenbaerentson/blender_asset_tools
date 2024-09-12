import bpy
from bpy.props import StringProperty, EnumProperty, IntProperty

bl_info = {
    "name": "Untag selected assets",
    "author": "Thorben Baerentson",
    "description": "Removes a tag from all selected item",
    "blender": (4, 00, 0),
    "category": "Object",
}

class UntagSelectedAssets(bpy.types.Operator):
    """Removes a tag from all selected item"""
    bl_idname = "object.untag_selected_assets"
    bl_label = "Untag selected assets"

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
            
            if o.asset_data.tags[self.tag_name] is None:
                print(o.name + " has not been tagged with " + self.tag_name)
                continue
            
            o.asset_data.tags.remove(o.asset_data.tags[self.tag_name])
            
        return { "FINISHED" }
        
    tag_name : StringProperty(default = "Road", name = "Tag Name")

def menu_func(self, context):
    self.layout.operator(
        UntagSelectedAssets.bl_idname, 
        text = UntagSelectedAssets.bl_label)

# Register and add to the "object" menu.
def register():
    bpy.utils.register_class(UntagSelectedAssets)

def unregister():
    bpy.utils.unregister_class(UntagSelectedAssets)