import bpy
from mathutils import Vector
import math
import os
import sys

'''Run each script one after another, running the CTRLs script after Auto_rig_6
    On script 1(this one), once run, fix IK angle on the leg IK,
    On script 3, once run, fix the IK angle of the arms. 
    When rotating the ange, center it on the pole location in the front Orthographic view
'''

# Adds the directory containing your module to the Python path (before importing it). Removed on the last line of every script
module_dir = os.path.abspath('O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig')
sys.path.insert(0, module_dir)

# Now you can import your module as usual
from rig_func import Rigging_Functions

# initialize the Class
r = Rigging_Functions()

rig = 'Female Transfer Rig'

a_rig = bpy.data.objects[rig]

a_rig['rig_id'] = "universal rig"

# inspect.getfullargspec(r.set_mode)

# Makes sure the scene's orientation transformation is set to Global
bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'

r.set_mode('OBJECT')
r.remove_object_selection()
r.remove_edit_and_arm_selection(rig)

r.create_root_bone(rig) #4
r.parent_bone(rig, 'pelvis', 'root', False)

##################################
##################################
### TOES

r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.object_selection(rig)
r.set_mode('EDIT')
toe_rotation_to_duplicate = ['bigToe_1_L', 'bigToe_1_R', 'indexToe_1_L', 'indexToe_1_R', 
                             'midToe_1_L', 'midToe_1_R', 'ringToe_1_L', 'ringToe_1_R', 'pinkyToe_1_L', 'pinkyToe_1_R']
arm = bpy.data.objects[rig]
left_toes = []
right_toes = []
for bone in arm.data.bones:
    if bone.parent is None:
        pass
    elif bone.parent.name == 'toes_L' and bone.parent.name not in left_toes:
        left_toes.append(bone.name)
        for child_bone in bone.children_recursive:
            left_toes.append(child_bone.name)

for bone in arm.data.bones:
    if bone.parent is None:
        pass
    elif bone.parent.name == 'toes_R' and bone.parent.name not in right_toes:
        right_toes.append(bone.name)
        for child_bone in bone.children_recursive:
            right_toes.append(child_bone.name)


for item in toe_rotation_to_duplicate:
    if item[-1] == 'L':
        new_name = item[:-3] + 'Rotation_L'
        l_pos_1, l_pos_2 = r.bone_global_locations(rig, item)
        the_roll = r.bone_roll(rig, item)
        r.new_bone_creation(l_pos_1, l_pos_2, new_name, rig, 'toes_L', False, the_roll)
        r.renamer(rig, new_name, new_name.replace('_', '', 1))
    else:
        new_name = item[:-3] + 'Rotation_R'
        r_pos_1, r_pos_2 = r.bone_global_locations(rig, item)
        the_roll = r.bone_roll(rig, item)
        r.new_bone_creation(r_pos_1, r_pos_2, new_name, rig, 'toes_R', False, the_roll)
        r.renamer(rig, new_name, new_name.replace('_', '', 1))

close_toes_L = ['bigToe_1_L', 'indexToe_1_L', 'ringToe_1_L', 'pinkyToe_1_L', 'midToe_1_L']        
for item in close_toes_L:
    r.lock_rotation(rig, item, y=True)
    r.lock_rotation(rig, (item[:-4] + 'Rotation_L'), y=True, z=True)
    r.copy_rotation(rig, item, subtarget=(item[:-4] + 'Rotation_L'),use_x=True, target_space='LOCAL', owner_space='LOCAL' )
close_toes_R =  ['bigToe_1_R', 'indexToe_1_R', 'ringToe_1_R', 'pinkyToe_1_R', 'midToe_1_R']
for item in close_toes_R:
    r.lock_rotation(rig, item, y=True)
    r.lock_rotation(rig, (item[:-4] + 'Rotation_R'), y=True, z=True)
    r.copy_rotation(rig, item, subtarget=(item[:-4] + 'Rotation_R'),use_x=True, target_space='LOCAL', owner_space='LOCAL')

left_rest_toes = list(set(left_toes) - set(close_toes_L))
right_rest_toes = list(set(right_toes) - set(close_toes_R))

for item in left_rest_toes:
    r.lock_rotation(rig, item, y=True, z=True)
    r.copy_rotation(rig, item, mix_mode='AFTER', subtarget=(item[:-4] + 'Rotation_L'), use_x=True, target_space='LOCAL', owner_space='LOCAL')

for item in right_rest_toes:
    r.lock_rotation(rig, item, y=True, z=True)
    r.copy_rotation(rig, item, mix_mode='AFTER', subtarget=(item[:-4] + 'Rotation_R'), use_x=True, target_space='LOCAL', owner_space='LOCAL')

r.set_mode('OBJECT')
r.remove_edit_and_arm_selection(rig)
r.set_mode('OBJECT')
r.remove_object_selection()
r.object_selection(rig)
mix_mode_fix = left_rest_toes + right_rest_toes
for item in mix_mode_fix:
    arm = bpy.data.objects[rig]
    bone = r.select_bone_as_active_pose(rig, item)
    bone.constraints[-1].mix_mode = 'AFTER'

##################################
##################################
### LEG AND FOOT


# 1-2 footFK and toesIK
r.remove_edit_and_arm_selection(rig)
r.duplicate_bones(rig, 'footFK_L', 'MCH_foot_L', False, False, r.bone_roll(rig, 'footFK_L'), keep_selection=False)
r.duplicate_bones(rig, 'toes_L', 'toesIK_L', False, False, r.bone_roll(rig, 'toes_L'), keep_selection=False)
r.duplicate_bones(rig, 'footFK_R', 'MCH_foot_R', False, False, r.bone_roll(rig, 'footFK_R'), keep_selection=False)
r.duplicate_bones(rig, 'toes_R', 'toesIK_R', False, False, r.bone_roll(rig, 'toes_L'), keep_selection=False)


# 3-4
left_foot_tip_empty_location, left_foot_tip_empty_world = r.object_location('footTip_Empty_L')
left_foot_end_empty_location, left_foot_end_empty_world = r.object_location('footEnd_Empty_L')
left_Knee_empty_location, left_Knee_empty_world = r.object_location('knee_Empty_L')
right_foot_tip_empty_location, right_foot_tip_empty_world = r.object_location('footTip_Empty_R')
right_foot_end_empty_location, right_foot_end_empty_world = r.object_location('footEnd_Empty_R')
right_Knee_empty_location, right_Knee_empty_world = r.object_location('knee_Empty_R')

r.new_bone_creation(left_foot_tip_empty_location, left_foot_end_empty_location, 'footIK_L', rig, 'root', False, 1.5708)
r.new_bone_creation(right_foot_tip_empty_location, right_foot_end_empty_location, 'footIK_R', rig, 'root', False, 1.5708)


# 5 - 6
r.extrude_out('MCH_foot_L', 'footRollCTRL_L', rig, True, False, (0, 0.1, 0), 0.038292, 0)
r.parent_bone(rig, 'footRollCTRL_L', 'footIK_L', False)
r.extrude_out('MCH_foot_R', 'footRollCTRL_R', rig, True, False, (0, 0.1, 0), 0.038292, 0)
r.parent_bone(rig, 'footRollCTRL_R', 'footIK_R', False)

# 7 - 8
pos_1, pos_2 = r.bone_global_locations(rig, 'MCH_foot_L')
r.new_bone_creation(pos_2, left_foot_end_empty_location, 'MCH_footRoll_1_L', rig, 'root', False, 0)
position_0 = left_foot_end_empty_location[0]
position_1 = left_foot_end_empty_location[1]
r.move_head_or_tail('MCH_footRoll_1_L', rig, False, True, 0, (position_0, position_1, pos_2[2]))

pos_1, pos_2 = r.bone_global_locations(rig, 'MCH_foot_R')
r.new_bone_creation(pos_2, right_foot_end_empty_location, 'MCH_footRoll_1_R', rig, 'root', False, 0)
position_0 = right_foot_end_empty_location[0]
position_1 = right_foot_end_empty_location[1]
r.move_head_or_tail('MCH_footRoll_1_R', rig, False, True, 0, (position_0, position_1, pos_2[2]))

left_change = r.bone_length('MCH_footRoll_1_L', rig)
right_change = r.bone_length('MCH_footRoll_1_R', rig)
r.change_bone_length('MCH_footRoll_1_L', rig, (left_change / 4))
r.change_bone_length('MCH_footRoll_1_R', rig, (right_change / 4))

# 9-10
r.parent_bone(rig, 'MCH_foot_L', 'MCH_footRoll_1_L', False)
r.parent_bone(rig, 'MCH_foot_R', 'MCH_footRoll_1_R', False)
r.parent_bone(rig, 'MCH_footRoll_1_L', 'footIK_L', False)
r.parent_bone(rig, 'MCH_footRoll_1_R', 'footIK_R', False)

# 11-13
r.eular_change(rig, 'footRollCTRL_R', 'XYZ')
r.eular_change(rig, 'footRollCTRL_L', 'XYZ')
r.lock_location(rig, 'footRollCTRL_R', x=True, y=True, z=True)
r.lock_location(rig, 'footRollCTRL_L', x=True, y=True, z=True)
r.lock_scale(rig, 'footRollCTRL_R', x=True, y=True, z=True)
r.lock_scale(rig, 'footRollCTRL_L', x=True, y=True, z=True)
r.lock_rotation(rig, 'footRollCTRL_R', z=True)
r.lock_rotation(rig, 'footRollCTRL_L', z=True)

# 14-15
r.copy_rotation(rig, 'MCH_footRoll_1_L',subtarget='footRollCTRL_L', use_x=True, target_space='LOCAL', owner_space='LOCAL')
r.copy_rotation(rig, 'MCH_footRoll_1_R',subtarget='footRollCTRL_R', use_x=True, target_space='LOCAL', owner_space='LOCAL')
r.limit_rotation(rig, 'MCH_footRoll_1_L', max_x=r.degree_to_radians(170), limit_x=True, target_space='LOCAL', owner_space='LOCAL')
r.limit_rotation(rig, 'MCH_footRoll_1_R', max_x=r.degree_to_radians(170), limit_x=True, target_space='LOCAL', owner_space='LOCAL')

# 16-21
start_point, global_pos, end_point, global_alt = r.object_location('footEnd_Empty_L', y=0.042891, alter=True)
r.new_bone_creation(start_point, end_point, 'heelPosition_L', rig, 'root', False, 0)
start_point, global_pos, end_point, global_alt = r.object_location('footEnd_Empty_R', y=0.042891, alter=True)
r.new_bone_creation(start_point, end_point, 'heelPosition_R', rig, 'root', False, 0)

r.copy_rotation(rig, 'heelPosition_L',subtarget='footRollCTRL_L', use_x=True, target_space='LOCAL', owner_space='LOCAL')
r.copy_rotation(rig, 'heelPosition_R',subtarget='footRollCTRL_R', use_x=True, target_space='LOCAL', owner_space='LOCAL')
r.limit_rotation(rig, 'heelPosition_L', min_x=r.degree_to_radians(-170), limit_x=True, target_space='LOCAL', owner_space='LOCAL')
r.limit_rotation(rig, 'heelPosition_R', min_x=r.degree_to_radians(-170), limit_x=True, target_space='LOCAL', owner_space='LOCAL')

r.parent_bone(rig, 'MCH_footRoll_1_L', 'heelPosition_L', False)
r.parent_bone(rig, 'MCH_footRoll_1_R', 'heelPosition_R', False)
r.parent_bone(rig, 'toesIK_L', 'heelPosition_L', False)
r.parent_bone(rig, 'toesIK_R', 'heelPosition_R', False)

# 22-27
pos_1, pos_2 = r.bone_global_locations(rig, 'heelPosition_R')
pos_1[0] -= 0.03
pos_2[0] -= 0.03
r.new_bone_creation(pos_1, pos_2, 'MCH_footRoll_3_R', rig, 'footIK_R', False, 0)
pos_1, pos_2 = r.bone_global_locations(rig, 'heelPosition_R')
pos_1[0] += 0.03
pos_2[0] += 0.03
r.new_bone_creation(pos_1, pos_2, 'MCH_footRoll_2_R', rig, 'MCH_footRoll_3_R', False, 0)

pos_1, pos_2 = r.bone_global_locations(rig, 'heelPosition_L')
pos_1[0] += 0.03
pos_2[0] += 0.03
r.new_bone_creation(pos_1, pos_2, 'MCH_footRoll_3_L', rig, 'footIK_L', False, 0)
pos_1, pos_2 = r.bone_global_locations(rig, 'heelPosition_L')
pos_1[0] -= 0.03
pos_2[0] -= 0.03
r.new_bone_creation(pos_1, pos_2, 'MCH_footRoll_2_L', rig, 'MCH_footRoll_3_L', False, 0)
r.parent_bone(rig, 'heelPosition_L', 'MCH_footRoll_2_L', False)
r.parent_bone(rig, 'heelPosition_R', 'MCH_footRoll_2_R', False)

r.copy_rotation(rig, 'MCH_footRoll_2_L',subtarget='footRollCTRL_L', use_y=True, target_space='LOCAL', owner_space='LOCAL')
r.copy_rotation(rig, 'MCH_footRoll_2_R',subtarget='footRollCTRL_R', use_y=True, target_space='LOCAL', owner_space='LOCAL')
r.limit_rotation(rig, 'MCH_footRoll_2_L', min_y=r.degree_to_radians(-170), max_y=0, limit_y=True, target_space='LOCAL', owner_space='LOCAL')
r.limit_rotation(rig, 'MCH_footRoll_2_R', min_y=r.degree_to_radians(-170), max_y=0, limit_y=True, target_space='LOCAL', owner_space='LOCAL')

r.copy_rotation(rig, 'MCH_footRoll_3_L',subtarget='footRollCTRL_L', use_y=True, target_space='LOCAL', owner_space='LOCAL')
r.copy_rotation(rig, 'MCH_footRoll_3_R',subtarget='footRollCTRL_R', use_y=True, target_space='LOCAL', owner_space='LOCAL')
r.limit_rotation(rig, 'MCH_footRoll_3_L', max_y=r.degree_to_radians(170), limit_y=True, target_space='LOCAL', owner_space='LOCAL')
r.limit_rotation(rig, 'MCH_footRoll_3_R', max_y=r.degree_to_radians(170), limit_y=True, target_space='LOCAL', owner_space='LOCAL')

# 28-33
pos_1, pos_2 = r.bone_global_locations(rig, 'MCH_footRoll_1_L')
r.new_bone_creation(pos_1, pos_2, 'heelHeight_L', rig, 'heelPosition_L', False, 0)
r.remove_constraints(rig, 'heelHeight_L')
length = r.bone_length('heelHeight_L', rig)
r.change_bone_length('heelHeight_L', rig, (length*2.5))
r.parent_bone(rig, 'heelHeight_L', 'heelPosition_L', False)
r.eular_change(rig, 'heelHeight_L', 'XYZ')
r.lock_rotation(rig, 'heelHeight_L', y=True, z=True)
r.lock_location(rig, 'heelPosition_L',x=True, z=True)
r.lock_rotation(rig, 'heelPosition_L', x=True, y=True, z=True, w=True)
r.lock_scale(rig, 'heelPosition_L', x=True, y=True, z=True)

pos_1, pos_2 = r.bone_global_locations(rig, 'MCH_footRoll_1_R')
r.new_bone_creation(pos_1, pos_2, 'heelHeight_R', rig, 'heelPosition_R', False, 0)
r.remove_constraints(rig, 'heelHeight_R')
length = r.bone_length('heelHeight_R', rig)
r.change_bone_length('heelHeight_R', rig, (length*2.5))
r.parent_bone(rig, 'heelHeight_R', 'heelPosition_R', False)
r.eular_change(rig, 'heelHeight_R', 'XYZ')
r.lock_rotation(rig, 'heelHeight_R', y=True, z=True)
r.lock_location(rig, 'heelPosition_R',x=True, z=True)
r.lock_rotation(rig, 'heelPosition_R', x=True, y=True, z=True, w=True)
r.lock_scale(rig, 'heelPosition_R', x=True, y=True, z=True)

# 35-38
r.transformation(rig, 'heelHeight_L', from_max_y=1, to_max_y=-1, map_from='LOCATION',map_to_y_from="Y", subtarget='heelPosition_L', target=rig,use_motion_extrapolate=True, owner_space="LOCAL", target_space='LOCAL')
r.copy_location(rig, 'toesIK_L', subtarget='heelHeight_L', use_x=True, use_y=True, use_z=True)
r.copy_rotation(rig, 'toes_L', subtarget='toesIK_L', use_x=True, use_y=True, use_z=True)
r.copy_rotation(rig, 'footFK_L', subtarget='MCH_foot_L', use_x=True, use_y=True, use_z=True)

r.transformation(rig, 'heelHeight_R', from_max_y=1, to_max_y=-1, map_from='LOCATION',map_to_y_from="Y", subtarget='heelPosition_R', target=rig,use_motion_extrapolate=True, owner_space="LOCAL", target_space='LOCAL')
r.copy_location(rig, 'toesIK_R', subtarget='heelHeight_R', use_x=True, use_y=True, use_z=True)
r.copy_rotation(rig, 'toes_R', subtarget='toesIK_R', use_x=True, use_y=True, use_z=True)
r.copy_rotation(rig, 'footFK_R', subtarget='MCH_foot_R', use_x=True, use_y=True, use_z=True)

roll_list = ['toesIK_L', 'toesIK_R', 'toes_L', 'toes_R', 'heelHeight_L', 'heelHeight_R', 'MCH_footRoll_1_L', 'MCH_footRoll_1_R', 'heelPosition_L', 'heelPosition_R','MCH_footRoll_2_L','MCH_footRoll_2_R','MCH_footRoll_3_L', 'MCH_footRoll_3_R']
r.set_mode('OBJECT')
r.remove_object_selection()
r.object_selection(rig)
r.set_mode('EDIT')

for item in roll_list:
    arm = bpy.data.armatures[rig]

    bone = arm.edit_bones[item]
    bone.roll = 0

# 39-43 -
start_point, global_pos, end_point, global_alt = r.object_location('knee_Empty_L', y=-.1, alter=True)
r.new_bone_creation(start_point, end_point, 'kneePole_L', rig, 'footIK_L', False, 0)
r.change_bone_length('kneePole_L', rig, .12)
r.parent_bone(rig, 'kneePole_L', 'footIK_L', False)
pos_1, pos_2 = r.bone_global_locations(rig, 'kneePole_L')
pos_1[1] += -.7
pos_2[1] += -.7
r.move_head_or_tail('kneePole_L', rig, True, True, pos_1, pos_2)

start_point, global_pos, end_point, global_alt = r.object_location('knee_Empty_R', y=-.1, alter=True)
r.new_bone_creation(start_point, end_point, 'kneePole_R', rig, 'footIK_R', False, 0)
r.change_bone_length('kneePole_R', rig, .12)
r.parent_bone(rig, 'kneePole_R', 'footIK_R', False)
pos_1, pos_2 = r.bone_global_locations(rig, 'kneePole_R')
pos_1[1] += -.7
pos_2[1] += -.7
r.move_head_or_tail('kneePole_R', rig, True, True, pos_1, pos_2)


# 44

### new ik location
r.create_IK(rig, 'tibia_L', 2, 0, 'kneePole_L', rig, 'MCH_foot_L', rig)
r.create_IK(rig, 'tibia_R', 2, r.degree_to_radians(-180), 'kneePole_R', rig, 'MCH_foot_R', rig)

sys.path.remove(module_dir)
