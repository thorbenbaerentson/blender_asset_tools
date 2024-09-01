import bpy
from bpy.props import StringProperty, EnumProperty, IntProperty

bl_info = {
    "name": "Tag assets based on parent names",
    "author": "Thorben Baerentson",
    "description": "Adds tags to selected items based on all parent objects, using empties only.",
    "blender": (4, 00, 0),
    "category": "Object",
}

class TagAssetsBasedOnParentNames(bpy.types.Operator):
    """Adds tags to selected items based on all parent objects, using empties only."""
    bl_idname = "object.tag_assets_based_on_parent_names"
    bl_label = "Tag assets based on parent names"

    @classmethod
    def poll(cls, context):
        return context.selected_objects is not None
    
    def handle_parent(self, o, p):
        if p is None:
            return
        
        # Consider all items in the hierarchy but ignore objects that are not empty.
        if p.type != "EMPTY":
            self.handle_parent(o, p.parent)
            return
        
        # Tag object and move on.
        o.asset_data.tags.new(p.name, skip_if_exists = True)        
        self.handle_parent(o, p.parent)
    
    def execute(self, context):
        for o in context.selected_objects:
            if o.parent is None:
                continue
            
            if o.asset_data is None:
                print("Ignoring '" + o.name + "' since it is not marked as an asset.")
                continue
            
            self.handle_parent(o, o.parent)
            
        return { "FINISHED" }


def menu_func(self, context):
    self.layout.operator(
        TagAssetsBasedOnParentNames.bl_idname, 
        text = TagAssetsBasedOnParentNames.bl_label)

# Register and add to the "object" menu.
def register():
    bpy.utils.register_class(TagAssetsBasedOnParentNames)

def unregister():
    bpy.utils.unregister_class(TagAssetsBasedOnParentNames)