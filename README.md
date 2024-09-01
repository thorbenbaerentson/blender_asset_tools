# Table of Contents
- [Blender Asset Tools](#blender-asset-tools)
- [Operators](#operators)
    - [Add property to selected](#add-property-to-selected)
    - [Tag assets based on parent names](#tag-assets-based-on-parent-names)
    - [Set asset value](#set-asset-value)

# Blender Asset Tools
This is a collection of operators that make managing assets in blender more convenient. 

# Operators
All operators a put under Object :arror-right: Asset :arror-right: Asset Tools under the 'Layout' tab. Keep in mind, that each operator requires at least one object to be selected.

## Add property to selected
Takes a property name and value and adds this property value on all selected objects. Properties can be added to the object or the data tab. Property values will be exported alongside the object if blender exports .glft or .glb files. Game engines like [Bevy](https://bevyengine.org/) import these property values when loading .gltfs (see [Load gltf extras](https://bevyengine.org/examples/3d-rendering/load-gltf-extras)). This enables us to pump data from Blender to a game engine. 
Think of adding a property called 'Collider' to all objects and setting it to true for all objects, that should serve as a collider. When loading a .gltf you could replace all of objects with a physics object, if the 'Collider' value is true and use a regular mesh renderer if not. 
This opens up almost infinite possibilities to interact with a game engine from Blender. Actually this should enable us to turn Blender into a Level Editor for engines like [Bevy](https://bevyengine.org/).

## Tag assets based on parent names
Goes through all selected objects and adds tags to it, if the object has been marked as an asset. The tag names are derived from its parents object. If a parent object is an empty its name is used to create a new tag. A tag is added for each empty this script finds above the selected object. Tags can be used in the asset browser to search for assets.
With this operator a user can organize the asset inside a scene and generate tags based on the scene structure.

## Set asset value
Allows bulk editing of values like 'Author' and 'License' for assets.