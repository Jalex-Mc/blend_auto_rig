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


rig = 'Female Transfer Rig'

################################
######### ARM ################

pole_location, pole_global_location = object_location('elbowPoleEmpty_L')
head = list(set(pole_location))
tail = pole_location
tail[1] += .1
new_bone_creation(head, tail, 'elbowPole_L', rig, 'ROOT', False, 0)
head, tail = bone_global_locations(rig, 'elbowPole_L')
head[1] += .16
tail[1] += .16
move_bone_world_location(rig, 'elbowPole_L', head, tail)

pole_location, pole_global_location = object_location('elbowPoleEmpty_R')
head = list(set(pole_location))
tail = pole_location
tail[1] += .1
new_bone_creation(head, tail, 'elbowPole_R', rig, 'ROOT', False, 0)
head, tail = bone_global_locations(rig, 'elbowPole_R')
head[1] += .16
tail[1] += .16
move_bone_world_location(rig, 'elbowPole_R', head, tail)


arm = bpy.data.objects[rig]
upmost_left_fingers = ['thumb_2_L', 'index_2_L', 'middle_2_L', 'ring_2_L', 'pinky_2_L']
upmost_right_fingers = ['thumb_2_R', 'index_2_R', 'middle_2_R', 'ring_2_R', 'pinky_2_R']

set_mode('OBJECT')
remove_object_selection()
remove_edit_and_arm_selection(rig)
rotation_bones = []

for item in upmost_left_fingers:
    arm = bpy.data.armatures[rig]
    bone = arm.edit_bones[item]
    head, tail = bone_global_locations(rig, item)
    rotation_bone = f"{item.split('_')[0]+'Rotation_L'}"
    rotation_bones.append(rotation_bone)
    new_bone_creation(head, tail, rotation_bone, rig, None, False, bone.roll)
    parent_bone(rig, rotation_bone, f"{item.split('_')[0]+'_1_L'}", True)

for index, item in enumerate(rotation_bones):
    arm = bpy.data.armatures[rig]
    roll = arm.edit_bones[upmost_left_fingers[index]].roll
    bone = arm.edit_bones[item]
    bone.roll = -roll

set_mode('OBJECT')
remove_object_selection()
remove_edit_and_arm_selection(rig)
rotation_bones = []

for item in upmost_right_fingers:
    arm = bpy.data.armatures[rig]
    bone = arm.edit_bones[item]
    head, tail = bone_global_locations(rig, item)
    rotation_bone = f"{item.split('_')[0]+'Rotation_R'}"
    rotation_bones.append(rotation_bone)
    new_bone_creation(head, tail, rotation_bone, rig, None, False, bone.roll)
    parent_bone(rig, rotation_bone, f"{item.split('_')[0]+'_1_R'}", True)

for index, item in enumerate(rotation_bones):
    arm = bpy.data.armatures[rig]
    roll = arm.edit_bones[upmost_left_fingers[index]].roll
    bone = arm.edit_bones[item]
    bone.roll = -roll

arm = bpy.data.objects[rig]
left_fingers = []
right_fingers = []
left_rotation = []
right_rotation = []
for bone in arm.data.bones:
    if bone.parent is None:
        pass
    elif bone.parent.name == 'hand_L':
        left_fingers.append(bone.name)
        for child_bone in bone.children_recursive:
            left_fingers.append(child_bone.name)

left_fingers.remove('thumb_2_L')
sub = item.split('_')[0] + 'Rotation_L'
copy_rotation(rig, 'thumb_2_L', influence=1.0, mix_mode='AFTER', subtarget=sub, use_x=True, target_space='LOCAL', owner_space='LOCAL')

for item in left_fingers:
    if '_1_' in item:
        left_fingers.remove(item)

for item in left_fingers:
    if '_2_' in item:
        lock_rotation(rig, item, z=True)
    else:
        lock_rotation(rig, item, y=True, z=True)

for item in left_fingers:
    if 'Rotation' in item:
        left_fingers.remove(item)
        left_rotation.append(item)

for item in left_fingers:
    if '_4_' in item or 'thumb_3_L' in item:
        sub = item.split('_')[0] + 'Rotation_L'
        copy_rotation(rig, item, influence=1.0, mix_mode='AFTER', subtarget=sub, use_x=True, target_space='LOCAL', owner_space='LOCAL')
        bone = select_bone_as_active_pose(rig, item)
        bone.constraints[-1].mix_mode = "AFTER"
    else:
        sub = item.split('_')[0] + 'Rotation_L'
        copy_rotation(rig, item, influence=1.0, mix_mode='BEFORE', subtarget=sub, use_x=True, target_space='LOCAL', owner_space='LOCAL')
        bone = select_bone_as_active_pose(rig, item)
        bone.constraints[-1].mix_mode = "BEFORE"

for item in left_rotation:
    if 'thumb' in item:
        pass
    else:
        limit_rotation(rig, item, max_x=degree_to_radians(85), limit_x=True, owner_space='LOCAL')

remove_edit_and_arm_selection(rig)
set_mode('OBJECT')
remove_object_selection()
object_selection(rig)
set_mode('EDIT')
forearm_roll = bone_roll(rig, 'forearm_L')
##
##
##
##

## SUBDIVIDE ##
set_mode('OBJECT')
remove_object_selection()
remove_edit_and_arm_selection(rig)
forearm_roll = bone_roll(rig, 'forearm_L')
duplicate_bones(rig, 'forearm_L', 'forearm_L.001', 'humerus_L', True, forearm_roll, True)
remove_edit_and_arm_selection(rig)
arm = bpy.data.objects[rig]
bone = arm.data.edit_bones['forearm_L']
bone.select = True
bone.select_head = True
bone.select_tail = True
arm.data.edit_bones.active = bone
bpy.ops.armature.subdivide(number_cuts=2)
remove_edit_and_arm_selection(rig)
renamer(rig, 'forearm_L', 'armTwist_1_L')
renamer(rig, 'forearm_L.003', 'armTwist_2_L')
renamer(rig, 'forearm_L.002', 'armTwist_3_L')
renamer(rig, 'forearm_L.001', 'forearm_L')

set_mode('OBJECT')
remove_object_selection()
remove_edit_and_arm_selection(rig)
forearm_roll = bone_roll(rig, 'forearm_R')
duplicate_bones(rig, 'forearm_R', 'forearm_R.001', 'humerus_R', True, forearm_roll, True)
remove_edit_and_arm_selection(rig)
arm = bpy.data.objects[rig]
bone = arm.data.edit_bones['forearm_R']
bone.select = True
bone.select_head = True
bone.select_tail = True
arm.data.edit_bones.active = bone
bpy.ops.armature.subdivide(number_cuts=2)
remove_edit_and_arm_selection(rig)
renamer(rig, 'forearm_R', 'armTwist_1_R')
renamer(rig, 'forearm_R.003', 'armTwist_2_R')
renamer(rig, 'forearm_R.002', 'armTwist_3_R')
renamer(rig, 'forearm_R.001', 'forearm_R')

copy_rotation(rig, 'armTwist_1_L',influence=0.3 ,subtarget='armTwist_2_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
copy_rotation(rig, 'armTwist_2_L',influence=0.727 ,subtarget='armTwist_3_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
copy_rotation(rig, 'armTwist_3_L',subtarget='hand_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')



##### IK ####

remove_edit_and_arm_selection(rig)
set_mode('OBJECT')
remove_object_selection()
left_arm_bones = []
right_arm_bones = []
arm = bpy.data.objects[rig]
left_arm_IK_bones = []
left_arm_FK_bones = []
right_arm_IK_bones = []
right_arm_FK_bones = []

for bone in arm.data.bones:
    if bone.parent is None:
        pass
    elif bone.parent.name == 'clavicle_L':
        left_arm_bones.append(bone.name)

        for child_bone in bone.children_recursive:
            if "thumb" in child_bone.name:
                pass
            elif "index" in child_bone.name:
                pass
            elif "middle" in child_bone.name:
                pass
            elif "ring" in child_bone.name:
                pass
            elif "pinky" in child_bone.name:
                pass
            else:
                left_arm_bones.append(child_bone.name)

for bone in arm.data.bones:
    if bone.parent is None:
        pass
    elif bone.parent.name == 'clavicle_R':
        right_arm_bones.append(bone.name)

        for child_bone in bone.children_recursive:
            if "thumb" in child_bone.name:
                pass
            elif "index" in child_bone.name:
                pass
            elif "middle" in child_bone.name:
                pass
            elif "ring" in child_bone.name:
                pass
            elif "pinky" in child_bone.name:
                pass
            else:
                right_arm_bones.append(child_bone.name)

for item in left_arm_bones:
    left_arm_IK_bones.append(item)
    left_arm_FK_bones.append(item)

for item in right_arm_bones:
    right_arm_IK_bones.append(item)
    right_arm_FK_bones.append(item)

number = ['1', '2', '3']

for index, item in enumerate(left_arm_IK_bones):
    if 'hand' in item:
        left_arm_IK_bones[index] = f"{item.split('_')[0]}IK_CTRL_L"
    else:
        if any(bone in item for bone in number):
            left_arm_IK_bones[index] = f"{item.split('_', 2)[0]}_{(item.split('_', 1)[1])[:-1]}IK_L"
        else:
            left_arm_IK_bones[index] = f"{item.split('_', 2)[0]}_IK_L"

for index, item in enumerate(left_arm_FK_bones):
    if 'hand' in item:
        left_arm_FK_bones[index] = f"{item.split('_')[0]}FK_L"
    else:
        if any(bone in item for bone in number):
            left_arm_FK_bones[index] = f"{item.split('_', 2)[0]}_{(item.split('_', 1)[1])[:-1]}FK_L"
        else:
            left_arm_FK_bones[index] = f"{item.split('_', 2)[0]}_FK_L"

for index, item in enumerate(right_arm_IK_bones):
    if 'hand' in item:
        right_arm_IK_bones[index] = f"{item.split('_')[0]}IK_CTRL_R"
    else:
        if any(bone in item for bone in number):
            right_arm_IK_bones[index] = f"{item.split('_', 2)[0]}_{(item.split('_', 1)[1])[:-1]}IK_R"
        else:
            right_arm_IK_bones[index] = f"{item.split('_', 2)[0]}_IK_R"

for index, item in enumerate(right_arm_FK_bones):
    if 'hand' in item:
        right_arm_FK_bones[index] = f"{item.split('_')[0]}FK_R"
    else:
        if any(bone in item for bone in number):
            right_arm_FK_bones[index] = f"{item.split('_', 2)[0]}_{(item.split('_', 1)[1])[:-1]}FK_R"
        else:
            right_arm_FK_bones[index] = f"{item.split('_', 2)[0]}_FK_R"
# for index, item in enumerate(left_arm_FK_bones):
#     left_arm_FK_bones[index] = f"{item.split('_')[0]}_FK_L"

# for index, item in enumerate(right_arm_FK_bones):
#     if 'hand' in item:
#         right_arm_IK_bones[index] = f"{item.split('_')[0]}IK_CTRL_R"
#     else:
#         right_arm_IK_bones[index] = f"{item.split('_')[0]}_IK_R"

# for index, item in enumerate(right_arm_FK_bones):
#     right_arm_FK_bones[index] = f"{item.split('_')[0]}_FK_R"


remove_edit_and_arm_selection(rig)
set_mode('OBJECT')
remove_object_selection()
object_selection(rig)
set_mode('EDIT')


for index, item in enumerate(left_arm_bones):
    forearm_roll = bone_roll(rig, left_arm_bones[index])
    arm = bpy.data.objects[rig]
    parent = arm.data.bones[item].parent.name
    duplicate_bones(rig, item, left_arm_IK_bones[index], parent, False, forearm_roll, False)
hand_ctrl_length = bone_length('handIK_CTRL_L', rig) * 2
change_bone_length('handIK_CTRL_L', rig, hand_ctrl_length)

for index, item in enumerate(left_arm_bones):
    forearm_roll = bone_roll(rig, left_arm_bones[index])
    arm = bpy.data.objects[rig]
    parent = arm.data.bones[item].parent.name
    duplicate_bones(rig, item, left_arm_FK_bones[index], parent, False, forearm_roll, False)

remove_edit_and_arm_selection(rig)
set_mode('OBJECT')
remove_object_selection()
object_selection(rig)
set_mode('EDIT')

for index, item in enumerate(right_arm_bones):
    forearm_roll = bone_roll(rig, right_arm_bones[index])
    arm = bpy.data.objects[rig]
    parent = arm.data.bones[item].parent.name
    duplicate_bones(rig, item, right_arm_IK_bones[index], parent, False, forearm_roll, False)
hand_ctrl_length = bone_length('handIK_CTRL_R', rig) * 2
change_bone_length('handIK_CTRL_R', rig, hand_ctrl_length)

for index, item in enumerate(right_arm_bones):
    forearm_roll = bone_roll(rig, right_arm_bones[index])
    arm = bpy.data.objects[rig]
    parent = arm.data.bones[item].parent.name
    duplicate_bones(rig, item, right_arm_FK_bones[index], parent, False, forearm_roll, False)

remove_edit_and_arm_selection(rig)
set_mode('OBJECT')
remove_object_selection()

copy_rotation(rig, 'hand_L', subtarget='handIK_CTRL_L')
copy_rotation(rig, 'hand_R', subtarget='handIK_CTRL_R')

parent_bone(rig, 'armTwist_1_L', 'forearm_L', False)
# parent_bone(rig, 'armTwist_2_L', 'forearm_L', False)
# parent_bone(rig, 'armTwist_3_L', 'forearm_L', False)
# parent_bone(rig, 'armTwist_1_FK_L', 'forearm_FK_L', False)
# parent_bone(rig, 'armTwist_2_FK_L', 'forearm_FK_L', False)
# parent_bone(rig, 'armTwist_3_FK_L', 'forearm_FK_L', False)
# parent_bone(rig, 'armTwist_1_IK_L', 'forearm_IK_L', False)
# parent_bone(rig, 'armTwist_2_IK_L', 'forearm_IK_L', False)
# parent_bone(rig, 'armTwist_3_IK_L', 'forearm_IK_L', False)

create_IK(rig, 'forearm_IK_L', 2, degree_to_radians(-80), 'elbowPole_L', rig, 'handIK_CTRL_L', rig)
create_IK(rig, 'forearm_IK_R', 2, degree_to_radians(-80), 'elbowPole_R', rig, 'handIK_CTRL_R', rig)


print(left_arm_bones)
print(left_arm_FK_bones)
print(left_arm_IK_bones)
print(right_arm_bones)
print(right_arm_FK_bones)
print(right_arm_IK_bones)

sys.path.remove(module_dir)
