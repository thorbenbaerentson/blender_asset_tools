# Table of Contents
- [Blender Asset Tools](#blender-asset-tools)
- [Operators](#operators)
    - [Tag assets based on parent names](#tag-assets-based-on-parent-names)
    - [Set asset value](#set-asset-value)
- [Known Issues](#known-issues)

# Blender Asset Tools
This is a collection of operators that make managing assets in blender more convenient. 

# Operators
All operators a put under 'Object :arrow_right: Asset :arrow_right: Asset Tools' under the 'Layout' tab. Keep in mind, that each operator requires at least one object to be selected.

## Tag assets based on parent names
Goes through all selected objects and adds tags to it, if the object has been marked as an asset. The tag names are derived from its parents object. If a parent object is an empty its name is used to create a new tag. A tag is added for each empty this script finds above the selected object. Tags can be used in the asset browser to search for assets.
With this operator a user can organize the asset inside a scene and generate tags based on the scene structure.

## Set asset value
Allows bulk editing of values like 'Author' and 'License' for assets. This might be helpful if you intend to share your work with others.

# Known Issues
- The menu item 'Asset Tools' should be grayed out when no object is selected. However, implementing 'poll' for a menu object does not seam to suffice in order to achive it.  
