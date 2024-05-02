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


#### Leg Continuation ####

rig = 'Female Transfer Rig'


# 45-54
set_mode("OBJECT")
remove_object_selection()
# local_pos, tail_pos = object_location('ankleHelper_L')
helper_head, tail_i_dont_need = bone_global_locations(rig, 'femur_L')
helper_tail, tail_i_dont_need = bone_global_locations(rig, 'MCH_foot_L')
helper_roll = bone_roll(rig, 'femur_L')
new_bone_creation(helper_head, helper_tail, 'IKpoleHelpers_1_L', rig, None, False, helper_roll)
change_bone_length('IKpoleHelpers_1_L', rig, .12)

new_head_point = (helper_head + helper_tail) / 2
new_bone_creation(new_head_point, helper_tail, 'IKpoleHelpers_2_L', rig, None, False, helper_roll)
change_bone_length('IKpoleHelpers_2_L', rig, .12)

last_tail = [helper_tail[0], helper_tail[1], -.02]
new_bone_creation(helper_tail, last_tail, 'IKpoleHelpers_3_L', rig, None, False, helper_roll)
parent_bone(rig, 'IKpoleHelpers_1_L', 'butt_L', False)
parent_bone(rig, 'IKpoleHelpers_2_L', 'butt_L', False)
parent_bone(rig, 'IKpoleHelpers_3_L', 'footIK_L', False)

set_mode("OBJECT")
remove_object_selection()
# local_pos, head_pos = object_location('IKhelper01_EMPTY_R')
# local_pos, tail_pos = object_location('ankleHelper_R')
helper_head, tail_i_dont_need = bone_global_locations(rig, 'femur_R')
helper_tail, tail_i_dont_need = bone_global_locations(rig, 'MCH_foot_R')
helper_roll = bone_roll(rig, 'femur_R')
new_bone_creation(helper_head, helper_tail, 'IKpoleHelpers_1_R', rig, None, False, helper_roll)
change_bone_length('IKpoleHelpers_1_R', rig, .12)

new_head_point = (helper_head + helper_tail) / 2
new_bone_creation(new_head_point, helper_tail, 'IKpoleHelpers_2_R', rig, None, False, helper_roll)
change_bone_length('IKpoleHelpers_2_R', rig, .12)

last_tail = [helper_tail[0], helper_tail[1], -.02]
new_bone_creation(helper_tail, last_tail, 'IKpoleHelpers_3_R', rig, None, False, helper_roll)

parent_bone(rig, 'IKpoleHelpers_1_R', 'butt_R', False)
parent_bone(rig, 'IKpoleHelpers_2_R', 'butt_R', False)
parent_bone(rig, 'IKpoleHelpers_3_R', 'footIK_R', False)

# 55-58
copy_transforms(rig, 'IKpoleHelpers_2_L', 1.0, 'IKpoleHelpers_1_L')
copy_transforms(rig, 'IKpoleHelpers_2_L', 0.5, 'IKpoleHelpers_3_L')
damped_track(rig, 'IKpoleHelpers_2_L', subtarget='IKpoleHelpers_3_L', track_axis='TRACK_Y')
# parent_bone(rig, 'kneePole_L', 'IKpoleHelpers_2_L', False)

copy_transforms(rig, 'IKpoleHelpers_2_R', 1.0, 'IKpoleHelpers_1_R')
copy_transforms(rig, 'IKpoleHelpers_2_R', 0.5, 'IKpoleHelpers_3_R')
damped_track(rig, 'IKpoleHelpers_2_R', subtarget='IKpoleHelpers_3_R', track_axis='TRACK_Y')
# parent_bone(rig, 'kneePole_R', 'IKpoleHelpers_2_R', False)

# 59-66
pos_1, pos_2 = bone_global_locations(rig, 'tibia_L')
roll = (bone_roll(rig, 'tibia_L') + 0.383972)
new_bone_creation(pos_1, pos_2, 'kneeBendDeform_L', rig, 'tibia_L', False, roll)
flip_bone(rig, 'kneeBendDeform_L')
parent_bone(rig, 'kneeBendDeform_L', 'tibia_L', False)
transformation(
    rig,
    "kneeBendDeform_L",
    from_max_z_rot=degree_to_radians(160),
    map_from="ROTATION",
    map_to="ROTATION",
    subtarget="tibia_L",
    target=rig,
    to_max_z_rot=degree_to_radians(8),
    owner_space="LOCAL",
    target_space="LOCAL",
)

pos_1, pos_2 = bone_global_locations(rig, 'femur_L')
roll = bone_roll(rig, 'femur_L')
new_bone_creation(pos_1, pos_2, 'femurDeform_L', rig, 'femur_L', False, roll)
flip_bone(rig, 'femurDeform_L')
parent_bone(rig, 'femurDeform_L', 'femur_L', False)
transformation(
    rig,
    "femurDeform_L",
    from_min_z_rot=degree_to_radians(-160),
    from_max_z_rot=0,
    map_from="ROTATION",
    map_to="ROTATION",
    subtarget="femur_L",
    target=rig,
    to_min_z_rot=degree_to_radians(-8),
    to_max_z_rot=0,
    owner_space="LOCAL",
    target_space="LOCAL",
)

pos_1, pos_2 = bone_global_locations(rig, 'tibia_R')
roll = (bone_roll(rig, 'tibia_R') - 0.383972)
new_bone_creation(pos_1, pos_2, 'kneeBendDeform_R', rig, 'tibia_R', False, roll)
flip_bone(rig, 'kneeBendDeform_R')
parent_bone(rig, 'kneeBendDeform_R', 'tibia_R', False)
transformation(
    rig,
    "kneeBendDeform_R",
    from_min_z_rot=degree_to_radians(-160),
    map_from="ROTATION",
    map_to="ROTATION",
    subtarget="tibia_R",
    target=rig,
    to_min_z_rot=degree_to_radians(-8),
    owner_space="LOCAL",
    target_space="LOCAL",
)
## fix roll
pos_1, pos_2 = bone_global_locations(rig, 'femur_R')
roll = bone_roll(rig, 'femur_R')
new_bone_creation(pos_1, pos_2, 'femurDeform_R', rig, 'femur_R', False, roll)
flip_bone(rig, 'femurDeform_R')
parent_bone(rig, 'femurDeform_R', 'femur_R', False)
transformation(
    rig,
    "femurDeform_R",
    from_max_z_rot=degree_to_radians(160),
    map_from="ROTATION",
    map_to="ROTATION",
    subtarget="femur_R",
    target=rig,
    to_max_z_rot=degree_to_radians(8),
    owner_space="LOCAL",
    target_space="LOCAL",
)

parent_bone(rig, 'kneeBendDeform_L', 'tibia_L', False)
parent_bone(rig, 'femurDeform_L', 'femur_L', False)

ik_properties(rig, 'tibia_L', lock_ik_x=True, lock_ik_y=True)
ik_properties(rig, 'tibia_R', lock_ik_x=True, lock_ik_y=True)

set_mode('OBJECT')
remove_edit_and_arm_selection(rig)
set_mode('OBJECT')
remove_object_selection()

###### Cleaning ######

rig = 'Female Transfer Rig'

set_mode('OBJECT')
remove_object_selection()
remove_edit_and_arm_selection(rig)

################################
######### SPINE ################

duplicate_bone(rig, 'pelvis', 'hipTwist')
flip_bone(rig, 'hipTwist')
limit_rotation(rig, 'hipTwist', max_x=degree_to_radians(25),min_x=degree_to_radians(-25),max_y=degree_to_radians(15),min_y=degree_to_radians(-15),max_z=degree_to_radians(10),min_z=degree_to_radians(-10),limit_x=True,limit_y=True,limit_z=True,owner_space='LOCAL',target_space='LOCAL')
parent_bone(rig, 'hipTwist', 'pelvis', False)
head, dontneed = bone_global_locations(rig, 'pelvis')
dontneed, tail = bone_global_locations(rig, 'spine_03')
head[1] += .1
tail[1] += .1
new_bone_creation(head, tail, 'backCTRL', rig, 'pelvis', False, 0)

parent_bone(rig, 'backCTRL', 'pelvis', False)
spines = ['spine_01', 'spine_02', 'spine_03']
for item in spines:
    copy_rotation(rig, item, influence=1.0, euler_order='YZX', mix_mode='AFTER', subtarget='backCTRL',use_x=True,use_y=True,use_z=True, target_space='LOCAL', owner_space='LOCAL')
    arm = bpy.data.objects[rig]
    bone = select_bone_as_active_pose(rig, item)
    bone.constraints[-1].mix_mode = 'AFTER'
    if item == 'spine_01':
        limit_rotation(rig, item, max_x=degree_to_radians(35),min_x=degree_to_radians(-25),max_y=degree_to_radians(15),min_y=degree_to_radians(-15),max_z=degree_to_radians(15),min_z=degree_to_radians(-15),limit_x=True,limit_y=True,limit_z=True,owner_space='LOCAL', target_space='LOCAL')
    if item == 'spine_02':
        limit_rotation(rig, item, max_x=degree_to_radians(40),min_x=degree_to_radians(-25),max_y=degree_to_radians(20),min_y=degree_to_radians(-20),max_z=degree_to_radians(24),min_z=degree_to_radians(-24),limit_x=True,limit_y=True,limit_z=True,owner_space='LOCAL', target_space='LOCAL')
    if item == 'spine_03':
        limit_rotation(rig, item, max_x=degree_to_radians(35),min_x=degree_to_radians(-25),max_y=degree_to_radians(12),min_y=degree_to_radians(-12),max_z=degree_to_radians(20),min_z=degree_to_radians(-20),limit_x=True,limit_y=True,limit_z=True,owner_space='LOCAL', target_space='LOCAL')

head, unneeded = bone_global_locations(rig, 'neck_01')
unneeded, tail = bone_global_locations(rig, 'neck_02')

head[1] += .08
tail[1] += .08

new_bone_creation(head, tail, 'neckHead', rig, 'spine_03', False, 0)
copy_rotation(rig, 'neck_01', influence=1.0, euler_order='YZX', mix_mode='AFTER', subtarget='neckHead', use_x=True, use_y=True, use_z=True, target_space='LOCAL',owner_space='LOCAL')
copy_rotation(rig, 'head', influence=1.0, euler_order='YZX', mix_mode='AFTER', subtarget='neckHead', use_x=True, use_y=True, use_z=True, target_space='LOCAL',owner_space='LOCAL')

sys.path.remove(module_dir)
