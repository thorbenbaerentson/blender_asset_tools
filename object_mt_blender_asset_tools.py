import bpy

class OBJECT_MT_BlenderAssetTools(bpy.types.Menu):
    bl_label = "Blender Asset Tools"
    bl_idname = "OBJECT_MT_AssetTools"

    @classmethod
    def poll(cls, context):
        return context.selected_objects is not None

    def draw(self, context):
        layout = self.layout

        if context.selected_objects is None:
            print("No objects selected. Noting to do.")
            return
       
        layout.operator(
            "object.tag_assets_based_on_parent_names", 
            text = "Tag assets based on parent names")
        
        layout.operator(
            "object.set_asset_value", 
            text = "Set asset value")
            
        layout.operator(
            "object.tag_selected_assets", 
            text = "Tag selected assets")
        
        layout.operator(
            "object.untag_selected_assets", 
            text = "Untag selected assets")

def draw_menu(self, context):
    self.layout.menu(OBJECT_MT_BlenderAssetTools.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_MT_BlenderAssetTools)
    bpy.types.VIEW3D_MT_object_asset.append(draw_menu)

def unregister():
    bpy.types.VIEW3D_MT_object_asset.remove(draw_menu)
    bpy.utils.unregister_class(OBJECT_MT_BlenderAssetTools)