import bpy
from bpy.props import StringProperty, EnumProperty, IntProperty

import sys
import importlib

bl_info = {
    "name": "Blender Asset Tools",
    "author": "Thorben Baerentson",
    "description": "A collection of tools that makes managing assets in blender easier and more productive.",
    "blender": (4, 00, 0),
    "category": "Object",
}

modulesNames = [
    'tag_assets_based_on_parent_names',
    'object_mt_blender_asset_tools',
    'set_asset_value',
    'tag_selected_assets',
    'untag_selected_assets',
]

modulesFullNames = {}
for currentModuleName in modulesNames:
    modulesFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))
 
# ... tben import or reload these modules.
for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)

def register():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()

def unregister():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()