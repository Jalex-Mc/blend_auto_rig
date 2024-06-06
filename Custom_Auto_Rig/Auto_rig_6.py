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
bone["FK IK"] = 1.0
prop = bone.id_properties_ui("FK IK")
prop.update(soft_min=0, soft_max=1, min=0.0, max=1.0)

data_path = bone["FK IK"]
#correct data path for driver = pose.bones["Bone.001"]["FK IK"]
full_data_path = bpy.data.objects[rig].pose.bones["root"]["FK IK"]

### Creating Drivers for FK IK Switch ###

FK = ['humerus_FK_L', 'humerus_FK_R', 'forearm_FK_L', 'forearm_FK_R', 'armTwist_1_FK_L', 'armTwist_1_FK_R', 'armTwist_2_FK_L', 'armTwist_2_FK_R', 'armTwist_3_FK_L', 'armTwist_3_FK_R', 'hand_FK_L', 'hand_FK_R']
IK = ['humerus_IK_L', 'humerus_IK_R', 'forearm_IK_L', 'forearm_IK_R', 'armTwist_1_IK_L', 'armTwist_1_IK_R', 'armTwist_2_IK_L', 'armTwist_2_IK_R', 'armTwist_3_IK_L', 'armTwist_3_IK_R', 'hand_IK_L', 'hand_IK_R']
deform_list = ["humerus_L", "humerus_R", "forearm_L",  "forearm_R", "armTwist_1_L", "armTwist_1_R", "armTwist_2_L", "armTwist_2_R", "armTwist_3_L","armTwist_3_R", "hand_L", "hand_R"]

armature_obj = bpy.data.objects.get(rig)

for item in deform_list:
    # Copy Transforms.001 - IK
    # Copy Transforms - FK
    ##IK below - 
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
    target.data_path = 'pose.bones["root"]["FK IK"]'
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

    ##FK below - 
    constraint_name = "Copy Transforms"
    constraint = bone.constraints.get(constraint_name)
    driver = constraint.driver_add("influence")
    driver2 = driver.driver
    driver2.type = 'AVERAGE'
    var = driver2.variables.new()
    var.name = 'var'
    target = var.targets[0]
    target.id = bpy.data.objects.get(rig)
    target.data_path = 'pose.bones["root"]["FK IK"]'
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
bone = arm.edit_bones['kneePole_R']
bone.parent = None

r.set_mode('POSE')

## hiding non-CTRL bones/Controls ##
arm = bpy.data.armatures[rig]
arm.collections.get("Deform").is_visible = False
arm.collections.get("ACCESSORY").is_visible = False
arm.collections.get("FK").is_visible = False
arm.collections.get("IK").is_visible = False
arm.collections.get("RBF").is_visible = False


sys.path.remove(module_dir)
