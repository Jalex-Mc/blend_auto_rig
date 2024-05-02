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

# initialize the methods
set_mode = Rigging_Functions.set_mode
remove_object_selection = Rigging_Functions.remove_object_selection
apply_scale = Rigging_Functions.apply_scale
select_bone_as_active_edit = Rigging_Functions.select_bone_as_active_edit
object_selection = Rigging_Functions.object_selection
remove_edit_and_arm_selection = Rigging_Functions.remove_edit_and_arm_selection
select_bone = Rigging_Functions.select_bone
select_bone_as_active_pose = Rigging_Functions.select_bone_as_active_pose
remove_constraints = Rigging_Functions.remove_constraints
degree_to_radians = Rigging_Functions.degree_to_radians
bone_roll = Rigging_Functions.bone_roll
create_IK = Rigging_Functions.create_IK
limit_rotation = Rigging_Functions.limit_rotation
limit_location = Rigging_Functions.limit_location
limit_scale = Rigging_Functions.limit_scale
copy_rotation = Rigging_Functions.copy_rotation
copy_location = Rigging_Functions.copy_location
copy_scale = Rigging_Functions.copy_scale
copy_transforms = Rigging_Functions.copy_transforms
damped_track = Rigging_Functions.damped_track
transformation = Rigging_Functions.transformation
ik_properties = Rigging_Functions.ik_properties
subdivide_bone = Rigging_Functions.subdivide_bone
rig_bone_list = Rigging_Functions.rig_bone_list
create_root_bone = Rigging_Functions.create_root_bone
parent_bone = Rigging_Functions.parent_bone
bone_length = Rigging_Functions.bone_length
change_bone_length = Rigging_Functions.change_bone_length
lock_location = Rigging_Functions.lock_location
lock_rotation = Rigging_Functions.lock_rotation
lock_scale = Rigging_Functions.lock_scale
eular_change = Rigging_Functions.eular_change
renamer = Rigging_Functions.renamer
duplicate_bone = Rigging_Functions.duplicate_bone
get_bone_location = Rigging_Functions.get_bone_location
move_bone_world_location = Rigging_Functions.move_bone_world_location
bone_global_location = Rigging_Functions.bone_global_location
bone_global_locations = Rigging_Functions.bone_global_locations
object_location = Rigging_Functions.object_location
new_bone_creation_using_duplication = Rigging_Functions.new_bone_creation_using_duplication
new_bone_creation = Rigging_Functions.new_bone_creation_using_duplication
extrude_out = Rigging_Functions.extrude_out
duplication_chain =  Rigging_Functions.duplication_chain
flip_bone = Rigging_Functions.flip_bone
create_bone_collections = Rigging_Functions.create_bone_collections
duplicate_bones = Rigging_Functions.duplicate_bones
move_head_or_tail = Rigging_Functions.move_head_or_tail


#### continuation ###

rig = 'Female Transfer Rig'

left_arm_bones = ['humerus_L', 'armTwist_1_L', 'forearm_L', 'armTwist_2_L', 'armTwist_3_L', 'hand_L']
left_arm_FK_bones = ['humerus_FK_L', 'armTwist_FK_L', 'forearm_FK_L', 'armTwist_FK_L', 'armTwist_FK_L', 'hand_FK_L']
left_arm_IK_bones = ['humerus_IK_L', 'armTwist_IK_L', 'forearm_IK_L', 'armTwist_IK_L', 'armTwist_IK_L', 'handIK_CTRL_L']
right_arm_bones = ['humerus_R', 'armTwist_1_R', 'forearm_R', 'armTwist_2_R', 'armTwist_3_R', 'hand_R']
right_arm_FK_bones = ['humerus_FK_R', 'armTwist_FK_R', 'forearm_FK_R', 'armTwist_FK_R', 'armTwist_FK_R', 'hand_FK_R']
right_arm_IK_bones = ['humerus_IK_R', 'armTwist_IK_R', 'forearm_IK_R', 'armTwist_IK_R', 'armTwist_IK_R', 'handIK_CTRL_R']

for index, item in enumerate(left_arm_bones):
    copy_transforms(rig, item, 1, left_arm_IK_bones[index])
for index, item in enumerate(left_arm_bones):
    copy_transforms(rig, item, 1, left_arm_FK_bones[index])
for index, item in enumerate(right_arm_bones):
    copy_transforms(rig, item, 1, right_arm_IK_bones[index])
for index, item in enumerate(right_arm_bones):
    copy_transforms(rig, item, 1, right_arm_FK_bones[index])

#hardcoded name fix, tired -

renamer(rig, 'armTwist_FK_L', 'armTwist_1_FK_L')
renamer(rig, 'armTwist_FK_L.001', 'armTwist_2_FK_L')
renamer(rig, 'armTwist_FK_L.002', 'armTwist_3_FK_L')
renamer(rig, 'armTwist_IK_L', 'armTwist_1_IK_L')
renamer(rig, 'armTwist_IK_L.001', 'armTwist_2_IK_L')
renamer(rig, 'armTwist_IK_L.002', 'armTwist_3_IK_L')

renamer(rig, 'armTwist_FK_R', 'armTwist_1_FK_R')
renamer(rig, 'armTwist_FK_R.001', 'armTwist_2_FK_R')
renamer(rig, 'armTwist_FK_R.002', 'armTwist_3_FK_R')
renamer(rig, 'armTwist_IK_R', 'armTwist_1_IK_R')
renamer(rig, 'armTwist_IK_R.001', 'armTwist_2_IK_R')
renamer(rig, 'armTwist_IK_R.002', 'armTwist_3_IK_R')


copy_rotation(rig, 'armTwist_1_IK_L',influence=0.3 ,subtarget='armTwist_2_IK_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
copy_rotation(rig, 'armTwist_2_IK_L',influence=0.727 ,subtarget='armTwist_3_IK_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
copy_rotation(rig, 'armTwist_3_IK_L',subtarget='handIK_CTRL_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')

copy_rotation(rig, 'armTwist_1_FK_L',influence=0.3 ,subtarget='armTwist_2_FK_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
copy_rotation(rig, 'armTwist_2_FK_L',influence=0.727 ,subtarget='armTwist_3_FK_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
copy_rotation(rig, 'armTwist_3_FK_L',subtarget='hand_FK_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')

copy_rotation(rig, 'armTwist_1_IK_R',influence=0.3 ,subtarget='armTwist_2_IK_R', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
copy_rotation(rig, 'armTwist_2_IK_R',influence=0.727 ,subtarget='armTwist_3_IK_R', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
copy_rotation(rig, 'armTwist_3_IK_R',subtarget='handIK_CTRL_R', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')

copy_rotation(rig, 'armTwist_1_FK_R',influence=0.3 ,subtarget='armTwist_2_FK_R', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
copy_rotation(rig, 'armTwist_2_FK_R',influence=0.727 ,subtarget='armTwist_3_FK_R', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
copy_rotation(rig, 'armTwist_3_FK_R',subtarget='hand_FK_R', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')

## rbf bone creation ##

clavicle_roll = bone_roll(rig, 'clavicle_L')
duplicate_bones(rig, 'clavicle_L', 'clavicle_MCH_L', 'clavicle_L', False, clavicle_roll, False)
humerus_roll = bone_roll(rig, 'humerus_L')
duplicate_bones(rig, 'humerus_L', 'RBF_Upperarm_L', 'humerus_L', False, clavicle_roll, False)
femur_roll = bone_roll(rig, 'femur_L')
duplicate_bones(rig, 'femur_L', 'RBF_leg_L', 'femur_L', False, clavicle_roll, False)
copy_rotation(rig, 'clavicle_L', mix_mode='AFTER', subtarget='clavicle_MCH_L', use_x=True,use_y=True,use_z=True, target_space='LOCAL', owner_space='LOCAL')


clavicle_roll = bone_roll(rig, 'clavicle_R')
duplicate_bones(rig, 'clavicle_R', 'clavicle_MCH_R', 'clavicle_R', False, clavicle_roll, False)
humerus_roll = bone_roll(rig, 'humerus_R')
duplicate_bones(rig, 'humerus_R', 'RBF_Upperarm_R', 'humerus_R', False, clavicle_roll, False)
femur_roll = bone_roll(rig, 'femur_R')
duplicate_bones(rig, 'femur_R', 'RBF_leg_R', 'femur_R', False, clavicle_roll, False)
copy_rotation(rig, 'clavicle_R', mix_mode='AFTER', subtarget='clavicle_MCH_R', use_x=True,use_y=True,use_z=True, target_space='LOCAL', owner_space='LOCAL')

sys.path.remove(module_dir)
