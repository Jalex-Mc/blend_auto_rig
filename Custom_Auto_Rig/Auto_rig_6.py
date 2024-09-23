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

### deform & collections ###

deform_list = [
    "head",
    "neck_2",
    "neck_1",
    "scapula_L",
    "scapula_R",
    "clavicle_L",
    "clavicle_R",
    "breast_L",
    "breast_R",
    "spine_3",
    "spine_2",
    "spine_1",
    "pelvis_L",
    "pelvis_R",
    "humerus_L",
    "humerus_R",
    "forearm_L",
    "forearm_R",
    "armTwist_1_L",
    "armTwist_1_R",
    "armTwist_2_L",
    "armTwist_2_R",
    "armTwist_3_L",
    "armTwist_3_R",
    "hand_L",
    "hand_R",
    "hipTwist",
    "butt_R",
    "butt_L",
    "femurDeform_L",
    "femurDeform_R",
    "kneeBendDeform_L",
    "kneeBendDeform_R",
    'femur_L',
    'femur_R',
    'femur_IK_L',
    'femur_IK_R',
    'tibia_IK_L',
    'tibia_IK_R',
    'tibia_L',
    'tibia_R',
    "footFK_L",
    "footFK_R",
    "bigToe_1_L",
    "bigToe_1_R",
    "bigToe_2_L",
    "bigToe_2_R",
    "indexToe_1_L",
    "indexToe_1_R",
    "indexToe_2_L",
    "indexToe_2_R",
    "indexToe_3_L",
    "indexToe_3_R",
    "midToe_1_L",
    "midToe_1_R",
    "midToe_2_L",
    "midToe_2_R",
    "midToe_3_L",
    "midToe_3_R",
    "ringToe_1_L",
    "ringToe_1_R",
    "ringToe_2_L",
    "ringToe_2_R",
    "ringToe_3_L",
    "ringToe_3_R",
    "pinkyToe_1_L",
    "pinkyToe_1_R",
    "pinkyToe_2_L",
    "pinkyToe_2_R",
    "pinkyToe_3_L",
    "pinkyToe_3_R",
    "index_1_L",
    "index_2_L",
    "index_3_L",
    "index_4_L",
    "index_1_R",
    "index_2_R",
    "index_3_R",
    "index_4_R",
    "middle_1_R",
    "middle_2_R",
    "middle_3_R",
    "middle_4_R",
    "middle_1_L",
    "middle_2_L",
    "middle_3_L",
    "middle_4_L",
    "ring_1_R",
    "ring_2_R",
    "ring_3_R",
    "ring_4_R",
    "ring_1_L",
    "ring_2_L",
    "ring_3_L",
    "ring_4_L",
    "pinky_1_L",
    "pinky_2_L",
    "pinky_3_L",
    "pinky_4_L",
    "pinky_1_R",
    "pinky_2_R",
    "pinky_3_R",
    "pinky_4_R",
    "thumb_1_L",
    "thumb_2_L",
    "thumb_3_L",
    "thumb_1_R",
    "thumb_2_R",
    "thumb_3_R",
]

CTRL = ['root', 'head', 'neck_2', 'neck_1', 'neckHead', 'backCTRL','clavicle_L', 'clavicle_R', 'spine_3', 'spine_2', 'spine_1', 'pelvis', 'hipTwist', 'humerus_FK_L', 'humerus_FK_R', 'elbowPole_L', 'elbowPole_R', 'forearm_FK_L', 'forearm_FK_R', 'hand_FK_L', 'hand_FK_R', 'hand_IK_L', 'hand_IK_R', 'index_1_L', 'index_2_L', 'index_3_L', 'index_4_L', 'index_1_R', 'index_2_R', 'index_3_R', 'index_4_R', 'indexRotation_L', 'indexRotation_R', 'middle_1_R', 'middle_2_R', 'middle_3_R', 'middle_4_R', 'middle_1_L', 'middle_2_L', 'middle_3_L', 'middle_4_L', 'middleRotation_L', 'middleRotation_R', 'ring_1_R', 'ring_2_R', 'ring_3_R', 'ring_4_R', 'ring_1_L', 'ring_2_L', 'ring_3_L', 'ring_4_L', 'ringRotation_L', 'ringRotation_R', 'pinky_1_L', 'pinky_2_L', 'pinky_3_L', 'pinky_4_L', 'pinky_1_R', 'pinky_2_R', 'pinky_3_R', 'pinky_4_R', 'pinkyRotation_L', 'pinkyRotation_R', 'thumb_1_L', 'thumb_2_L', 'thumb_3_L', 'thumb_1_R', 'thumb_2_R', 'thumb_3_R', 'thumbRotation_L', 'thumbRotation_R', 'footRollCTRL_L', 'footRollCTRL_R', 'footIK_L', 'footIK_R', 'heelHeight_L', 'heelHeight_R', 'heelPosition_L', 'heelPosition_R', 'toesIK_L', 'toesIK_R', 'bigToeRotation_L', 'bigToeRotation_R', 'indexToeRotation_L', 'indexToeRotation_R', 'midToeRotation_L', 'midToeRotation_R', 'ringToeRotation_L', 'ringToeRotation_R', 'pinkyToeRotation_L', 'pinkyToeRotation_R', 'bigToe_1_L', 'bigToe_1_R', 'bigToe_2_L', 'bigToe_2_R', 'indexToe_1_L', 'indexToe_1_R', 'indexToe_2_L', 'indexToe_2_R', 'indexToe_3_L', 'indexToe_3_R', 'midToe_1_L', 'midToe_1_R', 'midToe_2_L', 'midToe_2_R', 'midToe_3_L', 'midToe_3_R', 'ringToe_1_L', 'ringToe_1_R', 'ringToe_2_L', 'ringToe_2_R', 'ringToe_3_L', 'ringToe_3_R', 'pinkyToe_1_L', 'pinkyToe_1_R', 'pinkyToe_2_L', 'pinkyToe_2_R', 'pinkyToe_3_L', 'pinkyToe_3_R']
CTRL = []
ACCESSORY = ['clavicle_MCH_L', 'clavicle_MCH_R', 'RBF_Upperarm_L', 'RBF_Upperarm_R', 'RBF_leg_L', 'RBF_leg_R', 'IKpoleHelpers_1_L', 'IKpoleHelpers_1_R', 'IKpoleHelpers_2_L', 'IKpoleHelpers_2_R', 'IKpoleHelpers_3_L', 'IKpoleHelpers_3_R', 'MCH_foot_L', 'MCH_foot_R', 'MCH_footRoll_1_L', 'MCH_footRoll_1_R', 'MCH_footRoll_3_L', 'MCH_footRoll_3_R', 'MCH_footRoll_2_L', 'MCH_footRoll_2_R', 'toes_L', 'toes_R']
FK = ['humerus_FK_L', 'humerus_FK_R', 'forearm_FK_L', 'forearm_FK_R', 'armTwist_1_FK_L', 'armTwist_1_FK_R', 'armTwist_2_FK_L', 'armTwist_2_FK_R', 'armTwist_3_FK_L', 'armTwist_3_FK_R', 'hand_FK_L', 'hand_FK_R', 'footFK_L', 'footFK_R']
IK = ['humerus_IK_L', 'humerus_IK_R', 'elbowPole_L', 'elbowPole_R', 'forearm_IK_L', 'forearm_IK_R', 'armTwist_1_IK_L', 'armTwist_1_IK_R', 'armTwist_2_IK_L', 'armTwist_2_IK_R', 'armTwist_3_IK_L', 'armTwist_3_IK_R', 'hand_IK_L', 'hand_IK_R', 'footIK_L', 'footIK_R', 'toesIK_L', 'toesIK_R']
RBF = ['clavicle_MCH_L', 'clavicle_MCH_R', 'RBF_Upperarm_L', 'RBF_Upperarm_R', 'RBF_leg_L', 'RBF_leg_R']
bones_to_assign = {'Deform': deform_list, 'CTRL': CTRL, 'ACCESSORY': ACCESSORY, 'FK': FK, 'IK': IK, 'RBF': RBF}

def deform_bones(rig_name):
    r.set_mode('OBJECT')
    r.remove_object_selection()
    r.object_selection(rig_name)
    r.set_mode('EDIT')
    arm = bpy.data.armatures[rig_name]
    bone_list = r.rig_bone_list(rig_name)

    for item in bone_list:
        bone = arm.edit_bones[item]
        if item in deform_list:
            bone.use_deform = True
        else:
            bone.use_deform = False

deform_bones(rig)
r.create_bone_collections(rig, bones_to_assign)


###############################################################
## create a dictionary for control

ctrls_list = [
    {'Root': 'root'},
    {'Head': ['head', 'neck_2', 'neck_1']},
    {'Head CTRL': 'neckHead'},
    {'L clavicle': 'clavicle_L'},
    {'R clavicle': 'clavicle_R'},
    {'Breast/Pecs': ['breast_L', 'breast_R']},
    {'L arm IK': ['elbowPole_L', 'hand_IK_L']},
    {'R arm IK': ['elbowPole_R', 'hand_IK_R']},
    {'L arm FK': ['humerus_FK_L', 'forearm_FK_L', 'hand_FK_L']},
    {'R arm FK': ['humerus_FK_R', 'forearm_FK_R', 'hand_FK_R']},
    {'L hand': ['pinky_1_L','ring_1_L','middle_1_L','index_1_L','thumb_1_L', 'thumbRotation_L', 'thumb_2_L', 'thumb_3_L', 'indexRotation_L', 'index_2_L', 'index_3_L', 'index_4_L', 'middleRotation_L', 'middle_2_L', 'middle_3_L', 'middle_4_L', 'ringRotation_L', 'ring_2_L', 'ring_3_L', 'ring_4_L', 'pinkyRotation_L', 'pinky_2_L', 'pinky_3_L', 'pinky_4_L']},
    {'R hand': ['pinky_1_R','ring_1_R','middle_1_R','index_1_R','thumb_1_R','thumbRotation_R', 'thumb_2_R', 'thumb_3_R', 'indexRotation_R', 'index_2_R', 'index_3_R', 'index_4_R', 'middleRotation_R', 'middle_2_R', 'middle_3_R', 'middle_4_R', 'ringRotation_R', 'ring_2_R', 'ring_3_R', 'ring_4_R', 'pinkyRotation_R', 'pinky_2_R', 'pinky_3_R', 'pinky_4_R']},
    {'Spine': ['spine_3', 'spine_2', 'spine_1']},
    {'Back': 'backCTRL'},
    {'Hip': 'hipTwist'},
    {'Pelvis': 'pelvis'},
    {'L Leg IK': ['kneePole_L', 'footIK_L', 'toesIK_L', 'footRollCTRL_L']},
    {'R Leg IK': ['kneePole_R', 'footIK_R', 'toesIK_R', 'footRollCTRL_R']},
    {'L heel position': ['heelPosition_L', 'heelHeight_L']},
    {'R heel position': ['heelPosition_R', 'heelHeight_R']},
    {'L toes': ['toes_L', 'bigToeRotation_L', 'bigToe_1_L', 'bigToe_2_L', 'indexToeRotation_L', 'indexToe_1_L', 'indexToe_2_L', 'indexToe_3_L', 'midToeRotation_L', 'midToe_1_L', 'midToe_2_L', 'midToe_3_L', 'ringToeRotation_L', 'ringToe_1_L', 'ringToe_2_L', 'ringToe_3_L', 'pinkyToeRotation_L', 'pinkyToe_1_L', 'pinkyToe_2_L', 'pinkyToe_3_L']},
    {'R toes': ['toes_R', 'bigToeRotation_R', 'bigToe_1_R', 'bigToe_2_R', 'indexToeRotation_R', 'indexToe_1_R', 'indexToe_2_R', 'indexToe_3_R', 'midToeRotation_R', 'midToe_1_R', 'midToe_2_R', 'midToe_3_R', 'ringToeRotation_R', 'ringToe_1_R', 'ringToe_2_R', 'ringToe_3_R', 'pinkyToeRotation_R', 'pinkyToe_1_R', 'pinkyToe_2_R', 'pinkyToe_3_R']},
    {'L Leg FK': ['footFK_L', 'tibia_FK_L', 'femur_FK_L']},
    {'R Leg FK': ['footFK_R', 'tibia_FK_R', 'femur_FK_R']},
    {'L foot': 'footFK_L'},
    {'R foot': 'footFK_R'}]

# print(len(ctrls_list))

# for item in ctrls_list:
#     for key, value in item.items():
#         if value != list:
#             bcoll_child = armature.collections.new(key, parent=bcoll_root)
#         print(value)

# for index, item in enumerate(deform_list):
    # print(ctrls_list[index])

# Create bone collections
## putting bones in ctrl 

############################

armature = bpy.data.objects["Female Transfer Rig"].data
# print(armature.collections["CTRL"])

bcoll_root = armature.collections["CTRL"]

for item in ctrls_list:
    for key, value in item.items():
        if type(value) != list:
            bcoll_child = armature.collections.new(key, parent=bcoll_root)
            bcoll_child.assign(armature.bones[value])
        else:
            bcoll_child = armature.collections.new(key, parent=bcoll_root)
            for bone in value:
                bcoll_child.assign(armature.bones[bone])

        print(value)

# bcoll_child = armature.collections.new("Child Collection", parent=bcoll_root)

# # Moving the bone collection after it has been created.
# bcoll = armature.collections.new("collection")
# bcoll.parent = bcoll_root  # Assign a new parent collection.
# bcoll.child_number = 0     # Move to be the first of its siblings.

# # Access to the top level (aka 'root') collections:
# for bcoll in armature.collections:
#     print(f'Root collection: {bcoll.name}')

# # Access to all collections:
# for bcoll in armature.collections_all:
#     print(f'Collection: {bcoll.name}')

# # Assigned bones can be retrieved hierarchically:
# bcoll_child.assign(armature.bones['backCTRL'])
# for bone in bcoll_root.bones_recursive:
#     print(bone.name)

##########################################################
# rig clean up



# r.lock_rotation(rig, 'humerus_FK_L', y=True, z=True)
# r.lock_rotation(rig, 'humerus_FK_R', y=True, z=True)

left_hand_rotation_bones = ['thumbRotation_L', 'indexRotation_L', 'middleRotation_L', 'ringRotation_L', 'pinkyRotation_L']

for bone in left_hand_rotation_bones:
    r.set_mode('OBJECT')
    r.remove_edit_and_arm_selection(rig)
    r.set_mode('OBJECT')
    r.remove_object_selection()
    r.object_selection(rig)
    r.set_mode('EDIT')
    arm = bpy.data.armatures[rig]
    bone = arm.edit_bones[bone]
    bone.roll *= -1 

r.limit_rotation(rig, 'hipTwist', max_x=r.degree_to_radians(25), min_x=r.degree_to_radians(-35), max_y=r.degree_to_radians(15), min_y=r.degree_to_radians(-15), max_z=r.degree_to_radians(30), min_z=r.degree_to_radians(-20), limit_x=True, limit_y=True,limit_z=True, owner_space='LOCAL')

## bone color ##

red = ['head', 'neck_2', 'neck_1', 'spine_3', 'spine_2', 'spine_1', 'hand_IK_L']
blue = ['hand_IK_R']
theme11 = ['humerus_FK_R', 'forearm_FK_R','hand_FK_R', 'pelvis', 'tibia_FK_R', 'femur_FK_R']
theme12 = ['footIK_L', 'footIK_R', ]
yellow = ['hipTwist', 'root']
neon_green = ['neckHead', 'backCTRL']
orange = ['elbowPole_L', 'kneePole_L']
bluegreen = ['elbowPole_R', 'kneePole_R']
purple = ['heelHeight_L', 'heelHeight_R', 'bigToe_1_L', 'bigToe_1_R', 'bigToe_2_L', 'bigToe_2_R', 'indexToe_1_L', 'indexToe_1_R', 'indexToe_2_L', 'indexToe_2_R', 'indexToe_3_L', 'indexToe_3_R', 'midToe_1_L', 'midToe_1_R', 'midToe_2_L', 'midToe_2_R', 'midToe_3_L', 'midToe_3_R', 'ringToe_1_L', 'ringToe_1_R', 'ringToe_2_L', 'ringToe_2_R', 'ringToe_3_L', 'ringToe_3_R', 'pinkyToe_1_L', 'pinkyToe_1_R', 'pinkyToe_2_L', 'pinkyToe_2_R', 'pinkyToe_3_L', 'pinkyToe_3_R']
pink = ['footRollCTRL_L', 'footRollCTRL_R', 'toesIK_L', 'toesIK_R', 'bigToeRotation_L', 'bigToeRotation_R', 'indexToeRotation_L', 'indexToeRotation_R', 'midToeRotation_L', 'midToeRotation_R', 'ringToeRotation_L', 'ringToeRotation_R', 'pinkyToeRotation_L', 'pinkyToeRotation_R']
green = ['clavicle_L', 'clavicle_R', 'humerus_FK_L', 'forearm_FK_L', 'hand_FK_L', 'heelPosition_L', 'heelPosition_R', 'tibia_FK_L', 'femur_FK_L']

r.set_mode('OBJECT')
r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.object_selection(rig)
obj = bpy.context.active_object

if obj and obj.type == 'ARMATURE':
    # Iterate through the bones
    for bone in obj.pose.bones:
        if bone.name in red:
            bone.color.palette = 'THEME01'
        if bone.name in blue:
             bone.color.palette = 'THEME04'
        if bone.name in theme11:
            bone.color.palette = 'THEME11'
        if bone.name in theme12:
            bone.color.palette = 'THEME12'
        if bone.name in yellow:
            bone.color.palette = 'THEME09'
        if bone.name in neon_green:
            bone.color.palette = 'THEME03'
        if bone.name in orange:
            bone.color.palette = 'THEME02'
        if bone.name in bluegreen:
            bone.color.palette = 'THEME08'
        if bone.name in purple:
            bone.color.palette = 'THEME06'
        if bone.name in pink:
            bone.color.palette = 'THEME05'
        if bone.name in green:
            bone.color.palette = 'THEME15'


## file clean up ##

r.set_mode('OBJECT')
r.remove_object_selection()
r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()


col = bpy.data.collections.get("Collection")
if col:
   for obj in col.objects:
        if 'Empty' in obj.name:
           print(obj.name)
           obj.select_set(True)
        else:
           print(obj.name)
bpy.ops.object.delete()

r.remove_object_selection()

arm = bpy.data.armatures[rig]
arm.collections.get("Deform").is_visible = False
arm.collections.get("ACCESSORY").is_visible = False
arm.collections.get("FK").is_visible = False
arm.collections.get("IK").is_visible = False
arm.collections.get("RBF").is_visible = False

sys.path.remove(module_dir)
