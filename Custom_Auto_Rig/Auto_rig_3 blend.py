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
r = Rigging_Functions()

rig = 'Female Transfer Rig'

################################
######### ARM ################

pole_location, pole_global_location = r.object_location('elbowPoleEmpty_L')
head = list(set(pole_location))
tail = pole_location
tail[1] += .1
r.new_bone_creation(head, tail, 'elbowPole_L', rig, 'root', False, 0)
head, tail = r.bone_global_locations(rig, 'elbowPole_L')
head[1] += .5
tail[1] += .5
r.move_bone_world_location(rig, 'elbowPole_L', head, tail)

pole_location, pole_global_location = r.object_location('elbowPoleEmpty_R')
head = list(set(pole_location))
tail = pole_location
tail[1] += .1
r.new_bone_creation(head, tail, 'elbowPole_R', rig, 'root', False, 0)
head, tail = r.bone_global_locations(rig, 'elbowPole_R')
head[1] += .5
tail[1] += .5
r.move_bone_world_location(rig, 'elbowPole_R', head, tail)


arm = bpy.data.objects[rig]
upmost_left_fingers = ['thumb_2_L', 'index_2_L', 'middle_2_L', 'ring_2_L', 'pinky_2_L']
upmost_right_fingers = ['thumb_2_R', 'index_2_R', 'middle_2_R', 'ring_2_R', 'pinky_2_R']

r.set_mode('OBJECT')
r.remove_object_selection()
r.remove_edit_and_arm_selection(rig)
rotation_bones = []

for item in upmost_left_fingers:
    arm = bpy.data.armatures[rig]
    bone = arm.edit_bones[item]
    head, tail = r.bone_global_locations(rig, item)
    rotation_bone = f"{item.split('_')[0]+'Rotation_L'}"
    rotation_bones.append(rotation_bone)
    r.new_bone_creation(head, tail, rotation_bone, rig, None, False, bone.roll)
    r.parent_bone(rig, rotation_bone, f"{item.split('_')[0]+'_1_L'}", True)

for index, item in enumerate(rotation_bones):
    arm = bpy.data.armatures[rig]
    roll = arm.edit_bones[upmost_left_fingers[index]].roll
    bone = arm.edit_bones[item]
    bone.roll = -roll

r.set_mode('OBJECT')
r.remove_object_selection()
r.remove_edit_and_arm_selection(rig)
rotation_bones = []

for item in upmost_right_fingers:
    arm = bpy.data.armatures[rig]
    bone = arm.edit_bones[item]
    head, tail = r.bone_global_locations(rig, item)
    rotation_bone = f"{item.split('_')[0]+'Rotation_R'}"
    rotation_bones.append(rotation_bone)
    r.new_bone_creation(head, tail, rotation_bone, rig, None, False, bone.roll)
    r.parent_bone(rig, rotation_bone, f"{item.split('_')[0]+'_1_R'}", True)

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
r.copy_rotation(rig, 'thumb_2_L', influence=1.0, mix_mode='AFTER', subtarget='thumbRotation_L', use_x=True, target_space='LOCAL', owner_space='LOCAL')

for item in left_fingers:
    if '_1_' in item:
        left_fingers.remove(item)

for item in left_fingers:
    if '_2_' in item:
        r.lock_rotation(rig, item, z=True)
    else:
        r.lock_rotation(rig, item, y=True, z=True)

for item in left_fingers:
    if 'Rotation' in item:
        left_fingers.remove(item)
        left_rotation.append(item)

for item in left_fingers:
    if '_4_' in item or 'thumb_3_L' in item:
        sub = item.split('_')[0] + 'Rotation_L'
        r.copy_rotation(rig, item, influence=1.0, mix_mode='AFTER', subtarget=sub, use_x=True, target_space='LOCAL', owner_space='LOCAL')
        bone = r.select_bone_as_active_pose(rig, item)
        bone.constraints[-1].mix_mode = "AFTER"
    else:
        sub = item.split('_')[0] + 'Rotation_L'
        r.copy_rotation(rig, item, influence=1.0, mix_mode='BEFORE', subtarget=sub, use_x=True, target_space='LOCAL', owner_space='LOCAL')
        bone = r.select_bone_as_active_pose(rig, item)
        bone.constraints[-1].mix_mode = "BEFORE"

for item in left_rotation:
    if 'thumb' in item:
        pass
    else:
        r.limit_rotation(rig, item, max_x=r.degree_to_radians(100), limit_x=True, owner_space='LOCAL')

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.object_selection(rig)
r.set_mode('EDIT')
forearm_roll = r.bone_roll(rig, 'forearm_L')

for bone in arm.data.bones:
    if bone.parent is None:
        pass
    elif bone.parent.name == 'hand_R':
        right_fingers.append(bone.name)
        for child_bone in bone.children_recursive:
            right_fingers.append(child_bone.name)

right_fingers.remove('thumb_2_R')
sub = item.split('_')[0] + 'Rotation_R'
r.copy_rotation(rig, 'thumb_2_R', influence=1.0, mix_mode='AFTER', subtarget='thumbRotation_R', use_x=True, target_space='LOCAL', owner_space='LOCAL')

for item in right_fingers:
    if '_1_' in item:
        right_fingers.remove(item)

for item in right_fingers:
    if '_2_' in item:
        r.lock_rotation(rig, item, z=True)
    else:
        r.lock_rotation(rig, item, y=True, z=True)

for item in right_fingers:
    if 'Rotation' in item:
        right_fingers.remove(item)
        right_rotation.append(item)

for item in right_fingers:
    if '_4_' in item or 'thumb_3_R' in item:
        sub = item.split('_')[0] + 'Rotation_R'
        r.copy_rotation(rig, item, influence=1.0, mix_mode='AFTER', subtarget=sub, use_x=True, target_space='LOCAL', owner_space='LOCAL')
        bone = r.select_bone_as_active_pose(rig, item)
        bone.constraints[-1].mix_mode = "AFTER"
    else:
        sub = item.split('_')[0] + 'Rotation_R'
        r.copy_rotation(rig, item, influence=1.0, mix_mode='BEFORE', subtarget=sub, use_x=True, target_space='LOCAL', owner_space='LOCAL')
        bone = r.select_bone_as_active_pose(rig, item)
        bone.constraints[-1].mix_mode = "BEFORE"

for item in right_rotation:
    if 'thumb' in item:
        pass
    else:
        r.limit_rotation(rig, item, max_x=r.degree_to_radians(100), limit_x=True, owner_space='LOCAL')

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.object_selection(rig)
r.set_mode('EDIT')
forearm_roll = r.bone_roll(rig, 'forearm_L')
##
##
##
##

## SUBDIVIDE ##

r.set_mode('OBJECT')
r.remove_object_selection()
r.remove_edit_and_arm_selection(rig)
forearm_roll = r.bone_roll(rig, 'forearm_L')
r.duplicate_bones(rig, 'forearm_L', 'forearm_L.001', 'humerus_L', True, forearm_roll, True)
r.remove_edit_and_arm_selection(rig)
arm = bpy.data.objects[rig]
bone = arm.data.edit_bones['forearm_L']
bone.select = True
bone.select_head = True
bone.select_tail = True
arm.data.edit_bones.active = bone
bpy.ops.armature.subdivide(number_cuts=2)
r.remove_edit_and_arm_selection(rig)
r.renamer(rig, 'forearm_L', 'armTwist_1_L')
r.renamer(rig, 'forearm_L.002', 'armTwist_2_L')
r.renamer(rig, 'forearm_L.003', 'armTwist_3_L')
r.renamer(rig, 'forearm_L.001', 'forearm_L')
r.parent_bone(rig, 'hand_L', 'forearm_L', True)

r.set_mode('OBJECT')
r.remove_object_selection()
r.remove_edit_and_arm_selection(rig)
forearm_roll = r.bone_roll(rig, 'forearm_R')
r.duplicate_bones(rig, 'forearm_R', 'forearm_R.001', 'humerus_R', True, forearm_roll, True)
r.remove_edit_and_arm_selection(rig)
arm = bpy.data.objects[rig]
bone = arm.data.edit_bones['forearm_R']
bone.select = True
bone.select_head = True
bone.select_tail = True
arm.data.edit_bones.active = bone
bpy.ops.armature.subdivide(number_cuts=2)
r.remove_edit_and_arm_selection(rig)
r.renamer(rig, 'forearm_R', 'armTwist_1_R')
r.renamer(rig, 'forearm_R.002', 'armTwist_2_R')
r.renamer(rig, 'forearm_R.003', 'armTwist_3_R')
r.renamer(rig, 'forearm_R.001', 'forearm_R')
r.parent_bone(rig, 'hand_R', 'forearm_R', True)


r.copy_rotation(rig, 'armTwist_1_L',influence=0.3 ,subtarget='armTwist_2_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
r.copy_rotation(rig, 'armTwist_2_L',influence=0.727 ,subtarget='armTwist_3_L', use_x=True, use_y=True, use_z=True, target_space='LOCAL', owner_space='LOCAL')
r.copy_rotation(rig, 'armTwist_3_L',subtarget='hand_L', use_y=True, target_space='LOCAL', owner_space='LOCAL')

at_1_L_head, at_1_L_tail = r.bone_global_locations(rig, 'armTwist_1_L')
at_2_L_head, at_2_L_tail = r.bone_global_locations(rig, 'armTwist_2_L')
at_3_L_head, at_3_L_tail = r.bone_global_locations(rig, 'armTwist_3_L')
at_1_R_head, at_1_R_tail = r.bone_global_locations(rig, 'armTwist_1_R')
at_2_R_head, at_2_R_tail = r.bone_global_locations(rig, 'armTwist_2_R')
at_3_R_head, at_3_R_tail = r.bone_global_locations(rig, 'armTwist_3_R')

location_list = [at_1_L_head, at_1_L_tail, at_2_L_head, at_2_L_tail, at_3_L_head, at_3_L_tail, at_1_R_head, at_1_R_tail, at_2_R_head, at_2_R_tail, at_3_L_head, at_3_L_tail]

# parenting armTwist_3 to the forearm freaking deletes it for some reason.

at_head, at_tail = r.bone_global_locations(rig, 'armTwist_1_L')

r.parent_bone(rig, 'armTwist_1_L', 'forearm_L', False)
r.parent_bone(rig, 'armTwist_2_L', 'forearm_L', False)
r.parent_bone(rig, 'armTwist_1_R', 'forearm_R', False)
r.parent_bone(rig, 'armTwist_2_R', 'forearm_R', False)

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.set_mode('EDIT')
arm = bpy.data.armatures[rig]
bone = arm.edit_bones['armTwist_3_L']
bone.use_connect = False
bone.parent = arm.edit_bones['forearm_L']
r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.set_mode('EDIT')
arm = bpy.data.armatures[rig]
bone = arm.edit_bones['armTwist_3_R']
bone.use_connect = False
bone.parent = arm.edit_bones['forearm_R']


# a_list = ['armTwist_1_L', 'armTwist_2_L', 'armTwist_3_L', 'armTwist_1_R', 'armTwist_2_R', 'armTwist_3_R']
r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.set_mode('EDIT')
head_count = 0
tail_count = 1
arm = bpy.data.armatures[rig]
bone = arm.edit_bones['armTwist_1_L']
# print(bone)
bone.head = at_head
bone.tail = at_tail

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.set_mode('EDIT')
head_count = 0
tail_count = 1
arm = bpy.data.armatures[rig]
bone = arm.edit_bones['armTwist_2_L']
# print(bone)
bone.head = at_2_L_head
bone.tail = at_2_L_tail

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.set_mode('EDIT')
head_count = 0
tail_count = 1
arm = bpy.data.armatures[rig]
bone = arm.edit_bones['armTwist_3_L']
# print(bone)
bone.head = at_3_L_head
bone.tail = at_3_L_tail

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.set_mode('EDIT')
head_count = 0
tail_count = 1
arm = bpy.data.armatures[rig]
bone = arm.edit_bones['armTwist_1_R']
# print(bone)
bone.head = at_1_R_head
bone.tail = at_1_R_tail

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.set_mode('EDIT')
head_count = 0
tail_count = 1
arm = bpy.data.armatures[rig]
bone = arm.edit_bones['armTwist_2_R']
# print(bone)
bone.head = at_2_R_head
bone.tail = at_2_R_tail

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.set_mode('EDIT')
head_count = 0
tail_count = 1
arm = bpy.data.armatures[rig]
bone = arm.edit_bones['armTwist_3_R']
# print(bone)
bone.head = at_3_R_head
bone.tail = at_3_R_tail

#for some reason, it won't select the right bone, so fuck me I guess.

# for item in a_list:
#     # print(item)
#     r.remove_edit_and_arm_selection(rig)
#     r.set_mode('OBJECT')
#     r.remove_object_selection()
#     r.object_selection(rig)
#     r.set_mode('EDIT')
#     arm = bpy.data.armatures[rig]
#     r.select_bone_as_active_edit(rig, item)
#     bone = arm.edit_bones[item]
#     print(bone.name)
#     if bone.name != item:
#         while bone.name != item:
#             for bone_name in bpy.context.active_object.data.edit_bones[:]:
#                 print(bone_name.name)
#                 if bone_name.name == item:
#                     bone = arm.edit_bones[bone_name.name]

#     print(bone.name)
#     the_head = location_list[head_count]
#     the_tail = location_list[head_count + 1]
#     at_head, at_tail = r.bone_global_locations(rig, bone.name)
#     print(at_head)
#     print(at_tail)
#     bone.head = at_head
#     bone.tail = at_tail
#     print(head_count)
#     head_count += 2

##### IK ####

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
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
        left_arm_IK_bones[index] = f"{item.split('_')[0]}_IK_L"
    else:
        if any(bone in item for bone in number):
            left_arm_IK_bones[index] = f"{item.split('_', 2)[0]}_{(item.split('_', 1)[1])[:-1]}IK_L"
        else:
            left_arm_IK_bones[index] = f"{item.split('_', 2)[0]}_IK_L"

for index, item in enumerate(left_arm_FK_bones):
    if 'hand' in item:
        left_arm_FK_bones[index] = f"{item.split('_')[0]}_FK_L"
    else:
        if any(bone in item for bone in number):
            left_arm_FK_bones[index] = f"{item.split('_', 2)[0]}_{(item.split('_', 1)[1])[:-1]}FK_L"
        else:
            left_arm_FK_bones[index] = f"{item.split('_', 2)[0]}_FK_L"

for index, item in enumerate(right_arm_IK_bones):
    if 'hand' in item:
        right_arm_IK_bones[index] = f"{item.split('_')[0]}_IK_R"
    else:
        if any(bone in item for bone in number):
            right_arm_IK_bones[index] = f"{item.split('_', 2)[0]}_{(item.split('_', 1)[1])[:-1]}IK_R"
        else:
            right_arm_IK_bones[index] = f"{item.split('_', 2)[0]}_IK_R"

for index, item in enumerate(right_arm_FK_bones):
    if 'hand' in item:
        right_arm_FK_bones[index] = f"{item.split('_')[0]}_FK_R"
    else:
        if any(bone in item for bone in number):
            right_arm_FK_bones[index] = f"{item.split('_', 2)[0]}_{(item.split('_', 1)[1])[:-1]}FK_R"
        else:
            right_arm_FK_bones[index] = f"{item.split('_', 2)[0]}_FK_R"

##### uncomment above

# for index, item in enumerate(left_arm_FK_bones):
#     left_arm_FK_bones[index] = f"{item.split('_')[0]}_FK_L"

# for index, item in enumerate(right_arm_FK_bones):
#     if 'hand' in item:
#         right_arm_IK_bones[index] = f"{item.split('_')[0]}IK_CTRL_R"
#     else:
#         right_arm_IK_bones[index] = f"{item.split('_')[0]}_IK_R"

# for index, item in enumerate(right_arm_FK_bones):
#     right_arm_FK_bones[index] = f"{item.split('_')[0]}_FK_R"

###### uncomment below
r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.object_selection(rig)
r.set_mode('EDIT')


for index, item in enumerate(left_arm_bones):
    forearm_roll = r.bone_roll(rig, left_arm_bones[index])
    arm = bpy.data.objects[rig]
    parent = arm.data.bones[item].parent.name
    r.duplicate_bones(rig, item, left_arm_IK_bones[index], parent, False, forearm_roll, False)
hand_ctrl_length = r.bone_length('hand_IK_L', rig) * 2
r.change_bone_length('hand_IK_L', rig, hand_ctrl_length)



for index, item in enumerate(left_arm_bones):
    forearm_roll = r.bone_roll(rig, left_arm_bones[index])
    arm = bpy.data.objects[rig]
    parent = arm.data.bones[item].parent.name
    r.duplicate_bones(rig, item, left_arm_FK_bones[index], parent, False, forearm_roll, False)

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.object_selection(rig)
r.set_mode('EDIT')

for index, item in enumerate(right_arm_bones):
    forearm_roll = r.bone_roll(rig, right_arm_bones[index])
    arm = bpy.data.objects[rig]
    parent = arm.data.bones[item].parent.name
    r.duplicate_bones(rig, item, right_arm_IK_bones[index], parent, False, forearm_roll, False)
hand_ctrl_length = r.bone_length('hand_IK_R', rig) * 2
r.change_bone_length('hand_IK_R', rig, hand_ctrl_length)

for index, item in enumerate(right_arm_bones):
    forearm_roll = r.bone_roll(rig, right_arm_bones[index])
    arm = bpy.data.objects[rig]
    parent = arm.data.bones[item].parent.name
    r.duplicate_bones(rig, item, right_arm_FK_bones[index], parent, False, forearm_roll, False)

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()

# r.copy_rotation(rig, 'hand_L', subtarget='hand_IK_L')
# r.copy_rotation(rig, 'hand_R', subtarget='hand_IK_R')

r.parent_bone(rig, 'forearm_IK_L', 'humerus_IK_L', True)
r.parent_bone(rig, 'forearm_IK_R', 'humerus_IK_R', True)
r.parent_bone(rig, 'forearm_FK_L', 'humerus_FK_L', True)
r.parent_bone(rig, 'forearm_FK_R', 'humerus_FK_R', True)


r.create_IK(rig, 'forearm_IK_L', 2, r.degree_to_radians(-80), 'elbowPole_L', rig, 'hand_IK_L', rig)
r.create_IK(rig, 'forearm_IK_R', 2, r.degree_to_radians(-80), 'elbowPole_R', rig, 'hand_IK_R', rig)


# print(left_arm_bones)
# print(left_arm_FK_bones)
# print(left_arm_IK_bones)
# print(right_arm_bones)
# print(right_arm_FK_bones)
# print(right_arm_IK_bones)

sys.path.remove(module_dir)
