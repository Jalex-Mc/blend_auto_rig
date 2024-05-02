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
    "neck_02",
    "neck_01",
    "scapula_L",
    "scapula_R",
    "clavicle_L",
    "clavicle_R",
    "breast_L",
    "breast_R",
    "spine_03",
    "spine_02",
    "spine_01",
    "pelvis",
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
    "butt_R",
    "butt_L",
    "femur_L",
    "femur_R",
    "tibia_L",
    "tibia_R",
    "kneeBendDeform_L",
    "kneeBendDeform_R",
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
]

CTRL = ['ROOT', 'head', 'neck_02', 'neck_01', 'neckHead', 'backCTRL', 'spine_03', 'spine_02', 'spine_01', 'pelvis', 'hipTwist', 'humerus_FK_L', 'humerus_FK_R', 'elbowPole_L', 'elbowPole_R', 'forearm_FK_L', 'forearm_FK_R', 'hand_FK_L', 'hand_FK_R', 'hand_IK_CTRL_L', 'hand_IK_CTRL_R', 'index_1_L', 'index_2_L', 'index_3_L', 'index_4_L', 'index_1_R', 'index_2_R', 'index_3_R', 'index_4_R', 'indexRotation_L', 'indexRotation_R', 'middle_1_R', 'middle_2_R', 'middle_3_R', 'middle_4_R', 'middle_1_L', 'middle_2_L', 'middle_3_L', 'middle_4_L', 'middleRotation_L', 'middleRotation_R', 'ring_1_R', 'ring_2_R', 'ring_3_R', 'ring_4_R', 'ring_1_L', 'ring_2_L', 'ring_3_L', 'ring_4_L', 'ringRotation_L', 'ringRotation_R', 'pinky_1_L', 'pinky_2_L', 'pinky_3_L', 'pinky_4_L', 'pinky_1_R', 'pinky_2_R', 'pinky_3_R', 'pinky_4_R', 'pinkyRotation_L', 'pinkyRotation_R', 'thumb_1_L', 'thumb_2_L', 'thumb_3_L', 'thumb_1_R', 'thumb_2_R', 'thumb_3_R', 'thumbRotation_L', 'thumbRotation_R', 'footRollCTRL_L', 'footRollCTRL_R', 'footIK_L', 'footIK_R', 'heelHeight_L', 'heelHeight_R', 'heelPosition_L', 'heelPosition_R', 'toesIK_L', 'toesIK_R', 'bigToeRotation_L', 'bigToeRotation_R', 'indexToeRotation_L', 'indexToeRotation_R', 'midToeRotation_L', 'midToeRotation_R', 'ringToeRotation_L', 'ringToeRotation_R', 'pinkyToeRotation_L', 'pinkyToeRotation_R', 'bigToe_1_L', 'bigToe_1_R', 'bigToe_2_L', 'bigToe_2_R', 'indexToe_1_L', 'indexToe_1_R', 'indexToe_2_L', 'indexToe_2_R', 'indexToe_3_L', 'indexToe_3_R', 'midToe_1_L', 'midToe_1_R', 'midToe_2_L', 'midToe_2_R', 'midToe_3_L', 'midToe_3_R', 'ringToe_1_L', 'ringToe_1_R', 'ringToe_2_L', 'ringToe_2_R', 'ringToe_3_L', 'ringToe_3_R', 'pinkyToe_1_L', 'pinkyToe_1_R', 'pinkyToe_2_L', 'pinkyToe_2_R', 'pinkyToe_3_L', 'pinkyToe_3_R', 'scapula_L', 'scapula_R']
ACCESSORY = ['clavicle_MCH_L', 'clavicle_MCH_R', 'RBF_Upperarm_L', 'RBF_Upperarm_R', 'RBF_leg_L', 'RBF_leg_R', 'IKpoleHelpers_1_L', 'IKpoleHelpers_1_R', 'IKpoleHelpers_2_L', 'IKpoleHelpers_2_R', 'IKpoleHelpers_3_L', 'IKpoleHelpers_3_R', 'MCH_foot_L', 'MCH_foot_R', 'MCH_footRoll_1_L', 'MCH_footRoll_1_R', 'MCH_footRoll_3_L', 'MCH_footRoll_3_R', 'MCH_footRoll_2_L', 'MCH_footRoll_2_R', 'toes_L', 'toes_R']
FK = ['humerus_FK_L', 'humerus_FK_R', 'forearm_FK_L', 'forearm_FK_R', 'armTwist_1_FK_L', 'armTwist_1_FK_R', 'armTwist_2_FK_L', 'armTwist_2_FK_R', 'armTwist_3_FK_L', 'armTwist_3_FK_R', 'hand_FK_L', 'hand_FK_R', 'footFK_L', 'footFK_R']
IK = ['humerus_IK_L', 'humerus_IK_R', 'elbowPole_L', 'elbowPole_R', 'forearm_IK_L', 'forearm_IK_R', 'armTwist_1_IK_L', 'armTwist_1_IK_R', 'armTwist_2_IK_L', 'armTwist_2_IK_R', 'armTwist_3_IK_L', 'armTwist_3_IK_R', 'hand_IK_CTRL_L', 'hand_IK_CTRL_R', 'footIK_L', 'footIK_R', 'toesIK_L', 'toesIK_R']
RBF = ['clavicle_MCH_L', 'clavicle_MCH_R', 'RBF_Upperarm_L', 'RBF_Upperarm_R', 'RBF_leg_L', 'RBF_leg_R']
bones_to_assign = {'Deform': deform_list, 'CTRL': CTRL, 'ACCESSORY': ACCESSORY, 'FK': FK, 'IK': IK, 'RBF': RBF}

def deform_bones(rig_name):
    r.set_mode('OBJECT')
    r.remove_object_selection()
    r.object_selection(rig)
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

## clean up ##

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

sys.path.remove(module_dir)
