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

# initialize the Class
r = Rigging_Functions()


#### Leg Continuation ####

rig = 'Female Transfer Rig'


# 45-54
r.set_mode("OBJECT")
r.remove_object_selection()
# local_pos, tail_pos = object_location('ankleHelper_L')
helper_head, tail_i_dont_need = r.bone_global_locations(rig, 'femur_L')
helper_tail, tail_i_dont_need = r.bone_global_locations(rig, 'MCH_foot_L')
helper_roll = r.bone_roll(rig, 'femur_L')
r.new_bone_creation(helper_head, helper_tail, 'IKpoleHelpers_1_L', rig, None, False, helper_roll)
r.change_bone_length('IKpoleHelpers_1_L', rig, .12)

new_head_point = (helper_head + helper_tail) / 2
r.new_bone_creation(new_head_point, helper_tail, 'IKpoleHelpers_2_L', rig, None, False, helper_roll)
r.change_bone_length('IKpoleHelpers_2_L', rig, .12)

last_tail = [helper_tail[0], helper_tail[1], -.02]
r.new_bone_creation(helper_tail, last_tail, 'IKpoleHelpers_3_L', rig, None, False, helper_roll)
r.parent_bone(rig, 'IKpoleHelpers_1_L', 'butt_L', False)
r.parent_bone(rig, 'IKpoleHelpers_2_L', 'butt_L', False)
r.parent_bone(rig, 'IKpoleHelpers_3_L', 'footIK_L', False)

r.set_mode("OBJECT")
r.remove_object_selection()
# local_pos, head_pos = object_location('IKhelper01_EMPTY_R')
# local_pos, tail_pos = object_location('ankleHelper_R')
helper_head, tail_i_dont_need = r.bone_global_locations(rig, 'femur_R')
helper_tail, tail_i_dont_need = r.bone_global_locations(rig, 'MCH_foot_R')
helper_roll = r.bone_roll(rig, 'femur_R')
r.new_bone_creation(helper_head, helper_tail, 'IKpoleHelpers_1_R', rig, None, False, helper_roll)
r.change_bone_length('IKpoleHelpers_1_R', rig, .12)

new_head_point = (helper_head + helper_tail) / 2
r.new_bone_creation(new_head_point, helper_tail, 'IKpoleHelpers_2_R', rig, None, False, helper_roll)
r.change_bone_length('IKpoleHelpers_2_R', rig, .12)

last_tail = [helper_tail[0], helper_tail[1], -.02]
r.new_bone_creation(helper_tail, last_tail, 'IKpoleHelpers_3_R', rig, None, False, helper_roll)

r.parent_bone(rig, 'IKpoleHelpers_1_R', 'butt_R', False)
r.parent_bone(rig, 'IKpoleHelpers_2_R', 'butt_R', False)
r.parent_bone(rig, 'IKpoleHelpers_3_R', 'footIK_R', False)

# 55-58
r.copy_transforms(rig, 'IKpoleHelpers_2_L', 1.0, 'IKpoleHelpers_1_L')
r.copy_transforms(rig, 'IKpoleHelpers_2_L', 0.5, 'IKpoleHelpers_3_L')
r.damped_track(rig, 'IKpoleHelpers_2_L', subtarget='IKpoleHelpers_3_L', track_axis='TRACK_Y')
# parent_bone(rig, 'kneePole_L', 'IKpoleHelpers_2_L', False)

r.copy_transforms(rig, 'IKpoleHelpers_2_R', 1.0, 'IKpoleHelpers_1_R')
r.copy_transforms(rig, 'IKpoleHelpers_2_R', 0.5, 'IKpoleHelpers_3_R')
r.damped_track(rig, 'IKpoleHelpers_2_R', subtarget='IKpoleHelpers_3_R', track_axis='TRACK_Y')
# parent_bone(rig, 'kneePole_R', 'IKpoleHelpers_2_R', False)

# 59-66
pos_1, pos_2 = r.bone_global_locations(rig, 'tibia_L')
roll = (r.bone_roll(rig, 'tibia_L') + 0.383972)
r.new_bone_creation(pos_1, pos_2, 'kneeBendDeform_L', rig, 'tibia_L', False, roll)
r.flip_bone(rig, 'kneeBendDeform_L')
r.parent_bone(rig, 'kneeBendDeform_L', 'tibia_L', False)
r.transformation(
    rig,
    "kneeBendDeform_L",
    from_max_z_rot=r.degree_to_radians(160),
    map_from="ROTATION",
    map_to="ROTATION",
    subtarget="tibia_L",
    target=rig,
    to_max_z_rot=r.degree_to_radians(8),
    owner_space="LOCAL",
    target_space="LOCAL",
)

pos_1, pos_2 = r.bone_global_locations(rig, 'femur_L')
roll = r.bone_roll(rig, 'femur_L')
r.new_bone_creation(pos_1, pos_2, 'femurDeform_L', rig, 'femur_L', False, roll)
r.flip_bone(rig, 'femurDeform_L')
r.parent_bone(rig, 'femurDeform_L', 'femur_L', False)
r.transformation(
    rig,
    "femurDeform_L",
    from_min_z_rot=r.degree_to_radians(-160),
    from_max_z_rot=0,
    map_from="ROTATION",
    map_to="ROTATION",
    subtarget="femur_L",
    target=rig,
    to_min_z_rot=r.degree_to_radians(-8),
    to_max_z_rot=0,
    owner_space="LOCAL",
    target_space="LOCAL",
)

pos_1, pos_2 = r.bone_global_locations(rig, 'tibia_R')
roll = (r.bone_roll(rig, 'tibia_R') - 0.383972)
r.new_bone_creation(pos_1, pos_2, 'kneeBendDeform_R', rig, 'tibia_R', False, roll)
r.flip_bone(rig, 'kneeBendDeform_R')
r.parent_bone(rig, 'kneeBendDeform_R', 'tibia_R', False)
r.transformation(
    rig,
    "kneeBendDeform_R",
    from_min_z_rot=r.degree_to_radians(-160),
    map_from="ROTATION",
    map_to="ROTATION",
    subtarget="tibia_R",
    target=rig,
    to_min_z_rot=r.degree_to_radians(-8),
    owner_space="LOCAL",
    target_space="LOCAL",
)
## fix roll
pos_1, pos_2 = r.bone_global_locations(rig, 'femur_R')
roll = r.bone_roll(rig, 'femur_R')
r.new_bone_creation(pos_1, pos_2, 'femurDeform_R', rig, 'femur_R', False, roll)
r.flip_bone(rig, 'femurDeform_R')
r.parent_bone(rig, 'femurDeform_R', 'femur_R', False)
r.transformation(
    rig,
    "femurDeform_R",
    from_max_z_rot=r.degree_to_radians(160),
    map_from="ROTATION",
    map_to="ROTATION",
    subtarget="femur_R",
    target=rig,
    to_max_z_rot=r.degree_to_radians(8),
    owner_space="LOCAL",
    target_space="LOCAL",
)

r.parent_bone(rig, 'kneeBendDeform_L', 'tibia_L', False)
r.parent_bone(rig, 'femurDeform_L', 'femur_L', False)

r.ik_properties(rig, 'tibia_L', lock_ik_x=True, lock_ik_y=True)
r.ik_properties(rig, 'tibia_R', lock_ik_x=True, lock_ik_y=True)

## parent with offset doesn't work for the knee pole for some reason, it'll always try to be in front of the parent
# r.parent_bone(rig, 'kneePole_L', '', False)
# r.parent_bone(rig, 'kneePole_R', '', False)

bone = r.select_bone_as_active_pose(rig, 'kneePole_L')
copy = bone.constraints.new(type='CHILD_OF')
target = bpy.data.objects[rig]
copy.target = target
copy.subtarget = 'IKpoleHelpers_2_L'
copy.use_rotation_x = False
copy.use_rotation_y = False
copy.use_rotation_z = False
copy.use_scale_x = False
copy.use_scale_y = False
copy.use_scale_z = False
copy.set_inverse_pending = True

bone = r.select_bone_as_active_pose(rig, 'kneePole_R')
copy = bone.constraints.new(type='CHILD_OF')
target = bpy.data.objects[rig]
copy.target = target
copy.subtarget = 'IKpoleHelpers_2_R'
copy.use_rotation_x = False
copy.use_rotation_y = False
copy.use_rotation_z = False
copy.use_scale_x = False
copy.use_scale_y = False
copy.use_scale_z = False
copy.set_inverse_pending = True

r.set_mode('OBJECT')
r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()

###### Cleaning ######

rig = 'Female Transfer Rig'

r.set_mode('OBJECT')
r.remove_object_selection()
r.remove_edit_and_arm_selection(rig)

################################
######### SPINE ################

r.duplicate_bone(rig, 'pelvis', 'hipTwist')
r.flip_bone(rig, 'hipTwist')
r.limit_rotation(rig, 'hipTwist', max_x=r.degree_to_radians(25),min_x=r.degree_to_radians(-25),max_y=r.degree_to_radians(15),min_y=r.degree_to_radians(-15),max_z=r.degree_to_radians(10),min_z=r.degree_to_radians(-10),limit_x=True,limit_y=True,limit_z=True,owner_space='LOCAL',target_space='LOCAL')
r.parent_bone(rig, 'hipTwist', 'pelvis', False)
head, dontneed = r.bone_global_locations(rig, 'pelvis')
dontneed, tail = r.bone_global_locations(rig, 'spine_3')
head[1] += .1
tail[1] += .1
r.new_bone_creation(head, tail, 'backCTRL', rig, 'pelvis', False, 0)

r.parent_bone(rig, 'backCTRL', 'pelvis', False)
spines = ['spine_1', 'spine_2', 'spine_3']
for item in spines:
    r.copy_rotation(rig, item, influence=1.0, euler_order='YZX', mix_mode='AFTER', subtarget='backCTRL',use_x=True,use_y=True,use_z=True, target_space='LOCAL', owner_space='LOCAL')
    arm = bpy.data.objects[rig]
    bone = r.select_bone_as_active_pose(rig, item)
    bone.constraints[-1].mix_mode = 'AFTER'
    if item == 'spine_1':
        r.limit_rotation(rig, item, max_x=r.degree_to_radians(35),min_x=r.degree_to_radians(-25),max_y=r.degree_to_radians(15),min_y=r.degree_to_radians(-15),max_z=r.degree_to_radians(15),min_z=r.degree_to_radians(-15),limit_x=True,limit_y=True,limit_z=True,owner_space='LOCAL', target_space='LOCAL')
    if item == 'spine_2':
        r.limit_rotation(rig, item, max_x=r.degree_to_radians(40),min_x=r.degree_to_radians(-25),max_y=r.degree_to_radians(20),min_y=r.degree_to_radians(-20),max_z=r.degree_to_radians(24),min_z=r.degree_to_radians(-24),limit_x=True,limit_y=True,limit_z=True,owner_space='LOCAL', target_space='LOCAL')
    if item == 'spine_3':
        r.limit_rotation(rig, item, max_x=r.degree_to_radians(35),min_x=r.degree_to_radians(-25),max_y=r.degree_to_radians(12),min_y=r.degree_to_radians(-12),max_z=r.degree_to_radians(20),min_z=r.degree_to_radians(-20),limit_x=True,limit_y=True,limit_z=True,owner_space='LOCAL', target_space='LOCAL')

head, unneeded = r.bone_global_locations(rig, 'neck_1')
unneeded, tail = r.bone_global_locations(rig, 'neck_2')

head[1] += .08
tail[1] += .08

r.new_bone_creation(head, tail, 'neckHead', rig, 'spine_3', False, 0)
r.copy_rotation(rig, 'neck_1', influence=1.0, euler_order='YZX', mix_mode='AFTER', subtarget='neckHead', use_x=True, use_y=True, use_z=True, target_space='LOCAL',owner_space='LOCAL')
r.copy_rotation(rig, 'head', influence=1.0, euler_order='YZX', mix_mode='AFTER', subtarget='neckHead', use_x=True, use_y=True, use_z=True, target_space='LOCAL',owner_space='LOCAL')

sys.path.remove(module_dir)
