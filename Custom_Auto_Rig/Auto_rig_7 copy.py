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

bone_drivers = {"Arms_up": "humerus",
"Arms_down": "humerus",
"Arms_forward": "humerus",
"Arms_back": "humerus",
"Knees_up": "alt",
"Knees_up_butt": "femur",
"knees_up_spine": "femur",
"Knees_up_pelvis": "femur",
"T-pose": "femur",
"Leg_spread": "femur",
"Leg_spread_front": "kneeBendDeform",
"Leg_back": "femur",
"Head_up": "alt",
"Head_down": "alt",
"Head_tilt": "alt",
"Head_turn": "alt",
"bend_back": "alt",
"bend_forward": "alt",
"bend_right": "alt",
"bend_left": "alt",
"turn_left": "alt",
"turn_right": "alt",
"fist": "alt",
"fingers_bent_up": None,
"fingers_spread": None,
"Elbow": "alt",
"tiptoes": "alt",
"foot_bend_in": "alt",
"foot_bend_out": "alt",
"toes_bend": None,
"toes_together": None,
"toes_spread": None,
"toes_curl": "alt"}


### Creating Drivers for shapekeys ###

### Get shapekey list ###

obj = r.object_selection(rig)

if obj.data.shape_keys:
    shape_keys = obj.data.shape_keys.key_blocks
    shape_key_names = [key.name for key in shape_keys]

obj = bpy.data.objects[rig]

pose_bone = obj.pose.bones.get("humerus_L")
bone_rotation = pose_bone.rotation_quaternion
bone_rotation_xyz = pose_bone.rotation_euler
rotation_mode = pose_bone.rotation_mode


driving_bones = {}
for item in shape_key_names:
    if "!!" in item:
        pass
    for key in bone_drivers.keys():
        name_of_driving_bone = ''
    
        if key.lower() in item.lower():

            if bone_drivers[key] == None:
                pass
            elif "!!" in item:
                pass
            elif 'head' in item:
                name_of_driving_bone = 'head'
                driving_bones[item] = name_of_driving_bone
            elif bone_drivers[key] != "alt":
                name_of_driving_bone = bone_drivers[key]

                if item[-1] == 'L':
                    name_of_driving_bone = name_of_driving_bone + '_L'
                    driving_bones[item] = name_of_driving_bone

                elif item[-1] == 'R':
                    name_of_driving_bone = name_of_driving_bone + '_R'
                    driving_bones[item] = name_of_driving_bone

                else:
                    pass

            elif bone_drivers[key] == "alt":

                if 'fist' in item.lower():
                    num = item[-1]
                    name_of_driving_bone = item.split('_')[-2]
                    name_of_driving_bone = name_of_driving_bone + "_" + num
                    if '_L_' in item:
                        name_of_driving_bone = name_of_driving_bone + '_L'
                        driving_bones[item] = name_of_driving_bone
                    else:
                        name_of_driving_bone = name_of_driving_bone + '_R'
                        driving_bones[item] = name_of_driving_bone

                
                elif 'toe_' in item.lower():
                    num = item[-1]
                    name_of_driving_bone = item.split('_')[-2]
                    name_of_driving_bone = name_of_driving_bone + "_" + num
                    if '_L_' in item:
                        name_of_driving_bone = name_of_driving_bone + '_L'
                        driving_bones[item] = name_of_driving_bone
                    else:
                        name_of_driving_bone = name_of_driving_bone + '_R'
                        driving_bones[item] = name_of_driving_bone
                    

                elif item[-1] is 1 or 2 or 3:
                    new = item[:-2]
                    cleaned = new.split('_')[-1]
                    name_of_driving_bone = cleaned + '_' + item[-1]
                    driving_bones[item] = name_of_driving_bone

                elif '_L' in item:
                    new = item[:-2]
                    cleaned = new.split('_')[-1]
                    name_of_driving_bone = cleaned + '_L'
                    driving_bones[item] = name_of_driving_bone
                elif '_R' in item:
                    new = item[:-2]
                    cleaned = new.split('_')[-1]
                    name_of_driving_bone = cleaned + '_R'
                    driving_bones[item] = name_of_driving_bone
                else:
                    pass

print(driving_bones)

