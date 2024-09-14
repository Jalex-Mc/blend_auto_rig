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

### Creating custom properties ###

obj = bpy.data.objects[rig]
bone = obj.pose.bones['root']
bone["L_Arm FK IK"] = 1.0
prop = bone.id_properties_ui("L_Arm FK IK")
prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

left_arm_data_path = bone["L_Arm FK IK"]
#correct data path for driver = pose.bones["Bone.001"]["FK IK"]
left_arm_full_data_path = bpy.data.objects[rig].pose.bones["root"]["L_Arm FK IK"]

obj = bpy.data.objects[rig]
bone = obj.pose.bones['root']
bone["R_Arm FK IK"] = 1.0
prop = bone.id_properties_ui("R_Arm FK IK")
prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

left_arm_data_path = bone["R_Arm FK IK"]
#correct data path for driver = pose.bones["Bone.001"]["FK IK"]
left_arm_full_data_path = bpy.data.objects[rig].pose.bones["root"]["R_Arm FK IK"]

obj = bpy.data.objects[rig]
bone = obj.pose.bones['root']
bone["L_Leg FK IK"] = 1.0
prop = bone.id_properties_ui("L_Leg FK IK")
prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

left_arm_data_path = bone["L_Leg FK IK"]
#correct data path for driver = pose.bones["Bone.001"]["FK IK"]
left_arm_full_data_path = bpy.data.objects[rig].pose.bones["root"]["L_Leg FK IK"]

obj = bpy.data.objects[rig]
bone = obj.pose.bones['root']
bone["R_Leg FK IK"] = 1.0
prop = bone.id_properties_ui("R_Leg FK IK")
prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

left_arm_data_path = bone["R_Leg FK IK"]
#correct data path for driver = pose.bones["Bone.001"]["FK IK"]
left_arm_full_data_path = bpy.data.objects[rig].pose.bones["root"]["R_Leg FK IK"]

### Creating Drivers for FK IK Switch ###

FK = ['humerus_FK_L', 'humerus_FK_R', 'forearm_FK_L', 'forearm_FK_R', 'armTwist_1_FK_L', 'armTwist_1_FK_R', 'armTwist_2_FK_L', 'armTwist_2_FK_R', 'armTwist_3_FK_L', 'armTwist_3_FK_R', 'hand_FK_L', 'hand_FK_R']
IK = ['humerus_IK_L', 'humerus_IK_R', 'forearm_IK_L', 'forearm_IK_R', 'armTwist_1_IK_L', 'armTwist_1_IK_R', 'armTwist_2_IK_L', 'armTwist_2_IK_R', 'armTwist_3_IK_L', 'armTwist_3_IK_R', 'hand_IK_L', 'hand_IK_R']
deform_list = ["humerus_L", "humerus_R", "forearm_L",  "forearm_R", "armTwist_1_L", "armTwist_1_R", "armTwist_2_L", "armTwist_2_R", "armTwist_3_L","armTwist_3_R", "hand_L", "hand_R"]

armature_obj = bpy.data.objects.get(rig)

for item in deform_list:
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
        target.data_path = 'pose.bones["root"]["L_Arm FK IK"]'
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
        target.data_path = 'pose.bones["root"]["L_Arm FK IK"]'
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
        target.data_path = 'pose.bones["root"]["R_Arm FK IK"]'
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
        target.data_path = 'pose.bones["root"]["R_Arm FK IK"]'
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

## LEG CLEAN UP


r.duplicate_bones(rig, 'tibia_L', 'tibia_IK_L', 'femur_L', False, r.degree_to_radians(71.1287), False)
r.duplicate_bones(rig, 'tibia_L', 'tibia_FK_L', 'femur_L', False, r.degree_to_radians(71.1287), False)
r.duplicate_bones(rig, 'tibia_R', 'tibia_IK_R', 'femur_R', False, r.degree_to_radians(-71.1287), False)
r.duplicate_bones(rig, 'tibia_R', 'tibia_FK_R', 'femur_R', False, r.degree_to_radians(-71.1287), False)

change_deform = ["tibia_IK_L", "tibia_FK_L", "tibia_IK_R", "tibia_FK_R"]

for item in change_deform:
    arm = bpy.data.armatures[rig]
    bone = arm.edit_bones[item]
    bone.use_deform = False


def copy_bone_constraint(source_bone, target_bone, constraint_type):
    # Iterate through constraints of source bone
    for constraint in source_bone.constraints:
        if constraint.type == constraint_type:
            # Create a new constraint on the target bone
            new_constraint = target_bone.constraints.new(type=constraint_type)
            
            # Copy properties from the source constraint to the new constraint
            for prop in constraint.bl_rna.properties:
                if not prop.is_readonly and prop.identifier != "rna_type":
                    try:
                        setattr(new_constraint, prop.identifier, getattr(constraint, prop.identifier))
                    except AttributeError:
                        pass
            break  # Exit loop after finding the first constraint of the specified type

r.remove_edit_and_arm_selection(rig)
r.set_mode("OBJECT")
r.remove_object_selection()
r.object_selection(rig)

## Chatgpt answer for transfering over IK from og tibia.

if bpy.context.active_object and bpy.context.active_object.type == 'ARMATURE':
    armature = bpy.context.active_object
    source_bone_name = "tibia_L"  # Replace with the name of the source bone
    target_bone_name = "tibia_IK_L"  # Replace with the name of the target bone
    
    source_bone = armature.pose.bones.get(source_bone_name)
    target_bone = armature.pose.bones.get(target_bone_name)
    
    if source_bone and target_bone:
        constraint_type = 'IK'  # Replace with the type of constraint you want to copy
        
        copy_bone_constraint(source_bone, target_bone, constraint_type)
        print(f"Constraint '{constraint_type}' copied from '{source_bone_name}' to '{target_bone_name}'.")
    else:
        print("Source or target bone not found.")
else:
    print("Active object is not an armature or no active object found.")

if bpy.context.active_object and bpy.context.active_object.type == 'ARMATURE':
    armature = bpy.context.active_object
    source_bone_name = "tibia_R"  # Replace with the name of the source bone
    target_bone_name = "tibia_IK_R"  # Replace with the name of the target bone
    
    source_bone = armature.pose.bones.get(source_bone_name)
    target_bone = armature.pose.bones.get(target_bone_name)
    
    if source_bone and target_bone:
        constraint_type = 'IK'  # Replace with the type of constraint you want to copy
        
        copy_bone_constraint(source_bone, target_bone, constraint_type)
        print(f"Constraint '{constraint_type}' copied from '{source_bone_name}' to '{target_bone_name}'.")
    else:
        print("Source or target bone not found.")
else:
    print("Active object is not an armature or no active object found.")

armature = bpy.data.objects.get(rig)
temp_bone = armature.pose.bones.get("tibia_L")
temp_bone.constraints.remove(temp_bone.constraints["IK"])
temp_bone = armature.pose.bones.get("tibia_R")
temp_bone.constraints.remove(temp_bone.constraints["IK"])

leg_list = ["tibia_L", "tibia_R", "footFK_L", "footFK_R"]

r.copy_transforms(rig, "tibia_L", 1, "tibia_IK_L")
r.copy_transforms(rig, "tibia_L", 0, "tibia_FK_L")
r.copy_transforms(rig, "tibia_R", 1, "tibia_IK_R")
r.copy_transforms(rig, "tibia_R", 0, "tibia_FK_R")


for item in leg_list:
    if "footFK_L" in item:
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
        target.data_path = 'pose.bones["root"]["L_Leg FK IK"]'
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

    elif "_L" and "tibia" in item:
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
        target.data_path = 'pose.bones["root"]["L_Leg FK IK"]'
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
        target.data_path = 'pose.bones["root"]["L_Leg FK IK"]'
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

    elif "_R" and "tibia" in item:
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
        target.data_path = 'pose.bones["root"]["R_Leg FK IK"]'
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
        target.data_path = 'pose.bones["root"]["R_Leg FK IK"]'
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

    elif "footFK_L" in item:
        constraint_name = "Copy Rotation"
        constraint = bone.constraints.get(constraint_name)
        driver = constraint.driver_add("influence")
        driver2 = driver.driver
        driver2.type = 'AVERAGE'
        var = driver2.variables.new()
        var.name = 'var'
        target = var.targets[0]
        target.id = bpy.data.objects.get(rig)
        target.data_path = 'pose.bones["root"]["R_Leg FK IK"]'
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

r.set_mode('EDIT')

## CLEAN UP and Bug fixes

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

r.set_mode('POSE')

## hiding non-CTRL bones/Controls ##
arm = bpy.data.armatures[rig]
arm.collections.get("Deform").is_visible = False
arm.collections.get("ACCESSORY").is_visible = False
arm.collections.get("FK").is_visible = False
arm.collections.get("IK").is_visible = False
arm.collections.get("RBF").is_visible = False


## adding actions for clavicle and breast follow
## need to add this to the first script

# r.anim_action(rig, 'scapula_L', 'Clavicle_L_rotation_pose_1', 'Elbow_actions_L', 0, 20, 1.21591, 1.27059,transform_channel='LOCATION_Z')
# r.anim_action(rig, 'scapula_L', 'Clavicle_L_rotation_pose_2', 'Elbow_actions_L', 0, 40, 1.27059, 1.76191,transform_channel='LOCATION_Z')
# r.anim_action(rig, 'scapula_L', 'Clavicle forward_L', 'Elbow_actions_L', 0, 20, 0.041209, -0.182764,transform_channel='LOCATION_Y')
# r.anim_action(rig, 'scapula_L', 'Clavicle backward_L', 'Elbow_actions_L', 0, 20, 0.041209, 0.284233,transform_channel='LOCATION_Y')

# r.anim_action(rig, 'scapula_R', 'Clavicle_R_rotation_pose_1', 'Elbow_actions_R', 0, 20, 1.21591, 1.27059,transform_channel='LOCATION_Z')
# r.anim_action(rig, 'scapula_R', 'Clavicle_R_rotation_pose_2', 'Elbow_actions_R', 0, 40, 1.27059, 1.76191,transform_channel='LOCATION_Z')
# r.anim_action(rig, 'scapula_R', 'Clavicle forward_R', 'Elbow_actions_R', 0, 20, 0.041209, -0.182764,transform_channel='LOCATION_Y')
# r.anim_action(rig, 'scapula_R', 'Clavicle backward_R', 'Elbow_actions_R', 0, 20, 0.041209, 0.284233,transform_channel='LOCATION_Y')

# r.anim_action(rig, 'breast_L', 'breast_follow_up_L', 'Elbow_actions_L', 0, 20, 1.27059, 1.76191,transform_channel='LOCATION_Z')
# r.anim_action(rig, 'breast_L', 'breast_follow_down_L', 'Elbow_actions_L', 0, 20, 1.27059, 1.21591,transform_channel='LOCATION_Z')
# r.anim_action(rig, 'breast_L', 'breast_follow_back_L', 'Elbow_actions_L', 0, 20, 0.041209, 0.32314,transform_channel='LOCATION_Y')

# r.anim_action(rig, 'breast_R', 'breast_follow_up_R', 'Elbow_actions_R', 0, 20, 1.27059, 1.76191,transform_channel='LOCATION_Z')
# r.anim_action(rig, 'breast_R', 'breast_follow_down_R', 'Elbow_actions_R', 0, 20, 1.27059, 1.21591,transform_channel='LOCATION_Z')
# r.anim_action(rig, 'breast_R', 'breast_follow_back_R', 'Elbow_actions_R', 0, 20, 0.041209, 0.32314,transform_channel='LOCATION_Y')

# r.set_mode('OBJECT')
# r.remove_object_selection()
# r.object_selection(rig)
# bone = r.select_bone_as_active_pose(rig, 'scapula_L')
# action = bone.constraints.new(type='ACTION')
# target = bpy.data.objects['Elbow_actions_L']
# action.action = bpy.data.actions['Clavicle_l_rotation_pose_1']
# action.frame_end = 20
# action.frame_start = 0
# action.max = 1.21591
# action.min = 1.27059
# # action.mix_mode = 'LOCATION_Z'
# action.subtarget = ""
# action.target = target
# # action.use_eval = use_eval
# action.transform_channel = 'LOCATION_Z'
# # action.use_bone_object_action = 'Clavicle_1_rotation_pose_1'

sys.path.remove(module_dir)

