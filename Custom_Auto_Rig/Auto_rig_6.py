import bpy
from mathutils import Vector
import math
import os
import sys

# Add the directory containing your module to the Python path (before importing it)
module_dir = os.path.abspath('O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig')
sys.path.insert(0, module_dir)

# Now you can import your module as usual
from rig_func import Rigging_Functions

# initialize the class
r = Rigging_Functions()

###### Cleaning ######

rig = 'Female Transfer Rig'

r.set_mode('OBJECT')
r.remove_object_selection()
r.remove_edit_and_arm_selection(rig)

### Creating custom properties ###

def custom_bone_prop(rig_name, bone_name, prop_name, prop_value):
    obj = bpy.data.objects[rig]
    bone = obj.pose.bones[bone_name]
    bone[prop_name] = prop_value
    prop = bone.id_properties_ui(prop_name)
    prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)


sys.path.remove(module_dir)
