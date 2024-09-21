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

## adding fk/ik switch to legs

# r.duplicate_bone(rig, 'femur_L', 'femur_IK_L')
# r.duplicate_bone(rig, 'femur_L', 'femur_FK_L')
# r.duplicate_bone(rig, 'tibia_L', 'tibia_IK_L')
# r.duplicate_bone(rig, 'tibia_L', 'tibia_FK_L')

r.duplicate_bones(rig, 'femur_L', 'femur_IK_L', 'pelvis_L', False, r.bone_roll(rig, 'femur_L'), True)
r.duplicate_bones(rig, 'femur_L', 'femur_FK_L', 'pelvis_L', False, r.bone_roll(rig, 'femur_L'), True)
r.duplicate_bones(rig, 'tibia_L', 'tibia_IK_L', 'femur_IK_L', False, r.bone_roll(rig, 'tibia_L'), True)
r.duplicate_bones(rig, 'tibia_L', 'tibia_FK_L', 'femur_FK_L', False, r.bone_roll(rig, 'tibia_L'), True)

r.duplicate_bones(rig, 'femur_R', 'femur_IK_R', 'pelvis_R', False, r.bone_roll(rig, 'femur_R'), True)
r.duplicate_bones(rig, 'femur_R', 'femur_FK_R', 'pelvis_R', False, r.bone_roll(rig, 'femur_R'), True)
r.duplicate_bones(rig, 'tibia_R', 'tibia_IK_R', 'femur_IK_R', False, r.bone_roll(rig, 'tibia_R'), True)
r.duplicate_bones(rig, 'tibia_R', 'tibia_FK_R', 'femur_FK_R', False, r.bone_roll(rig, 'tibia_R'), True)

# r.parent_bone(rig, 'femur_IK_L', 'pelvis_L', False)
# r.parent_bone(rig, 'femur_FK_L', 'pelvis_L', False)
# r.parent_bone(rig, 'tibia_IK_L', 'femur_IK_L', False)
# r.parent_bone(rig, 'tibia_FK_L', 'femur_FK_L', False)

r.copy_transforms(rig, 'femur_L', 1, 'femur_IK_L')
r.copy_transforms(rig, 'femur_L', 0, 'femur_FK_L')
r.copy_transforms(rig, 'tibia_L', 1, 'tibia_IK_L')
r.copy_transforms(rig, 'tibia_L', 0, 'tibia_FK_L')

r.copy_transforms(rig, 'femur_R', 1, 'femur_IK_R')
r.copy_transforms(rig, 'femur_R', 0, 'femur_FK_R')
r.copy_transforms(rig, 'tibia_R', 1, 'tibia_IK_R')
r.copy_transforms(rig, 'tibia_R', 0, 'tibia_FK_R')

r.create_IK(rig, 'tibia_IK_L', 2, r.degree_to_radians(-0.77), 'kneePole_L', 'kneePole_L', 'MCH_foot_L', 'Female Transfer Rig')
r.create_IK(rig, 'tibia_IK_R', 2, r.degree_to_radians(-179.24), 'kneePole_R', 'kneePole_R', 'MCH_foot_R', 'Female Transfer Rig')

arm_temp = bpy.data.objects[rig]
bone_to_alter = arm_temp.pose.bones['tibia_L']

for constraint in bone_to_alter.constraints:
    if constraint.name == "IK":
        bone_to_alter.constraints.remove(constraint)

arm_temp = bpy.data.objects[rig]
bone_to_alter = arm_temp.pose.bones['tibia_R']

for constraint in bone_to_alter.constraints:
    if constraint.name == "IK":
        bone_to_alter.constraints.remove(constraint)

# ### Creating custom properties ###

arm = bpy.data.objects[rig]

arm["L_Arm FK IK"] = 1.0
prop = arm.id_properties_ui("L_Arm FK IK")
prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

left_arm_data_path = ["L_Arm FK IK"]
left_arm_full_data_path = bpy.data.objects[rig]["L_Arm FK IK"]

arm = bpy.data.objects[rig]

arm["R_Arm FK IK"] = 1.0
prop = arm.id_properties_ui("R_Arm FK IK")
prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

right_arm_data_path = arm["R_Arm FK IK"]
right_arm_full_data_path = bpy.data.objects[rig]["R_Arm FK IK"]

arm["L_Leg FK IK"] = 1.0
prop = arm.id_properties_ui("L_Leg FK IK")
prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

left_leg_data_path = arm["L_Leg FK IK"]
left_leg_full_data_path = bpy.data.objects[rig]["L_Leg FK IK"]

arm["R_Leg FK IK"] = 1.0
prop = arm.id_properties_ui("R_Leg FK IK")
prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

right_leg_data_path = arm["R_Leg FK IK"]
right_leg_full_data_path = bpy.data.objects[rig]["R_Leg FK IK"]


# obj = bpy.data.objects[rig]
# bone = obj.pose.bones['root']
# bone["L_Arm FK IK"] = 1.0
# prop = bone.id_properties_ui("L_Arm FK IK")
# prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

# left_arm_data_path = bone["L_Arm FK IK"]
# #correct data path for driver = pose.bones["Bone.001"]["FK IK"]
# left_arm_full_data_path = bpy.data.objects[rig].pose.bones["root"]["L_Arm FK IK"]

# obj = bpy.data.objects[rig]
# bone = obj.pose.bones['root']
# bone["R_Arm FK IK"] = 1.0
# prop = bone.id_properties_ui("R_Arm FK IK")
# prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

# left_arm_data_path = bone["R_Arm FK IK"]
# #correct data path for driver = pose.bones["Bone.001"]["FK IK"]
# left_arm_full_data_path = bpy.data.objects[rig].pose.bones["root"]["R_Arm FK IK"]

# obj = bpy.data.objects[rig]
# bone = obj.pose.bones['root']
# bone["L_Leg FK IK"] = 1.0
# prop = bone.id_properties_ui("L_Leg FK IK")
# prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

# left_arm_data_path = bone["L_Leg FK IK"]
# #correct data path for driver = pose.bones["Bone.001"]["FK IK"]
# left_arm_full_data_path = bpy.data.objects[rig].pose.bones["root"]["L_Leg FK IK"]

# obj = bpy.data.objects[rig]
# bone = obj.pose.bones['root']
# bone["R_Leg FK IK"] = 1.0
# prop = bone.id_properties_ui("R_Leg FK IK")
# prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

# left_arm_data_path = bone["R_Leg FK IK"]
# #correct data path for driver = pose.bones["Bone.001"]["FK IK"]
# left_arm_full_data_path = bpy.data.objects[rig].pose.bones["root"]["R_Leg FK IK"]

### Creating Drivers for FK IK Switch ###

FK = ['humerus_FK_L', 'humerus_FK_R', 'forearm_FK_L', 'forearm_FK_R', 'armTwist_1_FK_L', 'armTwist_1_FK_R', 'armTwist_2_FK_L', 'armTwist_2_FK_R', 'armTwist_3_FK_L', 'armTwist_3_FK_R', 'hand_FK_L', 'hand_FK_R', 'femur_FK_L', "femur_FK_R", "tibia_FK_L", "tibia_FK_R"]
IK = ['humerus_IK_L', 'humerus_IK_R', 'forearm_IK_L', 'forearm_IK_R', 'armTwist_1_IK_L', 'armTwist_1_IK_R', 'armTwist_2_IK_L', 'armTwist_2_IK_R', 'armTwist_3_IK_L', 'armTwist_3_IK_R', 'hand_IK_L', 'hand_IK_R', "femur_IK_L", "femur_IK_R", "tibia_IK_L", "tibia_IK_R"]
deform_arm_list = ["humerus_L", "humerus_R", "forearm_L",  "forearm_R", "armTwist_1_L", "armTwist_1_R", "armTwist_2_L", "armTwist_2_R", "armTwist_3_L","armTwist_3_R", "hand_L", "hand_R", "femur_L", "femur_R", "tibia_L", "tibia_R"]
deform_leg_list = ["femur_L", "femur_R", "tibia_L", "tibia_R"]
deform_foot_list = ["footFK_L", "footFK_R", "toes_L", "toes_R"]

armature_obj = bpy.data.objects.get(rig)
# armature_obj = bpy.data.objects.get('female transfer rig')["L_Arm FK IK"]

for item in deform_arm_list:
    # Copy Transforms.001 - IK
    # Copy Transforms - FK
    ##IK below - 
    if "_L" in item:
        bone = armature_obj.pose.bones.get(item)
        constraint_name = "Copy Transforms.001"
        constraint = bone.constraints.get(constraint_name)
        driver = constraint.driver_add("influence")
        driver2 = driver.driver
        driver2.type = 'AVERAGE'
        var = driver2.variables.new()
        var.name = 'var'
        target = var.targets[0]
        target.id = bpy.data.objects.get(rig)
        # target.data_path = 'pose.bones["root"]["L_Arm FK IK"]'
        target.data_path = '["L_Arm FK IK"]'
        driver.modifiers.remove(driver.modifiers[0])

        driver.keyframe_points.insert(0,1)
        driver.keyframe_points.insert(1,0)
        point1 = driver.keyframe_points[0]
        point2 = driver.keyframe_points[1]

        #point1.interpolation = "SINE"
        point1.easing = "EASE_OUT"
        point1.handle_left = (-0.333333, 1.33333)
        point1.handle_right = (0.333333, 0.666667)
        #point2.interpolation = "SINE"
        point2.handle_left = (0.666667, 0.333333)
        point2.handle_right = (1.33333, -0.333333)

        ##IK below - 
        constraint_name = "Copy Transforms"
        constraint = bone.constraints.get(constraint_name)
        driver = constraint.driver_add("influence")
        driver2 = driver.driver
        driver2.type = 'AVERAGE'
        var = driver2.variables.new()
        var.name = 'var'
        target = var.targets[0]
        target.id = bpy.data.objects.get(rig)
        target.data_path = '["L_Arm FK IK"]'
        driver.modifiers.remove(driver.modifiers[0])

        driver.keyframe_points.insert(0,0)
        driver.keyframe_points.insert(1,1)

        point1 = driver.keyframe_points[0]
        point2 = driver.keyframe_points[1]

        #point1.interpolation = "SINE"
        point1.easing = "EASE_OUT"
        point1.handle_left = (-0.333333, -0.333333)
        point1.handle_right = (0.333333, 0.333333)

        #point2.interpolation = "SINE"
        point2.handle_left = (0.666667, 0.666667)
        point2.handle_right = (1.33333, 1.33333)

    if "_R" in item:
        bone = armature_obj.pose.bones.get(item)
        constraint_name = "Copy Transforms.001"
        constraint = bone.constraints.get(constraint_name)
        driver = constraint.driver_add("influence")
        driver2 = driver.driver
        driver2.type = 'AVERAGE'
        var = driver2.variables.new()
        var.name = 'var'
        target = var.targets[0]
        target.id = bpy.data.objects.get(rig)
        target.data_path = '["R_Arm FK IK"]'
        driver.modifiers.remove(driver.modifiers[0])

        driver.keyframe_points.insert(0,1)
        driver.keyframe_points.insert(1,0)
        point1 = driver.keyframe_points[0]
        point2 = driver.keyframe_points[1]

        #point1.interpolation = "SINE"
        point1.easing = "EASE_OUT"
        point1.handle_left = (-0.333333, 1.33333)
        point1.handle_right = (0.333333, 0.666667)
        #point2.interpolation = "SINE"
        point2.handle_left = (0.666667, 0.333333)
        point2.handle_right = (1.33333, -0.333333)

        ##IK below - 
        constraint_name = "Copy Transforms"
        constraint = bone.constraints.get(constraint_name)
        driver = constraint.driver_add("influence")
        driver2 = driver.driver
        driver2.type = 'AVERAGE'
        var = driver2.variables.new()
        var.name = 'var'
        target = var.targets[0]
        target.id = bpy.data.objects.get(rig)
        target.data_path = '["R_Arm FK IK"]'
        driver.modifiers.remove(driver.modifiers[0])

        driver.keyframe_points.insert(0,0)
        driver.keyframe_points.insert(1,1)

        point1 = driver.keyframe_points[0]
        point2 = driver.keyframe_points[1]

        #point1.interpolation = "SINE"
        point1.easing = "EASE_OUT"
        point1.handle_left = (-0.333333, -0.333333)
        point1.handle_right = (0.333333, 0.333333)

        #point2.interpolation = "SINE"
        point2.handle_left = (0.666667, 0.666667)
        point2.handle_right = (1.33333, 1.33333)

for item in deform_leg_list:
    # Copy Transforms.001 - IK
    # Copy Transforms - FK
    ##IK below - 
    if "_L" in item:
        bone = armature_obj.pose.bones.get(item)
        constraint_name = "Copy Transforms.001"
        constraint = bone.constraints.get(constraint_name)
        driver = constraint.driver_add("influence")
        driver2 = driver.driver
        driver2.type = 'AVERAGE'
        var = driver2.variables.new()
        var.name = 'var'
        target = var.targets[0]
        target.id = bpy.data.objects.get(rig)
        # target.data_path = 'pose.bones["root"]["L_Arm FK IK"]'
        target.data_path = '["L_Leg FK IK"]'
        # driver.modifiers.remove(driver.modifiers[0])

        driver.keyframe_points.insert(0,1)
        driver.keyframe_points.insert(1,0)
        point1 = driver.keyframe_points[0]
        point2 = driver.keyframe_points[1]

        #point1.interpolation = "SINE"
        point1.easing = "EASE_OUT"
        point1.handle_left = (-0.333333, 1.33333)
        point1.handle_right = (0.333333, 0.666667)
        #point2.interpolation = "SINE"
        point2.handle_left = (0.666667, 0.333333)
        point2.handle_right = (1.33333, -0.333333)

        ##IK below - 
        constraint_name = "Copy Transforms"
        constraint = bone.constraints.get(constraint_name)
        driver = constraint.driver_add("influence")
        driver2 = driver.driver
        driver2.type = 'AVERAGE'
        var = driver2.variables.new()
        var.name = 'var'
        target = var.targets[0]
        target.id = bpy.data.objects.get(rig)
        target.data_path = '["L_Arm FK IK"]'
        # driver.modifiers.remove(driver.modifiers[0])

        driver.keyframe_points.insert(0,0)
        driver.keyframe_points.insert(1,1)

        point1 = driver.keyframe_points[0]
        point2 = driver.keyframe_points[1]

        #point1.interpolation = "SINE"
        point1.easing = "EASE_OUT"
        point1.handle_left = (-0.333333, -0.333333)
        point1.handle_right = (0.333333, 0.333333)

        #point2.interpolation = "SINE"
        point2.handle_left = (0.666667, 0.666667)
        point2.handle_right = (1.33333, 1.33333)

    if "_R" in item:
        bone = armature_obj.pose.bones.get(item)
        constraint_name = "Copy Transforms.001"
        constraint = bone.constraints.get(constraint_name)
        driver = constraint.driver_add("influence")
        driver2 = driver.driver
        driver2.type = 'AVERAGE'
        var = driver2.variables.new()
        var.name = 'var'
        target = var.targets[0]
        target.id = bpy.data.objects.get(rig)
        target.data_path = '["R_Leg FK IK"]'
        # driver.modifiers.remove(driver.modifiers[0])

        driver.keyframe_points.insert(0,1)
        driver.keyframe_points.insert(1,0)
        point1 = driver.keyframe_points[0]
        point2 = driver.keyframe_points[1]

        #point1.interpolation = "SINE"
        point1.easing = "EASE_OUT"
        point1.handle_left = (-0.333333, 1.33333)
        point1.handle_right = (0.333333, 0.666667)
        #point2.interpolation = "SINE"
        point2.handle_left = (0.666667, 0.333333)
        point2.handle_right = (1.33333, -0.333333)

        ##IK below - 
        constraint_name = "Copy Transforms"
        constraint = bone.constraints.get(constraint_name)
        driver = constraint.driver_add("influence")
        driver2 = driver.driver
        driver2.type = 'AVERAGE'
        var = driver2.variables.new()
        var.name = 'var'
        target = var.targets[0]
        target.id = bpy.data.objects.get(rig)
        target.data_path = '["R_Arm FK IK"]'
        # driver.modifiers.remove(driver.modifiers[0])

        driver.keyframe_points.insert(0,0)
        driver.keyframe_points.insert(1,1)

        point1 = driver.keyframe_points[0]
        point2 = driver.keyframe_points[1]

        #point1.interpolation = "SINE"
        point1.easing = "EASE_OUT"
        point1.handle_left = (-0.333333, -0.333333)
        point1.handle_right = (0.333333, 0.333333)

        #point2.interpolation = "SINE"
        point2.handle_left = (0.666667, 0.666667)
        point2.handle_right = (1.33333, 1.33333)

for item in deform_foot_list:
    # Copy Transforms.001 - IK
    # Copy Transforms - FK
    ##IK below - 
    if "_L" in item:
        bone = armature_obj.pose.bones.get(item)
        constraint_name = "Copy Rotation"
        constraint = bone.constraints.get(constraint_name)
        driver = constraint.driver_add("influence")
        driver2 = driver.driver
        driver2.type = 'AVERAGE'
        var = driver2.variables.new()
        var.name = 'var'
        target = var.targets[0]
        target.id = bpy.data.objects.get(rig)
        # target.data_path = 'pose.bones["root"]["L_Arm FK IK"]'
        target.data_path = '["L_Leg FK IK"]'
        # driver.modifiers.remove(driver.modifiers[0])

        driver.keyframe_points.insert(0,1)
        driver.keyframe_points.insert(1,0)
        point1 = driver.keyframe_points[0]
        point2 = driver.keyframe_points[1]

        #point1.interpolation = "SINE"
        point1.easing = "EASE_OUT"
        point1.handle_left = (-0.333333, 1.33333)
        point1.handle_right = (0.333333, 0.666667)
        #point2.interpolation = "SINE"
        point2.handle_left = (0.666667, 0.333333)
        point2.handle_right = (1.33333, -0.333333)

    if "_R" in item:
        bone = armature_obj.pose.bones.get(item)
        constraint_name = "Copy Rotation"
        constraint = bone.constraints.get(constraint_name)
        driver = constraint.driver_add("influence")
        driver2 = driver.driver
        driver2.type = 'AVERAGE'
        var = driver2.variables.new()
        var.name = 'var'
        target = var.targets[0]
        target.id = bpy.data.objects.get(rig)
        target.data_path = '["R_Leg FK IK"]'
        # driver.modifiers.remove(driver.modifiers[0])

        driver.keyframe_points.insert(0,1)
        driver.keyframe_points.insert(1,0)
        point1 = driver.keyframe_points[0]
        point2 = driver.keyframe_points[1]

        #point1.interpolation = "SINE"
        point1.easing = "EASE_OUT"
        point1.handle_left = (-0.333333, 1.33333)
        point1.handle_right = (0.333333, 0.666667)
        #point2.interpolation = "SINE"
        point2.handle_left = (0.666667, 0.333333)
        point2.handle_right = (1.33333, -0.333333)


#####

change_deform = ["tibia_IK_L", "tibia_FK_L", "tibia_IK_R", "tibia_FK_R", "femur_IK_L", "femur_FK_L", "femur_IK_R", "femur_IK_L"]

arm_again = bpy.data.armatures[rig]

r.set_mode("EDIT")

for item in change_deform:
    arm = bpy.data.armatures[rig]
    bone = arm.edit_bones[item]
    bone.use_deform = False


# ## CLEAN UP and Bug fixes

arm = bpy.data.armatures[rig]
bone_for_roll = arm.edit_bones['thumbRotation_L']
bone_for_roll.roll = r.bone_roll(rig, 'thumb_2_L')

bone_for_roll = arm.edit_bones['thumbRotation_R']
bone_for_roll.roll = r.bone_roll(rig, 'thumb_2_R')

bone = r.select_bone_as_active_pose(rig, 'clavicle_L')
bone.constraints[-1].mix_mode = "AFTER"

bone = r.select_bone_as_active_pose(rig, 'clavicle_R')
bone.constraints[-1].mix_mode = "AFTER"

r.lock_rotation(rig, 'toesIK_L', y=True, z=True)
r.lock_rotation(rig, 'toesIK_R', y=True, z=True)

r.parent_bone(rig, 'hand_IK_L', 'root', False)
r.parent_bone(rig, 'hand_IK_R', 'root', False)

r.parent_bone(rig, 'pelvis_L', 'hipTwist', False)
r.parent_bone(rig, 'pelvis_R', 'hipTwist', False)

arm = bpy.data.armatures[rig]
bone = arm.edit_bones['kneePole_L']
bone.parent = None
bone_roll_fix = bone.roll
bone = arm.edit_bones['kneePole_R']
bone.parent = None
bone.roll = bone_roll_fix

bone = arm.edit_bones['footIK_L']
foot_ik_roll_fix = -bone.roll
bone = arm.edit_bones['footIK_R']
bone.roll = foot_ik_roll_fix

bone = arm.edit_bones['toesIK_L']
bone.roll = 0

bone = r.select_bone_as_active_pose(rig, 'neck_1')
bone.constraints[-1].mix_mode = "AFTER"

bone = r.select_bone_as_active_pose(rig, 'head')
bone.constraints[-1].mix_mode = "AFTER"

r.limit_rotation(rig, 'clavicle_L', max_z=r.degree_to_radians(30), min_z=r.degree_to_radians(-9), limit_z=True, owner_space='LOCAL')
r.limit_rotation(rig, 'clavicle_R', max_z=r.degree_to_radians(9), min_z=r.degree_to_radians(-30), limit_z=True, owner_space='LOCAL')

## fist control ##



r.set_mode('POSE')




# ## adding actions for clavicle and breast follow
# ## need to add this to the first script

# # r.anim_action(rig, 'scapula_L', 'Clavicle_L_rotation_pose_1', 'Elbow_actions_L', 0, 20, 1.21591, 1.27059,transform_channel='LOCATION_Z')
# # r.anim_action(rig, 'scapula_L', 'Clavicle_L_rotation_pose_2', 'Elbow_actions_L', 0, 40, 1.27059, 1.76191,transform_channel='LOCATION_Z')
# # r.anim_action(rig, 'scapula_L', 'Clavicle forward_L', 'Elbow_actions_L', 0, 20, 0.041209, -0.182764,transform_channel='LOCATION_Y')
# # r.anim_action(rig, 'scapula_L', 'Clavicle backward_L', 'Elbow_actions_L', 0, 20, 0.041209, 0.284233,transform_channel='LOCATION_Y')

# # r.anim_action(rig, 'scapula_R', 'Clavicle_R_rotation_pose_1', 'Elbow_actions_R', 0, 20, 1.21591, 1.27059,transform_channel='LOCATION_Z')
# # r.anim_action(rig, 'scapula_R', 'Clavicle_R_rotation_pose_2', 'Elbow_actions_R', 0, 40, 1.27059, 1.76191,transform_channel='LOCATION_Z')
# # r.anim_action(rig, 'scapula_R', 'Clavicle forward_R', 'Elbow_actions_R', 0, 20, 0.041209, -0.182764,transform_channel='LOCATION_Y')
# # r.anim_action(rig, 'scapula_R', 'Clavicle backward_R', 'Elbow_actions_R', 0, 20, 0.041209, 0.284233,transform_channel='LOCATION_Y')

# # r.anim_action(rig, 'breast_L', 'breast_follow_up_L', 'Elbow_actions_L', 0, 20, 1.27059, 1.76191,transform_channel='LOCATION_Z')
# # r.anim_action(rig, 'breast_L', 'breast_follow_down_L', 'Elbow_actions_L', 0, 20, 1.27059, 1.21591,transform_channel='LOCATION_Z')
# # r.anim_action(rig, 'breast_L', 'breast_follow_back_L', 'Elbow_actions_L', 0, 20, 0.041209, 0.32314,transform_channel='LOCATION_Y')

# # r.anim_action(rig, 'breast_R', 'breast_follow_up_R', 'Elbow_actions_R', 0, 20, 1.27059, 1.76191,transform_channel='LOCATION_Z')
# # r.anim_action(rig, 'breast_R', 'breast_follow_down_R', 'Elbow_actions_R', 0, 20, 1.27059, 1.21591,transform_channel='LOCATION_Z')
# # r.anim_action(rig, 'breast_R', 'breast_follow_back_R', 'Elbow_actions_R', 0, 20, 0.041209, 0.32314,transform_channel='LOCATION_Y')

# # r.set_mode('OBJECT')
# # r.remove_object_selection()
# # r.object_selection(rig)
# # bone = r.select_bone_as_active_pose(rig, 'scapula_L')
# # action = bone.constraints.new(type='ACTION')
# # target = bpy.data.objects['Elbow_actions_L']
# # action.action = bpy.data.actions['Clavicle_l_rotation_pose_1']
# # action.frame_end = 20
# # action.frame_start = 0
# # action.max = 1.21591
# # action.min = 1.27059
# # # action.mix_mode = 'LOCATION_Z'
# # action.subtarget = ""
# # action.target = target
# # # action.use_eval = use_eval
# # action.transform_channel = 'LOCATION_Z'
# # # action.use_bone_object_action = 'Clavicle_1_rotation_pose_1'

sys.path.remove(module_dir)

