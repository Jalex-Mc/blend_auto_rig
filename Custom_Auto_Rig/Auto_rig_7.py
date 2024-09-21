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
r.set_mode('OBJECT')



# ## hiding non-CTRL bones/Controls ##
# # arm = bpy.data.armatures[rig]
# # arm.collections.get("Deform").is_visible = False
# # arm.collections.get("ACCESSORY").is_visible = False
# # arm.collections.get("FK").is_visible = False
# # arm.collections.get("IK").is_visible = False
# # arm.collections.get("RBF").is_visible = False




############# Driver set up for shapes ##############

# bone_drivers = {"Arms_up": ["humerus", 4],
# "Arms_down": ["humerus", 2],
# "Arms_forward": ["humerus", 3],
# "Arms_back": ["humerus", 1],
# "Knees_up": ["alt", 24],
# "Knees_up_butt": ["femur", 24],
# "knees_up_spine_1": ["femur", 24],
# "Knees_up_pelvis": ["femur", 24],
# "T-pose": ["femur", 28],
# "Leg_spread": ["femur", 25],
# "Leg_spread_front": ["tibia", 27],
# "Leg_back": ["femur", 26],
# "Head_up": ["alt", 23],
# "Head_down": ["alt",18],
# "Head_tilt": ["alt", {'left':19}, {'right':20}],
# "Head_turn": ["alt", 21, 22],
# "bend_back": ["alt", 6],
# "bend_forward": ["alt", 7],
# "bend_right": ["alt", 9],
# "bend_left": ["alt", 8],
# "turn_left": ["alt", 33],
# "turn_right": ["alt", 34],
# "fist": ["alt",{'left':12}, {'right':13}],
# "fingers_bent_up": None,
# "fingers_spread": None,
# "Elbow": ["alt",{'left':10},{'right':11}],
# "tiptoes": ["alt",{'left':29},{'right':30}],
# "foot_bend_in": ["alt", {'left':14}, {'right':15}],
# "foot_bend_out": ["alt", {'left':16}, {'right':17}],
# "toes_bend": None,
# "toes_together": None,
# "toes_spread": None,
# "toes_curl": ["alt", {'left':31}, {'right':32}]}

# action_numbers = {
# 1:"Arms back",
# 2:"Arms Down",
# 3:"Arms forward",
# 4:"Arms up",
# 5:"Base",
# 6:"Bend back",
# 7:"Bend forward",
# 8:"Bend left",
# 9:"Bend right",
# 10:"Elbow left",
# 11:"Elbow right",
# 12:"Fist Left",
# 13:"Fist right",
# 14:"Foot bend in left",
# 15:"Foot bend in right",
# 16:"Foot bend out left",
# 17:"Foot bend out right",
# 18:"Head down",
# 19:"Head tilt left",
# 20:"Head tilt right",
# 21:"Head turned left",
# 22:"Head turned right",
# 23:"Head up",
# 24:"Knees up",
# 25:"Leg spread",
# 26:"Legs back",
# 27:"Legs Spread FWD",
# 28:"T-Pose",
# 29:"Tiptoes Left",
# 30:"Tiptoes right",
# 31:"Toes curl left",
# 32:"Toes curl right",
# 33:"turn Left",
# 34:"turn right"}

# action_assignments = {}

# ### Creating Drivers for shapekeys ###

# ### Get shapekey list ###

# # obj = r.object_selection(rig)
# mesh = 'Universal Female without mouth'
# obj = bpy.data.objects[mesh]
# obj.select_set(True)
# bpy.context.view_layer.objects.active = obj

# # doesn't work within a fucking class, stupid piece of shit.
# shape_keys = obj.data.shape_keys.key_blocks
# shape_key_names = [key.name for key in shape_keys]

# driving_bones = r.shapes_target_bones(shape_key_names)


# driving_bones["Head_tilt_L_head"] = ['head', 19]
# driving_bones["Head_tilt_L_neck_2"] = ['neck_2', 19]
# driving_bones["Head_tilt_L_neck_1"] = ['neck_1', 19]
# driving_bones["Head_tilt_R_head"] = ['head', 20]
# driving_bones["Head_tilt_R_neck_2"] = ['neck_2', 20]
# driving_bones["Head_tilt_R_neck_1"] = ['neck_1', 20]
# driving_bones["Head_turn_R_head"] = ['head', 21]
# driving_bones["Head_turn_R_neck_2"] = ['neck_2', 21]
# driving_bones["Head_turn_R_neck_1"] = ['neck_1', 21]
# driving_bones["Head_turn_L_head"] = ['head', 22]
# driving_bones["Head_turn_L_neck_2"] = ['neck_2', 22]
# driving_bones["Head_turn_L_neck_1"] = ['neck_1', 22]

# print(driving_bones)

# count = 1

# r.change_frame(10)

# actions = r.action_list()
# actions_without_ex = [x for x in actions if "Armature" not in x]

# # for action in actions_without_ex:
# # print(action)

# # for key, value in action_assignments:
# #     pass

# # for key, value in bone_drivers.items():
# # key_cleaned = key.replace('_', ' ')
# # if key_cleaned in actions_without_ex:
# # print(f"{key_cleaned} is in action")
# # r.assign_animation_action(rig, )

# for shape_key, bone_target in driving_bones.items():
#     print('Shapekey driven')
#     if bone_target[0].lower() == "basis":
#         pass
#     target_rotation = r.get_highest_bone_rotation_for_driver(rig, bone_target[0])
#     r.assign_animation_action(rig, action_numbers[bone_target[1]])
#     r.corrective_shape_driver(rig, 'Universal Female without mouth', shape_key,bone_target[0], target_rotation)
# # this will be were everything happens


# r.change_frame(0)

sys.path.remove(module_dir)