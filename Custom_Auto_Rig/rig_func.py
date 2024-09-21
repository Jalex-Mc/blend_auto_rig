import bpy
from mathutils import Vector
import math
import numpy as np


class Rigging_Functions:
    
    def __init__(self):
        pass

    @staticmethod
    def set_mode(a_mode):
        bpy.ops.object.mode_set(mode=a_mode)
    
    def remove_object_selection(self):
        bpy.ops.object.select_all(action='DESELECT')

    def apply_scale(self, object):
        bpy.ops.object.mode_set(mode='OBJECT')
        self.remove_object_selection()
        self.object_selection(object)
        bpy.ops.object.transform_apply(scale=True)

    @staticmethod
    def select_bone_as_active_edit(rig_name, bone_name):
        bpy.ops.object.mode_set(mode='OBJECT')
        arm = bpy.data.armatures[rig_name]
        bpy.ops.object.mode_set(mode='EDIT')
        bone = arm.edit_bones[bone_name]
        arm.edit_bones.active = bone
        bone.select_head = True
        bone.select_tail = True
        
    @staticmethod
    def object_selection(object_name):
        obj = bpy.data.objects[object_name]
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

    @staticmethod
    def remove_edit_and_arm_selection(object_name):
        obj = bpy.data.objects[object_name]
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.select_all(action='DESELECT')
    
    @staticmethod
    def select_bone(bone_name, rig_name, tail, head):
        bpy.ops.object.mode_set(mode='EDIT')
        arm = bpy.data.armatures[rig_name]
        bone = arm.edit_bones[bone_name]
        arm.edit_bones.active = bone
        arm.edit_bones[bone_name].select_tail = tail
        arm.edit_bones[bone_name].select_head = head

    @staticmethod
    def select_bone_as_active_pose(rig_name, bone_name):
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='DESELECT')
        bone = bpy.context.active_object.pose.bones[bone_name]
        return bone

    def remove_constraints(self, rig_name, bone_name):
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
        for item in bone.constraints:
            bone.constraints.remove(item)

    @staticmethod
    def degree_to_radians(degrees):
        return math.radians(degrees)

    def bone_roll(self, rig_name, bone_name):
        self.remove_edit_and_arm_selection(rig_name)
        self.set_mode('OBJECT')
        self.remove_object_selection()
        self.object_selection(rig_name)
        self.set_mode('EDIT')
        arm = bpy.data.armatures[rig_name]
        bone = arm.edit_bones[bone_name]
        return bone.roll

    def create_IK(self, rig_name, bone_name, chain_count, pole_angle, pole_subtarget, pole_target, subtarget, target):
        self.set_mode('OBJECT')
        self.remove_object_selection()
        self.object_selection(rig_name)
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
        copy = bone.constraints.new(type='IK')
        target = bpy.data.objects[rig_name]
        copy.chain_count = chain_count
        copy.pole_angle = pole_angle
        copy.pole_subtarget = pole_subtarget
        copy.pole_target = target
        copy.subtarget = subtarget
        copy.target = target

    def limit_rotation(self, rig_name, bone_name, order='AUTO',max_x=0.0,min_x=0.0,max_y=0.0, min_y=0.0,max_z=0.0,min_z=0.0,limit_x=False, limit_y=False, limit_z=False,transform_limit=False, owner_space='WORLD', target_space='WORLD'):
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
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

        
    def limit_location(self, rig_name, bone_name,max_x=0.0,min_x=0.0,max_y=0.0, min_y=0.0,max_z=0.0,min_z=0.0,limit_x=False, limit_y=False, limit_z=False,transform_limit=False, owner_space='WORLD', target_space='WORLD'):
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
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

    def limit_scale(self, rig_name, bone_name,max_x=0.0,min_x=0.0,max_y=0.0, min_y=0.0,max_z=0.0,min_z=0.0,limit_x=False, limit_y=False, limit_z=False,transform_limit=False, owner_space='WORLD', target_space='WORLD'):
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
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

    def copy_rotation(self, rig_name, bone_name, influence=1.0, euler_order='AUTO',invert_x=False,invert_y=False,invert_z=False,mix_mode='REPLACE',subtarget="",target='target',use_offset=False,use_x=False,use_y=False,use_z=False, target_space='WORLD', owner_space='WORLD'):
        self.set_mode('OBJECT')
        self.remove_object_selection()
        self.object_selection(rig_name)
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
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

    def copy_location(self, rig_name, bone_name, head_tail=0.0,invert_x=False, invert_y=False, invert_z=False, subtarget="",target='target',use_bbone_shape=False,use_offset=False,use_x=False,use_y=False,use_z=False,target_space='WORLD', owner_space='WORLD'):
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
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
        
    def copy_scale(self, rig_name, bone_name, power=1.0,subtarget="",target='target',use_add=False,use_make_uniform=False,use_offset=False,use_x=False,use_y=False,use_z=False,target_space='WORLD', owner_space='WORLD'):
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
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


    def copy_transforms(self, rig_name, bone_name, influence, subtarget):
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
        copy = bone.constraints.new(type='COPY_TRANSFORMS')
        # target = bpy.data.objects[rig_name]
        copy.target = bpy.data.objects[rig_name]
        # print(f'{copy}{influence}{subtarget}{target}')
        copy.influence = influence
        copy.subtarget = subtarget

    def damped_track(self, rig_name, bone_name, head_tail=0.0,subtarget="",target='target',track_axis='TRACK_X',use_bbone_shape=False):    
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
        copy = bone.constraints.new(type='DAMPED_TRACK')
        target = bpy.data.objects[rig_name]
        copy.head_tail = head_tail
        copy.subtarget = subtarget
        copy.target = target
        copy.track_axis = track_axis
        copy.use_bbone_shape = use_bbone_shape

    def transformation(
        self,
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
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
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
        self,
        rig_name,
        bone_name,
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
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
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

    def subdivide_bone(self, rig_name, bone_name, cut_amount):
        self.select_bone_as_active_edit(rig_name, bone_name)
        self.set_mode('OBJECT')
        bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
        self.set_mode('EDIT')
        bpy.ops.armature.subdivide(number_cuts=(cut_amount, 20))

    @staticmethod
    def rig_bone_list(rig_name):
        arm = bpy.data.armatures[rig_name]
        bone_names = [bone.name for bone in arm.bones]
        return bone_names

    def create_root_bone(self, rig_name):
        bpy.ops.object.mode_set(mode='OBJECT')
        self.remove_object_selection()
        bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
        bpy.ops.object.mode_set(mode='EDIT')
        self.remove_edit_and_arm_selection(rig_name)
        arm = bpy.data.armatures[rig_name]
        bone = arm.edit_bones.new("root")
        bone.head = (0, 0, 0)  # Starting position
        bone.tail = (0, 0, 0.185127)  # Ending position
    
    def parent_bone(self, rig_name, child_bone, parent_bone, offset):
        self.set_mode('OBJECT')
        self.remove_object_selection()
        self.object_selection(rig_name)
        self.set_mode('EDIT')
        arm = bpy.data.armatures[rig_name]
        bone = arm.edit_bones[child_bone]
        bone.use_connect = offset
        bone.parent = arm.edit_bones[parent_bone]
        
    def bone_length(self, bone_name, rig_name):
        bpy.ops.object.mode_set(mode='OBJECT')
        self.remove_object_selection()
        self.object_selection(rig_name)
        self.set_mode('EDIT')
        arm = bpy.data.armatures[rig_name]
        bone = arm.edit_bones[bone_name]
        return bone.length

    def change_bone_length(self, bone_name, rig_name, length):
        self.set_mode('OBJECT')
        self.remove_object_selection()
        self.object_selection(rig_name)
        self.set_mode('EDIT')
        arm = bpy.data.armatures[rig_name]
        bone = arm.edit_bones[bone_name]
        bone.length = length

    def lock_location(self, rig_name, bone_name, x=False, y=False, z=False):
        self.set_mode('OBJECT')
        self.remove_object_selection()
        bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
        bpy.ops.object.mode_set(mode='POSE')
        bone = bpy.context.active_object.pose.bones[bone_name]
        bone.lock_location[0] = x
        bone.lock_location[1] = y
        bone.lock_location[2] = z
        
    def lock_rotation(self, rig_name, bone_name, w=False, x=False, y=False, z=False):
        self.set_mode('OBJECT')
        self.remove_object_selection()
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

    def lock_scale(self, rig_name, bone_name, x=False, y=False, z=False):
        self.set_mode('OBJECT')
        self.remove_object_selection()
        bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
        bpy.ops.object.mode_set(mode='POSE')
        bone = bpy.context.active_object.pose.bones[bone_name]
        bone.lock_scale[0] = x
        bone.lock_scale[1] = y
        bone.lock_scale[2] = z

    def eular_change(self, rig_name, bone_name, rotation):
        self.set_mode('OBJECT')
        self.remove_object_selection()
        self.object_selection(rig_name)
        bpy.ops.object.mode_set(mode='POSE')
        bone = bpy.context.active_object.pose.bones[bone_name]
        bone.rotation_mode = rotation

    def renamer(self, rig_name, bone_name, new_bone_name):
        self.set_mode('OBJECT')
        self.remove_edit_and_arm_selection(rig_name)
        self.set_mode('OBJECT')
        self.remove_object_selection()
        bones_list = bpy.data.armatures[rig_name].bones
        for item in bones_list:
            if item.name == bone_name:
                print(item.name)
                item.name = new_bone_name
        self.remove_edit_and_arm_selection(rig_name)

    # duplicates bone
    def duplicate_bone(self, rig_name, bone_name, new_bone_name):
        self.remove_edit_and_arm_selection(rig_name)
        self.set_mode('OBJECT')
        self.object_selection(rig_name)
        self.set_mode('EDIT')
        # self.select_bone_as_active_edit(rig_name, bone_name)
        arm = bpy.data.objects[rig_name]
        # bone = arm.data.edit_bones[bone_name]
        bone = arm.data.edit_bones.get(bone_name)
        bone.select=True
        bone.select_head = True
        bone.select_tail = True
        arm.data.edit_bones.active = bone
        # arm.data.edit_bones.active = bone
        bpy.ops.armature.duplicate()
        new_bone = bpy.context.selected_editable_bones
        new_bone[0].name = new_bone_name

    # get's bone's head and tails location
    @staticmethod
    def get_bone_location(rig_name, bone_name):
        bpy.ops.object.mode_set(mode='POSE')
        arm = bpy.data.objects[rig_name]
        bone = arm.pose.bones[bone_name]
        # print(bone.head)
        # print(bone.tail)
        bone.bone.select = True
        head = bone.head
        tail = bone.tail
        return head, tail

    # this takes a bone's position and convert it to world
    @staticmethod
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
    @staticmethod
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

    def bone_global_locations(self, rig_name, bone_name):
        self.set_mode('OBJECT')
        self.remove_edit_and_arm_selection(rig_name)
        self.object_selection(rig_name)
        bpy.ops.object.mode_set(mode='POSE')
        arm = bpy.data.objects[rig_name]
        bone = arm.pose.bones[bone_name]
        # print(bone.head)
        # print(bone.tail)
        bone.bone.select = True
        head = bone.head
        tail = bone.tail
        self.set_mode('EDIT')
        # arm = bpy.data.armatures[rig_name]
        # bone = arm.edit_bones[bone_name]
        matrix_world_inv = arm.matrix_world.inverted()
        global_position_1 = matrix_world_inv @ head
        global_position_2 = matrix_world_inv @ tail
        return global_position_1, global_position_2

    @staticmethod
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
    def new_bone_creation_using_duplication(self, pos_1, pos_2, bone_name, new_bone_name, rig_name, parent, parent_offset, roll, keep_selection=True):
        bpy.ops.object.mode_set(mode='OBJECT')
        self.remove_object_selection()
        bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
        bpy.ops.object.mode_set(mode='EDIT')
        self.remove_edit_and_arm_selection(rig_name)
        # after here is the issue
        self.select_bone_as_active_edit(rig_name, bone_name)
        arm = bpy.data.armatures[rig_name]
        bone = arm.edit_bones.new(new_bone_name)
        bone.roll = roll
        # print(pos_1)
        # print(pos_2)
        if parent == None:
            pass
        else:
            arm.edit_bones[new_bone_name].use_connect = parent_offset
            arm.edit_bones[new_bone_name].parent = arm.edit_bones[parent]

        # Set the head and tail positions of the bone
        bone.head = pos_1  # Starting position
        bone.tail = pos_2  # Ending position
        self.remove_edit_and_arm_selection(rig_name)
        if keep_selection == True:
            new_bone = bpy.context.visible_bones
            # print(new_bone[-1].name)
            self.select_bone_as_active_edit(rig_name, new_bone[-1].name)
        else:
            self.remove_edit_and_arm_selection(rig_name)

    def new_bone_creation(self, pos_1, pos_2, new_bone_name, rig_name, parent, parent_offset, roll):
        bpy.ops.object.mode_set(mode='OBJECT')
        self.remove_object_selection()
        bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
        bpy.ops.object.mode_set(mode='EDIT')
        self.remove_edit_and_arm_selection(rig_name)
        #here is the issue
        arm = bpy.data.armatures[rig_name]
        bone = arm.edit_bones.new(new_bone_name)
        bone.roll = roll
        # Set the head and tail positions of the bone
        bone.head = pos_1  # Starting position
        bone.tail = pos_2  # Ending position
        # print(pos_1)
        # print(pos_2)
        # print(parent)
        # print(parent_offset)
        if parent == None:
            pass
        else:
            pass
            arm.edit_bones[new_bone_name].use_connect = parent_offset
            arm.edit_bones[new_bone_name].parent = arm.edit_bones[parent]
        self.remove_edit_and_arm_selection(rig_name)
        # print("Done")



    #extrudes from a bone, oarameters to select which head to extrude from and the axis
    def extrude_out(self, bone_name, new_bone_name, rig_name, head, tail, value, bone_length, roll):
        bpy.ops.object.mode_set(mode='OBJECT')
        self.remove_object_selection()
        bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
        bpy.ops.object.mode_set(mode='EDIT')
        self.remove_edit_and_arm_selection(rig_name)
        arm = bpy.data.armatures[rig_name]
        bone = arm.edit_bones[bone_name]
        bone.select_head = head
        bone.select_tail = tail
        bpy.ops.armature.extrude_move(TRANSFORM_OT_translate={"value": value})
        bpy.context.active_object.data.edit_bones[-1].name = new_bone_name
        new_bone = arm.edit_bones[new_bone_name]
        new_bone.length = bone_length
        new_bone.roll = roll
        self.select_bone(new_bone_name, rig_name, True, True)

    # might just use my function duplicate_bone instead of this methof
    def duplication_chain(self, rig_name, bone_name, new_bone_name, parent='', parent_offset = True, roll=0):
        #get's bone's local heads and tails location
        head_loc, tail_loc = self.get_bone_location(rig_name, bone_name)
        #get's bone's world locations
        head_global, tail_global = self.bone_global_location(head_loc, tail_loc)
        #duplicate bone and give it the same location of the bone_name parameter
        self.new_bone_creation(head_global, tail_global, new_bone_name, rig_name, parent, parent_offset, roll) 

    def flip_bone(self, rig_name, bone_name):
        self.set_mode('EDIT')
        self.remove_edit_and_arm_selection(rig_name)
        self.set_mode('OBJECT')
        arm = bpy.data.armatures[rig_name]
        bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
        self.set_mode('EDIT')
        bone = arm.edit_bones[bone_name]
        arm.edit_bones.active = bone
        arm.edit_bones.active.select = True
        bone.select_head = True
        bone.select_tail = True
        bpy.ops.armature.switch_direction()

    def create_bone_collections(self, rig_name, bones_to_assign):
        self.remove_edit_and_arm_selection(rig_name)
        self.set_mode('OBJECT')
        self.remove_object_selection()
        self.object_selection(rig_name)
        arm = bpy.context.object.data

        for collection_name, value in bones_to_assign.items():
            bone_coll = arm.collections.new(collection_name)

            for bone_coll in arm.collections:
                print(f"collection: {bone_coll.name}")
            for item in value:
                bone_coll.assign(arm.bones[item])

    bones_to_assign = {'firstBones': ['Bone', 'Bone.001', 'Bone.002', 'Bone.003'], 'secondBones': ['Bone.004', 'Bone.005', 'Bone.006', 'Bone.007']}


    def duplicate_bones(self, rig_name, bone_name, new_bone_name, parent, parent_offset, roll, keep_selection):
        pos_1, pos_2 = self.bone_global_locations(rig_name, bone_name)
        self.new_bone_creation_using_duplication(pos_1, pos_2, bone_name, new_bone_name, rig_name, parent, parent_offset, roll, keep_selection)

    def move_head_or_tail(self, bone_name, rig_name, head, tail, value_1, value_2):
        self.set_mode('OBJECT')
        self.remove_object_selection()
        self.object_selection(rig_name)
        self.set_mode('EDIT')
        arm = bpy.data.armatures[rig_name]
        bone = arm.edit_bones[bone_name]

        if head == True:
            bone.head = value_1
        if tail == True:
            bone.tail = value_2

    def copy_scale(self, rig_name, bone_name, power=1.0,subtarget="",target='target',use_add=False,use_make_uniform=False,use_offset=False,use_x=False,use_y=False,use_z=False,target_space='WORLD', owner_space='WORLD'):
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
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
        
    def anim_action(self, rig_name, bone_name, action, target_name, frame_start, frame_end, min, max, mix_mode="AFTER_FULL", subtarget="", use_eval_time=False, transform_channel='ROTATION_X', bone_action=False):
        self.set_mode('OBJECT')
        self.remove_object_selection()
        self.object_selection(rig_name)
        bone = self.select_bone_as_active_pose(rig_name, bone_name)
        action_cons = bone.constraints.new(type='ACTION')
        target = bpy.data.objects[target_name]
        action_cons.action = bpy.data.actions[action]
        action_cons.frame_end = frame_end
        action_cons.frame_start = frame_start
        action_cons.max = max
        action_cons.min = min
        action_cons.mix_mode = mix_mode
        action_cons.subtarget = subtarget
        action_cons.target = target
        action_cons.use_eval_time = use_eval_time
        action_cons.transform_channel = transform_channel
        action_cons.use_bone_object_action = bone_action

    # @staticmethod
    # def list_of_shapekeys(object_with_shapes):
    #     # obj = bpy.data.objects[object_with_shapes]
    #     obj.select_set(True)
    #     # bpy.context.view_layer.objects.active = obj
    #     # bpy.context.view_layer.objects.active = obj
    #     print("FUCKING SHIT")
    #     # print(obj)
    #     # obj = self.object_selection(object_with_shapes)
    #     # print(obj)
    #     # shape_keys = obj.shape_keys.key_blocks
    #     print(obj.__dir__())
    #     # shape_key_names = [key.name for key in shape_keys]
    #     # return shape_key_names
    
    def shapes_target_bones(self, shape_key_list):

        bone_drivers = {"Arms_up": ["humerus", 4],
        "Arms_down": ["humerus", 2],
        "Arms_forward": ["humerus", 3],
        "Arms_back": ["humerus", 1],
        "Knees_up": ["alt", 24],
        "Knees_up_butt": ["femur", 24],
        "knees_up_spine_1": ["femur", 24],
        "Knees_up_pelvis": ["femur", 24],
        "T-pose": ["femur", 28],
        "Leg_spread": ["femur", 25],
        "Leg_spread_front": ["kneeBendDeform", 27],
        "Leg_back": ["femur", 26],
        "Head_up": ["alt", 23],
        "Head_down": ["alt",18],
        "Head_tilt": ["alt", {'left':19}, {'right':20}],
        "Head_turn": ["alt", {'left':21}, {'right':22}],
        "bend_back": ["alt", 6],
        "bend_forward": ["alt", 7],
        "bend_right": ["alt", 9],
        "bend_left": ["alt", 8],
        "turn_left": ["alt", 33],
        "turn_right": ["alt", 34],
        "fist": ["alt",{'left':12}, {'right':13}],
        "fingers_bent_up": None,
        "fingers_spread": None,
        "Elbow": ["alt",{'left':10},{'right':11}],
        "tiptoes": ["alt",{'left':29},{'right':30}],
        "foot_bend_in": ["alt", {'left':14}, {'right':15}],
        "foot_bend_out": ["alt", {'left':16}, {'right':17}],
        "toes_bend": None,
        "toes_together": None,
        "toes_spread": None,
        "toes_curl": ["alt", {'left':31}, {'right':32}]}

        driving_bones = {}
        shape_key_names = shape_key_list
        for item in shape_key_names:
            if "!!" in item:
                pass
            for key in bone_drivers.keys():
                name_of_driving_bone = ''
            
                if key.lower() in item.lower():

                    if bone_drivers[key] == None:
                        pass
                    elif "!!" in item:
                        pass
                    elif 'head' in item.lower() and 'neck' not in item.lower():
                        # print(item.lower())
                        if len(bone_drivers[key]) == 3:
                            if '_R_' in item:
                                name_of_driving_bone = 'head'
                                driving_bones[item] = [name_of_driving_bone, bone_drivers[key][2]['right']]
                                # driving_bones[item] = [name_of_driving_bone, bone_drivers[key][2]]
                                # print(driving_bones[item])
                            if '_L_' in item:
                                name_of_driving_bone = 'head'
                                driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]['left']]
                                # driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]]
                                # print(driving_bones[item])
                        name_of_driving_bone = 'head'
                        driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]]
                        pass
                        # print(driving_bones[item])
                         ## when adding to dictionary, have name_of_driving_bone be the first item on list, and number second [name_of_driving, num]

                    elif 'hiptwist' in item.lower():
                        pass
                        # print(item)
                        # name_of_driving_bone = 'hipTwist'
                        # driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]]

                    elif bone_drivers[key][0] != "alt":
                        name_of_driving_bone = bone_drivers[key][0]

                        if item[-1] == 'L':
                            name_of_driving_bone = name_of_driving_bone + '_L'
                            driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]]
                            # print(driving_bones[item])
                        elif item[-1] == 'R':
                            name_of_driving_bone = name_of_driving_bone + '_R'
                            driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]]
                            # print(driving_bones[item])
                        else:
                            pass

                    elif bone_drivers[key][0] == "alt":

                        if 'fist' in item.lower():
                            num = item[-1]
                            name_of_driving_bone = item.split('_')[-2]
                            name_of_driving_bone = name_of_driving_bone + "_" + num
                            if '_L_' in item:
                                name_of_driving_bone = name_of_driving_bone + '_L'
                                driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]['left']]
                            else:
                                name_of_driving_bone = name_of_driving_bone + '_R'
                                driving_bones[item] = [name_of_driving_bone, bone_drivers[key][2]['right']]

                        
                        elif 'toe_' in item.lower():
                            num = item[-1]
                            name_of_driving_bone = item.split('_')[-2]
                            name_of_driving_bone = name_of_driving_bone + "_" + num
                            if '_L_' in item:
                                name_of_driving_bone = name_of_driving_bone + '_L'
                                driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]['left']]
                            else:
                                name_of_driving_bone = name_of_driving_bone + '_R'
                                driving_bones[item] = [name_of_driving_bone, bone_drivers[key][2]['right']]
                            
                        elif '_L' in item:
                            if len(bone_drivers[key]) == 3:
                                new = item[:-2]
                                cleaned = new.split('_')[-1]
                                name_of_driving_bone = cleaned + '_L'
                                driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]['left']]
                                # print(bone_drivers[key][1])
                            else:
                                new = item[:-2]
                                cleaned = new.split('_')[-1]
                                name_of_driving_bone = cleaned + '_L'    
                                driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]]
                        
                        elif '_R' in item:
                            if len(bone_drivers[key]) == 3:
                                new = item[:-2]
                                cleaned = new.split('_')[-1]
                                name_of_driving_bone = cleaned + '_R'
                                driving_bones[item] = [name_of_driving_bone, bone_drivers[key][2]['right']]
                                # print(driving_bones[item])
                            else:
                                new = item[:-2]
                                cleaned = new.split('_')[-1]
                                name_of_driving_bone = cleaned + '_R'
                                driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]]
                                # print(driving_bones[item])

                        elif item[-1] == 1 or item[-1] == 2 or item[-1] == 3:
                            print(item[-1])
                            new = item[:-2]
                            print(new)
                            cleaned = new.split('_')[-1]
                            print(cleaned)
                            name_of_driving_bone = cleaned + '_' + item[-1]
                            driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]]
                            # print(driving_bones[item])

                        elif 'head' and 'tilt' in item.lower():
                            if item[-1] == 1 or item[-1] == 2:
                                name_of_driving_bone = 'neck' + '_' + item[-1]
                                # print(name_of_driving_bone)
                                if '_L_' in item:
                                    driving_bones[item] = [name_of_driving_bone, bone_drivers[key][2]['left']]
                                elif '_R_' in item:
                                    driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]['right']]
                                else:
                                    driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]]
                            else:
                                name_of_driving_bone = 'head'
                                if '_L_' in item:
                                    driving_bones[item] = [name_of_driving_bone, bone_drivers[key][2]['left']]
                                if '_R_' in item:
                                    driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]['right']]
                                else:
                                    driving_bones[item] = [name_of_driving_bone, bone_drivers[key][1]]
                        else:
                            pass
        # for item in driving_bones:
        #     if 'head_'
        return driving_bones

    @staticmethod
    def corrective_shape_driver(rig_name, mesh_name, shape_key_name, bone_target, transform_type, driver_type="AVERAGE", driver_express="var", var_type="TRANSFORMS", transform_space="LOCAL_SPACE"):
        arm = bpy.data.objects[rig_name]
        mesh = bpy.data.objects[mesh_name]
        shape_key = mesh.data.shape_keys.key_blocks[shape_key_name]
        driver = shape_key.driver_add('value').driver
        driver.type = driver_type
        
        var = driver.variables.new()
        var.name = 'var'
        var.type = var_type
        
        target = var.targets[0]
        target.id = arm
        target.bone_target = bone_target
        target.transform_type = transform_type
        target.transform_space = transform_space
        
        driver.expression = driver_express

    @staticmethod
    def get_highest_bone_rotation_for_driver(rig_name, bone_name):
        obj = bpy.data.objects[rig_name]
        arm = bpy.data.armatures[rig_name]
        pose_bone = obj.pose.bones.get(bone_name)
        bone_rotation = pose_bone.rotation_quaternion
        bone_rotation_xyz = pose_bone.rotation_euler
        rotation_mode = pose_bone.rotation_mode

        rotation_list = []

        if len(rotation_mode) == 3:
            for item in bone_rotation_xyz:
                if item < 0:
                    item = item * -1
                rotation_list.append(item)
            rotation_list.pop(0)
            # print(rotation_list)
            max_value = (rotation_list.index(max(rotation_list))) 
            # print(max_value)
            # print(bone_rotation[max_value])
            if max_value == 0:
                correct_rotation = 'ROT_X'
            elif max_value == 1:
                correct_rotation = 'ROT_Y'
            else:
                correct_rotation = 'ROT_Z'
            
        elif len(rotation_mode) > 3:
            for item in bone_rotation:
                if item < 0:
                    item = item * -1
                rotation_list.append(item)
            rotation_list.pop(0)
            print(rotation_list)
            max_value = (rotation_list.index(max(rotation_list)) + 1) 
            print(max_value)
            print(bone_rotation[max_value])
            if max_value == 1:
                correct_rotation = 'ROT_X'
            elif max_value == 2:
                correct_rotation = 'ROT_Y'
            else:
                correct_rotation = 'ROT_Z'
        return correct_rotation

    @staticmethod
    def assign_animation_action(rig_name, action_name):
        arm = bpy.data.objects[rig_name]
        named_action = bpy.data.actions.get(action_name)
        arm.animation_data.action = named_action

    @staticmethod
    def change_frame(frame_number):
        bpy.context.scene.frame_set(frame_number)

    @staticmethod
    def action_list():
        actions = bpy.data.actions
        action_names = [action.name for action in actions]
        return action_names

# Rigging_Functions.list_of_shapekeys('')