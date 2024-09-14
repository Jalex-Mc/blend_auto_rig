import bpy
# from Finished_functions import *
from mathutils import Vector
from collections import OrderedDict


################################
################################


def set_mode(a_mode):
    bpy.ops.object.mode_set(mode=a_mode)


def select_bone_as_active_edit(rig_name, bone_name):
    bpy.ops.object.mode_set(mode='OBJECT')
    arm = bpy.data.armatures[rig_name]
    bpy.ops.object.mode_set(mode='EDIT')
    bone = arm.edit_bones[bone_name]
    arm.edit_bones.active = bone


def remove_object_selection():
    set_mode('OBJECT')
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

def get_bone_location(rig_name, bone_name):
    bpy.ops.object.mode_set(mode='POSE')
    arm = bpy.data.objects[rig_name]
    bone = arm.pose.bones[bone_name]
    print(bone.head)
    print(bone.tail)
    bone.bone.select = True
    head = bone.head
    tail = bone.tail
    return head, tail

def bone_head_tail_locations(rig_name, bone_name):
    bpy.ops.object.mode_set(mode='OBJECT')
    remove_object_selection()
    bpy.context.view_layer.objects.active = bpy.data.objects[rig_name]
    bpy.ops.object.mode_set(mode='EDIT')
    arm = bpy.data.armatures[rig_name]
    bone = arm.edit_bones[bone_name]
    bone_roll = bone.roll
    head_local = bone.head
    tail_local = bone.tail
    armature_obj = bpy.context.active_object
    # armature = armature_obj.data
    # world_matrix = armature_obj.matrix_world
    head_global = armature_obj.matrix_world @ head_local
    tail_global = armature_obj.matrix_world @ tail_local
    return (head_global, tail_global, bone_roll)

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

################################
################################


def bonera_pole_fix(bone_name):
    # in pose mode.
    # make bone name active target.
    pass

## create args so I can add or find the default values for the peroperty, this is creating
## a float property 
def create_property(rig_name, bone_name, prop_name):
    set_mode("OBJECT")
    remove_object_selection()
    select_bone_as_active_edit(rig_name, bone_name)
    set_mode('POSE')
    
    # THIS CREATES THE DAMNED THING
    bone = bpy.data.objects[rig_name].pose.bones[bone_name]
    bone[prop_name] = 1.0
    # bone['IKFK'].IntProperty(min=0, max=1)
    fk_id_properties_ui = bpy.data.objects[rig_name].pose.bones[bone_name].id_properties_ui(prop_name)
    fk_id_properties_ui.update(max=1,min=0)
  
# create_property('Armature', 'Bone', "FKIK")

def get_data_path():
    pass

# def create_driver(rig_name, bone_name, modifier_name):
#     arm = bpy.data.objects[rig_name]
#     bone = arm.pose.bones.get(bone_name)
#     bone_modifiers = bone.constraints
#     for item in bone_modifiers:
#         if modifier_name in bone_modifiers:
#             print(item.influence)
#             object_path = repr(item.influence)
#             full_path = f"{object_path}.{item.influence.path_from_id()}"
#             print(full_path)

def create_driver_for_bone_modifiers(rig_name, bone_name,is_valid=False, type="AVERAGE",use_self=False):
    arm = bpy.data.objects[rig_name]
    bone = arm.pose.bones.get(bone_name)
    bone_modifiers = bone.constraints
    # for item in bone_modifiers:
    #     if modifier_name in bone_modifiers:
    #         print(item.influence)
    #         item.driver_add(driver_place)
    # bone_modifiers.driver
    # arm.driver

create_driver_for_bone_modifiers('Armature', 'Bone')

def create_driver_for_bone_modifiers(rig_name, bone_name, modifier_name, driver_place="",is_valid=False, type="AVERAGE",use_self=False):
    arm = bpy.data.objects[rig_name]
    bone = arm.pose.bones.get(bone_name)
    bone_modifiers = bone.constraints
    for item in bone_modifiers:
        if modifier_name in bone_modifiers:
            print(item.influence)
            item.driver_add(driver_place)

# def bone_eular_change(bone_name):
#     pass


def move_bone_top(bone_name, rig_name, head, tail, amount, axis):
    pass

def object_location(object):
    # object_selection(object)
    object_as_object = bpy.data.objects[object]
    return object_as_object.location

print(object_location('Empty'))

# functions I want. move bone head or tails
# rig constraints
# Flip bone
# bone to collection(if not found, create collection)
# subdivide bone(property for how many times)(name the new bones)(and parent)
# create property(takes the name of property and on what object(bone or object, etc))
# create driver
# get constraints on bone, then change the properties of a constraint.
# delete constraints
# look at instructions list to figure out any duplicates. Maybe even with the foot.


# def duplicate_bones(rig_name, bone_name, duplicated_name):
#    rig = bpy.data.armatures[rig_name]
#    bpy.ops.object.mode_set(mode='EDIT')
#    # gets the original bone to copy. it's in EditBone context.
#    bone = rig.edit_bones[bone_name]
#    duplicated_bone = rig.edit_bones.new(bone.name)
#    print(duplicated_bone)
#    duplicated_bone.name = duplicated_name
#    duplicated_bone.length = bone.length
#    duplicated_bone.matrix = bone.matrix.copy()
#    rig.edit_bones[duplicated_bone.name].parent = None
#    return select_bone(duplicated_bone.name, rig_name, True, True)

# bone_head_location, bone_tail_location = get_bone_world_location('Armature', 'Bone')
# move_bone_world_location('Armature', 'Bone', Vector ((-24.5384, 0.6713, 0)), Vector ((-24.5384, 2.4420, 0)))
# figure out how to make constraints.

# remember to go back and change the main file to check if any function requires an mode change, since I'm accessing the armature
# directly in most functions.
# delete empties on success as last step.

# select_bone_as_active_edit('Armature', 'bone_name')


# make the above a function
# make a function of getting an bone head or tail to get the world pos.
# test making a move with an offset, like move bone here but 1 away from this axis
# test creating a bone and doing the above.
