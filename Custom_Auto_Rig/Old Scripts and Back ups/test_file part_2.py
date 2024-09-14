import bpy
from mathutils import Vector
import math
from collections import OrderedDict
import numpy as np
import time


def set_mode(a_mode):
    bpy.ops.object.mode_set(mode=a_mode)

def apply_scale(object):
    bpy.ops.object.mode_set(mode='OBJECT')
    remove_object_selection()
    object_selection(object)
    #have an option to select the object first
    bpy.ops.object.transform_apply(scale=True)

def select_bone_as_active_edit(rig_name, bone_name):
    bpy.ops.object.mode_set(mode='OBJECT')
    arm = bpy.data.armatures[rig_name]
    bpy.ops.object.mode_set(mode='EDIT')
    bone = arm.edit_bones[bone_name]
    arm.edit_bones.active = bone
    bone.select_head = True
    bone.select_tail = True

def remove_object_selection():
    bpy.ops.object.select_all(action='DESELECT')

def object_selection(object_name):
    obj = bpy.data.objects[object_name]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

def remove_edit_and_arm_selection(object_name):
    obj = bpy.data.objects[object_name]
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.armature.select_all(action='DESELECT')

def select_bone(bone_name, rig_name, tail, head):
    bpy.ops.object.mode_set(mode='EDIT')
    arm = bpy.data.armatures[rig_name]
    bone = arm.edit_bones[bone_name]
    arm.edit_bones.active = bone
    arm.edit_bones[bone_name].select_tail = tail
    arm.edit_bones[bone_name].select_head = head

def select_bone_as_active_pose(rig_name, bone_name):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.select_all(action='DESELECT')
    bone = bpy.context.active_object.pose.bones[bone_name]
    return bone

def remove_constraints(rig_name, bone_name):
    bone = select_bone_as_active_pose(rig_name, bone_name)
    for item in bone.constraints:
        bone.constraints.remove(item)


def degree_to_radians(degrees):
    return math.radians(degrees)

def bone_roll(rig_name, bone_name):
    remove_edit_and_arm_selection(rig_name)
    set_mode('OBJECT')
    remove_object_selection()
    object_selection(rig_name)
    set_mode('EDIT')
    arm = bpy.data.armatures[rig_name]
    bone = arm.edit_bones[bone_name]
    return bone.roll

def create_IK(rig_name, bone_name, chain_count, pole_angle, pole_subtarget, pole_target, subtarget, target):
    set_mode('OBJECT')
    remove_object_selection()
    object_selection(rig_name)
    bone = select_bone_as_active_pose(rig_name, bone_name)
    copy = bone.constraints.new(type='IK')
    target = bpy.data.objects[rig_name]
    copy.chain_count = chain_count
    copy.pole_angle = pole_angle
    copy.pole_subtarget = pole_subtarget
    copy.pole_target = target
    copy.subtarget = subtarget
    copy.target = target

def limit_rotation(rig_name, bone_name, order='AUTO',max_x=0.0,min_x=0.0,max_y=0.0, min_y=0.0,max_z=0.0,min_z=0.0,limit_x=False, limit_y=False, limit_z=False,transform_limit=False, owner_space='WORLD', target_space='WORLD'):
    bone = select_bone_as_active_pose(rig_name, bone_name)
    limit = bone.constraints.new(type='LIMIT_ROTATION')
    ## you need to convert degrees to radians to get the correct value.
    limit.owner_space = owner_space
    limit.target_space = target_space
    limit.euler_order = order
    limit.max_x = max_x
    limit.min_x = min_x
    limit.max_y = max_y
    limit.min_y = min_y
    limit.max_z = max_z
    limit.min_z = min_z
    limit.use_limit_x = limit_x
    limit.use_limit_y = limit_y
    limit.use_limit_z = limit_z
    limit.use_transform_limit = transform_limit


def limit_location(rig_name, bone_name,max_x=0.0,min_x=0.0,max_y=0.0, min_y=0.0,max_z=0.0,min_z=0.0,limit_x=False, limit_y=False, limit_z=False,transform_limit=False, owner_space='WORLD', target_space='WORLD'):
    bone = select_bone_as_active_pose(rig_name, bone_name)
    limit = bone.constraints.new(type='LIMIT_LOCATION')
    limit.owner_space = owner_space
    limit.target_space = target_space
    limit.max_x = max_x
    limit.min_x = min_x
    limit.max_y = max_y
    limit.min_y = min_y
    limit.max_z = max_z
    limit.min_z = min_z
    limit.use_max_x = limit_x
    limit.use_max_y = limit_y
    limit.use_max_z = limit_z
    limit.use_transform_limit = transform_limit

def limit_scale(rig_name, bone_name,max_x=0.0,min_x=0.0,max_y=0.0, min_y=0.0,max_z=0.0,min_z=0.0,limit_x=False, limit_y=False, limit_z=False,transform_limit=False, owner_space='WORLD', target_space='WORLD'):
    bone = select_bone_as_active_pose(rig_name, bone_name)
    limit = bone.constraints.new(type='LIMIT_SCALE')
    limit.owner_space = owner_space
    limit.target_space = target_space
    limit.max_x = max_x
    limit.min_x = min_x
    limit.max_y = max_y
    limit.min_y = min_y
    limit.max_z = max_z
    limit.min_z = min_z
    limit.use_max_x = limit_x
    limit.use_max_y = limit_y
    limit.use_max_z = limit_z
    limit.use_transform_limit = transform_limit

def copy_rotation(rig_name, bone_name, influence=1.0, euler_order='AUTO',invert_x=False,invert_y=False,invert_z=False,mix_mode='REPLACE',subtarget="",target='target',use_offset=False,use_x=False,use_y=False,use_z=False, target_space='WORLD', owner_space='WORLD'):
    set_mode('OBJECT')
    remove_object_selection()
    object_selection(rig_name)
    bone = select_bone_as_active_pose(rig_name, bone_name)
    copy = bone.constraints.new(type='COPY_ROTATION')
    target = bpy.data.objects[rig_name]
    copy.owner_space = owner_space
    copy.target_space = target_space
    copy.euler_order = euler_order
    copy.invert_x = invert_x
    copy.invert_y = invert_y
    copy.invert_z = invert_z
    copy.mix_mode = mix_mode
    copy.subtarget = subtarget
    copy.target = target
    copy.use_offset = use_offset
    copy.use_x = use_x
    copy.use_y = use_y
    copy.use_z = use_z
    copy.influence = influence


def copy_location(rig_name, bone_name, head_tail=0.0,invert_x=False, invert_y=False, invert_z=False, subtarget="",target='target',use_bbone_shape=False,use_offset=False,use_x=False,use_y=False,use_z=False,target_space='WORLD', owner_space='WORLD'):
    bone = select_bone_as_active_pose(rig_name, bone_name)
    copy = bone.constraints.new(type='COPY_LOCATION')
    target = bpy.data.objects[rig_name]
    copy.owner_space = owner_space
    copy.target_space = target_space
    copy.head_tail = head_tail
    copy.invert_x = invert_x
    copy.invert_y = invert_y
    copy.invert_z = invert_z
    copy.subtarget = subtarget
    copy.target = target
    copy.use_bbone_shape = use_bbone_shape
    copy.use_offset = use_offset
    copy.use_x = use_x
    copy.use_y = use_y
    copy.use_z = use_z

def copy_scale(rig_name, bone_name, power=1.0,subtarget="",target='target',use_add=False,use_make_uniform=False,use_offset=False,use_x=False,use_y=False,use_z=False,target_space='WORLD', owner_space='WORLD'):
    bone = select_bone_as_active_pose(rig_name, bone_name)
    copy = bone.constraints.new(type='COPY_SCALE')
    target = bpy.data.objects[rig_name]
    copy.owner_space = owner_space
    copy.target_space = target_space
    copy.power = power
    copy.subtarget = subtarget
    copy.target = target
    copy.use_add = use_add
    copy.use_make_uniform = use_make_uniform
    copy.use_offset = use_offset
    copy.use_x = use_x
    copy.use_y = use_y
    copy.use_z = use_z

def copy_transforms(rig_name, bone_name, influence, subtarget):
    bone = select_bone_as_active_pose(rig_name, bone_name)
    copy = bone.constraints.new(type='COPY_TRANSFORMS')
    target = bpy.data.objects[rig_name]
    copy.target = target
    copy.influence = influence
    copy.subtarget = subtarget

def damped_track(rig_name, bone_name, head_tail=0.0,subtarget="",target='target',track_axis='TRACK_X',use_bbone_shape=False):    
    bone = select_bone_as_active_pose(rig_name, bone_name)
    copy = bone.constraints.new(type='DAMPED_TRACK')
    target = bpy.data.objects[rig_name]
    copy.head_tail = head_tail
    copy.subtarget = subtarget
    copy.target = target
    copy.track_axis = track_axis
    copy.use_bbone_shape = use_bbone_shape

def transformation(
    rig_name,
    bone_name,
    from_max_x=0.0,
    from_max_x_rot=0.0,
    from_max_x_scale=0.0,
    from_max_y=0.0,
    from_max_y_rot=0.0,
    from_max_y_scale=0.0,
    from_max_z=0.0,
    from_max_z_rot=0.0,
    from_max_z_scale=0.0,
    from_min_x=0.0,
    from_min_x_rot=0.0,
    from_min_x_scale=0.0,
    from_min_y=0.0,
    from_min_y_rot=0.0,
    from_min_y_scale=0.0,
    from_min_z=0.0,
    from_min_z_rot=0.0,
    from_min_z_scale=0.0,
    from_rotation_mode="AUTO",
    map_from="LOCATION",
    map_to="LOCATION",
    map_to_x_from="X",
    map_to_y_from="Y",
    map_to_z_from="Z",
    mix_mode="ADD",
    mix_mode_rot="ADD",
    mix_mode_scale="REPLACE",
    subtarget="",
    target="target",
    to_euler_order="AUTO",
    to_max_x=0.0,
    to_max_x_rot=0.0,
    to_max_x_scale=0.0,
    to_max_y=0.0,
    to_max_y_rot=0.0,
    to_max_y_scale=0.0,
    to_max_z=0.0,
    to_max_z_rot=0.0,
    to_max_z_scale=0.0,
    to_min_x=0.0,
    to_min_x_rot=0.0,
    to_min_x_scale=0.0,
    to_min_y=0.0,
    to_min_y_rot=0.0,
    to_min_y_scale=0.0,
    to_min_z=0.0,
    to_min_z_rot=0.0,
    to_min_z_scale=0.0,
    use_motion_extrapolate=False,
    owner_space='WORLD',
    target_space='WORLD'
):
    bone = select_bone_as_active_pose(rig_name, bone_name)
    copy = bone.constraints.new(type="TRANSFORM")
    target = bpy.data.objects[rig_name]
    copy.owner_space = owner_space
    copy.target_space = target_space
    copy.from_max_x = from_max_x
    copy.from_max_x_rot = from_max_x_rot
    copy.from_max_x_scale = from_max_x_scale
    copy.from_max_y = from_max_y
    copy.from_max_y_rot = from_max_y_rot
    copy.from_max_y_scale = from_max_y_scale
    copy.from_max_z = from_max_z
    copy.from_max_z_rot = from_max_z_rot
    copy.from_max_z_scale = from_max_z_scale
    copy.from_min_x = from_min_x
    copy.from_min_x_rot = from_min_x_rot
    copy.from_min_x_scale = from_min_x_scale
    copy.from_min_y = from_min_y
    copy.from_min_y_rot = from_min_y_rot
    copy.from_min_y_scale = from_min_y_scale
    copy.from_min_z = from_min_z
    copy.from_min_z_rot = from_min_z_rot
    copy.from_min_z_scale = from_min_z_scale
    copy.from_rotation_mode = from_rotation_mode
    copy.map_from = map_from
    copy.map_to = map_to
    copy.map_to_x_from = map_to_x_from
    copy.map_to_y_from = map_to_y_from
    copy.map_to_z_from = map_to_z_from
    copy.mix_mode = mix_mode
    copy.mix_mode_rot = mix_mode_rot
    copy.mix_mode_scale = mix_mode_scale
    copy.subtarget = subtarget
    copy.target = target
    copy.to_euler_order = to_euler_order
    copy.to_max_x = to_max_x
    copy.to_max_x_rot = to_max_x_rot
    copy.to_max_x_scale = to_max_x_scale
    copy.to_max_y = to_max_y
    copy.to_max_y_rot = to_max_y_rot
    copy.to_max_y_scale = to_max_y_scale
    copy.to_max_z = to_max_z
    copy.to_max_z_rot = to_max_z_rot
    copy.to_max_z_scale = to_max_z_scale
    copy.to_min_x = to_min_x
    copy.to_min_x_rot = to_min_x_rot
    copy.to_min_x_scale = to_min_x_scale
    copy.to_min_y = to_min_y
    copy.to_min_y_rot = to_min_y_rot
    copy.to_min_y_scale = to_min_y_scale
    copy.to_min_z = to_min_z
    copy.to_min_z_rot = to_min_z_rot
    copy.to_min_z_scale = to_min_z_scale
    copy.use_motion_extrapolate = use_motion_extrapolate


def ik_properties(
    rig_name,
    bone_name,
    # lock_x=False,
    # lock_y=False,
    # lock_z=False,
    lock_ik_x=False,
    lock_ik_y=False,
    lock_ik_z=False,
    lock_location=(False, False, False),
    lock_rotation=(False, False, False),
    lock_rotation_w=False,
    lock_rotations_4d=False,
    ik_linear_weight=0.0,
    ik_max_x=0.0,
    ik_max_y=0.0,
    ik_max_z=0.0,
    ik_min_x=0.0,
    ik_min_y=0.0,
    ik_min_z=0.0,
    ik_rotation_weight=0.0,
    ik_stiffness_x=0.0,
    ik_stiffness_y=0.0,
    ik_stiffness_z=0.0,
    ik_stretch=0.0,
    use_ik_limit_x=False,
    use_ik_limit_y=False,
    use_ik_limit_z=False,
    use_ik_linear_control=False,
    use_ik_rotation_control=False,
):
    bone = select_bone_as_active_pose(rig_name, bone_name)
    bone.lock_ik_x = lock_ik_x
    bone.lock_ik_y = lock_ik_y
    bone.lock_ik_z = lock_ik_z
    # bone.lock_x = lock_x
    # bone.lock_y = lock_y
    # bone.lock_z = lock_z
    bone.lock_location = lock_location
    bone.lock_rotation = lock_rotation
    bone.lock_rotation_w = lock_rotation_w
    bone.lock_rotations_4d = lock_rotations_4d
    bone.ik_linear_weight = ik_linear_weight
    bone.ik_max_x = ik_max_x
    bone.ik_max_y = ik_max_y
    bone.ik_max_z = ik_max_z
    bone.ik_min_x = ik_min_x
    bone.ik_min_y = ik_min_y
    bone.ik_min_z = ik_min_z
    bone.ik_rotation_weight = ik_rotation_weight
    bone.ik_stiffness_x = ik_stiffness_x
    bone.ik_stiffness_y = ik_stiffness_y
    bone.ik_stiffness_z = ik_stiffness_z
    bone.ik_stretch = ik_stretch
    bone.use_ik_limit_x = use_ik_limit_x
    bone.use_ik_limit_y = use_ik_limit_y
    bone.use_ik_limit_z = use_ik_limit_z
    bone.use_ik_linear_control = use_ik_linear_control
    bone.use_ik_rotation_control = use_ik_rotation_control

def subdivide_bone(rig_name, bone_name, cut_amount):
    select_bone_as_active_edit(rig_name, bone_name)
    set_mode('OBJECT')
    bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
    set_mode('EDIT')
    bpy.ops.armature.subdivide(cut_amount)

def rig_bone_list(rig_name):
    arm = bpy.data.armatures[rig_name]
    bone_names = [bone.name for bone in arm.bones]
    return bone_names

def create_root_bone(rig_name):
    bpy.ops.object.mode_set(mode='OBJECT')
    remove_object_selection()
    bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
    bpy.ops.object.mode_set(mode='EDIT')
    remove_edit_and_arm_selection(rig_name)
    arm = bpy.data.armatures[rig_name]
    bone = arm.edit_bones.new("ROOT")
    bone.head = (0, 0, 0)  # Starting position
    bone.tail = (0, 0, 0.185127)  # Ending position

def parent_bone(rig_name, child_bone, parent_bone, offset):
    set_mode('OBJECT')
    remove_object_selection()
    object_selection(rig_name)
    set_mode('EDIT')
    arm = bpy.data.armatures[rig_name]
    bone = arm.edit_bones[child_bone]
    bone.parent = arm.edit_bones[parent_bone]
    bone.use_connect = offset

def bone_length(bone_name, rig_name):
    bpy.ops.object.mode_set(mode='OBJECT')
    remove_object_selection()
    object_selection(rig_name)
    set_mode('EDIT')
    arm = bpy.data.armatures[rig_name]
    bone = arm.edit_bones[bone_name]
    return bone.length

def change_bone_length(bone_name, rig_name, length):
    set_mode('OBJECT')
    remove_object_selection()
    object_selection(rig_name)
    set_mode('EDIT')
    arm = bpy.data.armatures[rig_name]
    bone = arm.edit_bones[bone_name]
    bone.length = length

def lock_location(rig_name, bone_name, x=False, y=False, z=False):
    set_mode('OBJECT')
    remove_object_selection()
    bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
    bpy.ops.object.mode_set(mode='POSE')
    bone = bpy.context.active_object.pose.bones[bone_name]
    bone.lock_location[0] = x
    bone.lock_location[1] = y
    bone.lock_location[2] = z

def lock_rotation(rig_name, bone_name, w=False, x=False, y=False, z=False):
    set_mode('OBJECT')
    remove_object_selection()
    bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
    bpy.ops.object.mode_set(mode='POSE')
    bone = bpy.context.active_object.pose.bones[bone_name]
    if bone.rotation_mode == 'QUATERNION':
        bone.lock_rotation[0] = x
        bone.lock_rotation[1] = y
        bone.lock_rotation[2] = z
        bone.lock_rotation_w = w
    else:
        bone.lock_rotation[0] = x
        bone.lock_rotation[1] = y
        bone.lock_rotation[2] = z

def lock_scale(rig_name, bone_name, x=False, y=False, z=False):
    set_mode('OBJECT')
    remove_object_selection()
    bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
    bpy.ops.object.mode_set(mode='POSE')
    bone = bpy.context.active_object.pose.bones[bone_name]
    bone.lock_scale[0] = x
    bone.lock_scale[1] = y
    bone.lock_scale[2] = z

def eular_change(rig_name, bone_name, rotation):
    set_mode('OBJECT')
    remove_object_selection()
    object_selection(rig_name)
    bpy.ops.object.mode_set(mode='POSE')
    bone = bpy.context.active_object.pose.bones[bone_name]
    bone.rotation_mode = rotation

def renamer(rig_name, bone_name, new_bone_name):
    set_mode('OBJECT')
    remove_edit_and_arm_selection(rig_name)
    set_mode('OBJECT')
    remove_object_selection()
    bones_list = bpy.data.armatures[rig_name].bones
    for item in bones_list:
        if item.name == bone_name:
            print(item.name)
            item.name = new_bone_name
    remove_edit_and_arm_selection(rig_name)

# duplicates bone
def duplicate_bone(rig_name, bone_name, new_bone_name):
    remove_edit_and_arm_selection(rig_name)
    set_mode('OBJECT')
    object_selection(rig_name)
    set_mode('EDIT')
    arm = bpy.data.objects[rig_name]
    bone = arm.data.edit_bones[bone_name]
    bone.select=True
    bone.select_head = True
    bone.select_tail = True
    arm.data.edit_bones.active = bone
    bpy.ops.armature.duplicate()
    new_bone = bpy.context.selected_editable_bones
    new_bone[0].name = new_bone_name


# get's bone's head and tails location
def get_bone_location(rig_name, bone_name):
    bpy.ops.object.mode_set(mode='POSE')
    arm = bpy.data.objects[rig_name]
    bone = arm.pose.bones[bone_name]
    bone.bone.select = True
    head = bone.head
    tail = bone.tail
    return head, tail

# this takes a bone's position and convert it to world
def move_bone_world_location(rig_name, bone_name, head_pos, tail_pos):
    bpy.ops.object.mode_set(mode='EDIT')
    arm = bpy.data.objects[rig_name]
    bone = arm.data.edit_bones[bone_name]
    
    matrix_world_inv = arm.matrix_world.inverted()

    if head_pos:
        head_pos = head_pos
        bone.head = matrix_world_inv @ head_pos
    if tail_pos:
        tail_pos = tail_pos
        bone.tail = matrix_world_inv @ tail_pos


# takes a bone's head and tail's local location and return the world location.
def bone_global_location(pos_1, pos_2):
    # gets the location of where the tip will extrude too
    bpy.context.view_layer.objects.active = bpy.data.objects[pos_1]
    selected_object = bpy.context.active_object
    global_position_1 = selected_object.matrix_world.translation
    # to set the active object
    # bpy.data.objects["FootTip_positioner_L"].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[pos_2]
    selected_object = bpy.context.active_object
    global_position_2 = selected_object.matrix_world.translation
    return global_position_1, global_position_2

def bone_global_locations(rig_name, bone_name):
    remove_edit_and_arm_selection(rig_name)
    bpy.ops.object.mode_set(mode='POSE')
    arm = bpy.data.objects[rig_name]
    bone = arm.pose.bones[bone_name]
    bone.bone.select = True
    head = bone.head
    tail = bone.tail
    set_mode('EDIT')
    matrix_world_inv = arm.matrix_world.inverted()
    global_position_1 = matrix_world_inv @ head
    global_position_2 = matrix_world_inv @ tail
    return global_position_1, global_position_2

def object_location(object, x=0, y=0, z=0, alter=False):
    object_as_object = bpy.data.objects[object]
    local_pos = object_as_object.location
    global_pos = object_as_object.matrix_world @ local_pos
    if alter == True:
        if x != 0:
            local_pos = object_as_object.location
            to_loc = np.array(object_as_object.location)
            object_as_object.location.x += x
            altered_pos = np.array(object_as_object.location)
            global_alt = object_as_object.matrix_world @ altered_pos
            return to_loc, global_pos, altered_pos, global_alt

        if y != 0:
            local_pos = object_as_object.location
            to_loc = np.array(object_as_object.location)
            object_as_object.location.y += y
            altered_pos = np.array(object_as_object.location)
            global_alt = object_as_object.matrix_world @ local_pos
            return to_loc, global_pos, altered_pos, global_alt

        if z != 0:
            object_as_object.location.z += z
            altered_pos = object_as_object.location
            global_alt = object_as_object.matrix_world @ altered_pos
            return local_pos, global_pos, altered_pos, global_alt

    return local_pos, global_pos

# creates a bone at the position given, if you want to have it duplicate, pass in the
# global pos of the bone head and tail. pos_1 is heads.
def new_bone_creation_using_duplication(pos_1, pos_2, bone_name, new_bone_name, rig_name, parent, parent_offset, roll, keep_selection=True):
    bpy.ops.object.mode_set(mode='OBJECT')
    remove_object_selection()
    bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
    bpy.ops.object.mode_set(mode='EDIT')
    remove_edit_and_arm_selection(rig_name)
    # after here is the issue
    select_bone_as_active_edit(rig_name, bone_name)
    arm = bpy.data.armatures[rig_name]
    bone = arm.edit_bones.new(new_bone_name)
    bone.roll = roll

    if parent == None:
        pass
    else:
        arm.edit_bones[new_bone_name].use_connect = parent_offset
        arm.edit_bones[new_bone_name].parent = arm.edit_bones[parent]

    # Set the head and tail positions of the bone
    bone.head = pos_1  # Starting position
    bone.tail = pos_2  # Ending position
    remove_edit_and_arm_selection(rig_name)
    if keep_selection == True:
        new_bone = bpy.context.visible_bones
        # print(new_bone[-1].name)
        select_bone_as_active_edit(rig_name, new_bone[-1].name)
    else:
        remove_edit_and_arm_selection(rig_name)

def new_bone_creation(pos_1, pos_2, new_bone_name, rig_name, parent, parent_offset, roll):
    bpy.ops.object.mode_set(mode='OBJECT')
    remove_object_selection()
    bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
    bpy.ops.object.mode_set(mode='EDIT')
    remove_edit_and_arm_selection(rig_name)
    #here is the issue
    arm = bpy.data.armatures[rig_name]
    bone = arm.edit_bones.new(new_bone_name)
    bone.roll = roll
    # Set the head and tail positions of the bone
    bone.head = pos_1  # Starting position
    bone.tail = pos_2  # Ending position

    if parent == None:
        pass
    else:
        pass
        arm.edit_bones[new_bone_name].use_connect = parent_offset
        arm.edit_bones[new_bone_name].parent = arm.edit_bones[parent]
    remove_edit_and_arm_selection(rig_name)


# extrudes from a bone, oarameters to select which head to extrude from and the axis
def extrude_out(bone_name, new_bone_name, rig_name, head, tail, value, bone_length, roll):
    bpy.ops.object.mode_set(mode='OBJECT')
    remove_object_selection()
    bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
    bpy.ops.object.mode_set(mode='EDIT')
    remove_edit_and_arm_selection(rig_name)
    arm = bpy.data.armatures[rig_name]
    bone = arm.edit_bones[bone_name]
    bone.select_head = head
    bone.select_tail = tail
    bpy.ops.armature.extrude_move(TRANSFORM_OT_translate={"value": value})
    bpy.context.active_object.data.edit_bones[-1].name = new_bone_name
    new_bone = arm.edit_bones[new_bone_name]
    new_bone.length = bone_length
    new_bone.roll = roll
    select_bone(new_bone_name, rig_name, True, True)

# might just use my function duplicate_bone instead of this methof
def duplication_chain(rig_name, bone_name, new_bone_name, parent='', parent_offset = True, roll=0):
    #get's bone's local heads and tails location
    head_loc, tail_loc = get_bone_location(rig_name, bone_name)
    #get's bone's world locations
    head_global, tail_global = bone_global_location(head_loc, tail_loc)
    #duplicate bone and give it the same location of the bone_name parameter
    new_bone_creation(head_global, tail_global, new_bone_name, rig_name, parent, parent_offset, roll) 

def flip_bone(rig_name, bone_name):
    set_mode('EDIT')
    remove_edit_and_arm_selection(rig_name)
    set_mode('OBJECT')
    arm = bpy.data.armatures[rig_name]
    bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
    set_mode('EDIT')
    bone = arm.edit_bones[bone_name]
    arm.edit_bones.active = bone
    arm.edit_bones.active.select = True
    bone.select_head = True
    bone.select_tail = True
    bpy.ops.armature.switch_direction()

def create_bone_collections(rig_name, bones_to_assign):
    remove_edit_and_arm_selection(rig_name)
    set_mode('OBJECT')
    remove_object_selection()
    object_selection(rig_name)
    arm = bpy.context.object.data

    for collection_name, value in bones_to_assign.items():
        bone_coll = arm.collections.new(collection_name)

        for bone_coll in arm.collections:
            print(f"collection: {bone_coll.name}")
        for item in value:
            bone_coll.assign(arm.bones[item])

bones_to_assign = {'firstBones': ['Bone', 'Bone.001', 'Bone.002', 'Bone.003'], 'secondBones': ['Bone.004', 'Bone.005', 'Bone.006', 'Bone.007']}


def duplicate_bones(rig_name, bone_name, new_bone_name, parent, parent_offset, roll, keep_selection):
    pos_1, pos_2 = bone_global_locations(rig_name, bone_name)
    new_bone_creation_using_duplication(pos_1, pos_2, bone_name, new_bone_name, rig, parent, parent_offset, roll, keep_selection)

def move_head_or_tail(bone_name, rig_name, head, tail, value_1, value_2):
    set_mode('OBJECT')
    remove_object_selection()
    object_selection(rig_name)
    set_mode('EDIT')
    arm = bpy.data.armatures[rig_name]
    bone = arm.edit_bones[bone_name]

    if head == True:
        bone.head = value_1
    if tail == True:
        bone.tail = value_2

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

################################
######### ARM ################

# head, tail = bone_global_locations(rig, 'hand_L')
# new_bone_creation(head, tail, 'handIK_CTRL_L', rig, 'ROOT', False, degree_to_radians(140))

# head, tail = bone_global_locations(rig, 'hand_R')
# new_bone_creation(head, tail, 'handIK_CTRL_R', rig, 'ROOT', False, degree_to_radians(-140))

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


for index, item in enumerate(left_arm_IK_bones):
    if 'hand' in item:
        left_arm_IK_bones[index] = f"{item.split('_')[0]}IK_CTRL_L"
    else:
        left_arm_IK_bones[index] = f"{item.split('_')[0]}_IK_L"

for index, item in enumerate(left_arm_FK_bones):
    left_arm_FK_bones[index] = f"{item.split('_')[0]}_FK_L"

for index, item in enumerate(right_arm_FK_bones):
    if 'hand' in item:
        right_arm_IK_bones[index] = f"{item.split('_')[0]}IK_CTRL_R"
    else:
        right_arm_IK_bones[index] = f"{item.split('_')[0]}_IK_R"

for index, item in enumerate(right_arm_FK_bones):
    right_arm_FK_bones[index] = f"{item.split('_')[0]}_FK_R"


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

create_IK(rig, 'forearm_IK_L', 2, degree_to_radians(-80), 'elbowPole_L', rig, 'handIK_CTRL_L', rig)
create_IK(rig, 'forearm_IK_R', 2, degree_to_radians(-80), 'elbowPole_R', rig, 'handIK_CTRL_R', rig)

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

