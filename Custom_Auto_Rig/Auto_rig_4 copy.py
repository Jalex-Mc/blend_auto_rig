import bpy
from mathutils import Vector
import math
import os
import sys

'''
ADJUST
IK POLE ROTATIONS
BEFORE 
STARTING
THIS
SCRIPT
'''

# Add the directory containing your module to the Python path (before importing it)
module_dir = os.path.abspath('O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig')
sys.path.insert(0, module_dir)

# Now you can import your module as usual
from rig_func import Rigging_Functions

# initialize the class
r = Rigging_Functions()


#### continuation ###


rig = 'Female Transfer Rig'

left_arm_bones = ['humerus_L', 'armTwist_1_L', 'forearm_L', 'armTwist_2_L', 'armTwist_3_L', 'hand_L']
left_arm_FK_bones = ['humerus_FK_L', 'armTwist_FK_L', 'forearm_FK_L', 'armTwist_FK_L', 'armTwist_FK_L', 'hand_FK_L']
left_arm_IK_bones = ['humerus_IK_L', 'armTwist_IK_L', 'forearm_IK_L', 'armTwist_IK_L', 'armTwist_IK_L', 'hand_IK_L']
right_arm_bones = ['humerus_R', 'armTwist_1_R', 'forearm_R', 'armTwist_2_R', 'armTwist_3_R', 'hand_R']
right_arm_FK_bones = ['humerus_FK_R', 'armTwist_FK_R', 'forearm_FK_R', 'armTwist_FK_R', 'armTwist_FK_R', 'hand_FK_R']
right_arm_IK_bones = ['humerus_IK_R', 'armTwist_IK_R', 'forearm_IK_R', 'armTwist_IK_R', 'armTwist_IK_R', 'hand_IK_R']

for index, item in enumerate(left_arm_bones):
    # print(f"item-{item}")
    # print(f'index-{index}')
    r.copy_transforms(rig, item, 1, left_arm_IK_bones[index])
    # bone = r.select_bone_as_active_pose(rig, item)
    # copy = bone.constraints[-1]
    # copy.target = bpy.data.objects[rig]
# for index, item in enumerate(left_arm_bones):
#     r.copy_transforms(rig, item, 1, left_arm_FK_bones[index])
# for index, item in enumerate(right_arm_bones):
#     r.copy_transforms(rig, item, 1, right_arm_IK_bones[index])
# for index, item in enumerate(right_arm_bones):
#     r.copy_transforms(rig, item, 1, right_arm_FK_bones[index])

#hardcoded name fix -

# r.renamer(rig, 'armTwist_FK_L', 'armTwist_1_FK_L')
# r.renamer(rig, 'armTwist_FK_L.001', 'armTwist_2_FK_L')
# r.renamer(rig, 'armTwist_FK_L.002', 'armTwist_3_FK_L')
# r.renamer(rig, 'armTwist_IK_L', 'armTwist_1_IK_L')
# r.renamer(rig, 'armTwist_IK_L.001', 'armTwist_2_IK_L')
# r.renamer(rig, 'armTwist_IK_L.002', 'armTwist_3_IK_L')

# r.renamer(rig, 'armTwist_FK_R', 'armTwist_1_FK_R')
# r.renamer(rig, 'armTwist_FK_R.001', 'armTwist_2_FK_R')
# r.renamer(rig, 'armTwist_FK_R.002', 'armTwist_3_FK_R')
# r.renamer(rig, 'armTwist_IK_R', 'armTwist_1_IK_R')
# r.renamer(rig, 'armTwist_IK_R.001', 'armTwist_2_IK_R')
# r.renamer(rig, 'armTwist_IK_R.002', 'armTwist_3_IK_R')


# r.copy_rotation(rig, 'armTwist_1_IK_L',influence=0.3 ,subtarget='armTwist_2_IK_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
# r.copy_rotation(rig, 'armTwist_2_IK_L',influence=0.727 ,subtarget='armTwist_3_IK_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
# r.copy_rotation(rig, 'armTwist_3_IK_L',subtarget='hand_IK_L', use_y=True, target_space='LOCAL', owner_space='LOCAL')

# r.copy_rotation(rig, 'armTwist_1_FK_L',influence=0.3 ,subtarget='armTwist_2_FK_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
# r.copy_rotation(rig, 'armTwist_2_FK_L',influence=0.727 ,subtarget='armTwist_3_FK_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
# r.copy_rotation(rig, 'armTwist_3_FK_L',subtarget='hand_FK_L', use_y=True, target_space='LOCAL', owner_space='LOCAL')

# r.copy_rotation(rig, 'armTwist_1_IK_R',influence=0.3 ,subtarget='armTwist_2_IK_R', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
# r.copy_rotation(rig, 'armTwist_2_IK_R',influence=0.727 ,subtarget='armTwist_3_IK_R', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
# r.copy_rotation(rig, 'armTwist_3_IK_R',subtarget='hand_IK_R', use_y=True, target_space='LOCAL', owner_space='LOCAL')

# r.copy_rotation(rig, 'armTwist_1_FK_R',influence=0.3 ,subtarget='armTwist_2_FK_R', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
# r.copy_rotation(rig, 'armTwist_2_FK_R',influence=0.727 ,subtarget='armTwist_3_FK_R', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
# r.copy_rotation(rig, 'armTwist_3_FK_R',subtarget='hand_FK_R', use_y=True, target_space='LOCAL', owner_space='LOCAL')

# ## rbf bone creation ##

# clavicle_roll = r.bone_roll(rig, 'clavicle_L')
# r.duplicate_bones(rig, 'clavicle_L', 'clavicle_MCH_L', 'spine_3', False, clavicle_roll, False)
# humerus_roll = r.bone_roll(rig, 'humerus_L')
# r.duplicate_bones(rig, 'humerus_L', 'RBF_Upperarm_L', 'humerus_L', False, humerus_roll, False)
# femur_roll = r.bone_roll(rig, 'femur_L')
# r.duplicate_bones(rig, 'femur_L', 'RBF_leg_L', 'femur_L', False, femur_roll, False)
# r.copy_rotation(rig, 'clavicle_L', mix_mode='AFTER', subtarget='clavicle_MCH_L', use_x=True,use_y=True,use_z=True, target_space='LOCAL', owner_space='LOCAL')


# clavicle_roll = r.bone_roll(rig, 'clavicle_R')
# r.duplicate_bones(rig, 'clavicle_R', 'clavicle_MCH_R', 'spine_3', False, clavicle_roll, False)
# humerus_roll = r.bone_roll(rig, 'humerus_R')
# r.duplicate_bones(rig, 'humerus_R', 'RBF_Upperarm_R', 'humerus_R', False, humerus_roll, False)
# femur_roll = r.bone_roll(rig, 'femur_R')
# r.duplicate_bones(rig, 'femur_R', 'RBF_leg_R', 'femur_R', False, femur_roll, False)
# r.copy_rotation(rig, 'clavicle_R', mix_mode='AFTER', subtarget='clavicle_MCH_R', use_x=True,use_y=True,use_z=True, target_space='LOCAL', owner_space='LOCAL')

# r.parent_bone(rig, 'clavicle_MCH_R', 'spine_3', False)
# r.parent_bone(rig, 'clavicle_MCH_L', 'spine_3', False)

# r.parent_bone(rig, 'hand_FK_L', 'forearm_FK_L', True)
# r.parent_bone(rig, 'hand_FK_R', 'forearm_FK_R', True)

# sys.path.remove(module_dir)
