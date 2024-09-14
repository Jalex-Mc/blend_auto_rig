import bpy
import bmesh
from mathutils import Vector

############ WORKING TO MOVE VERTEX TO A STATED LOCATION ##########

def get_list_of_objs_in_coll(coll_name):
    # Get the collection by name
    collection_of_objects = []
    collection_name = coll_name  # Change this to your collection name
    collection = bpy.data.collections.get(collection_name)

    if collection:
        # Access all objects in the collection
        objects_in_collection = collection.objects
        
        # Print the names of all objects in the collection
        for obj in objects_in_collection:
            collection_of_objects.append(obj.name)
    else:
        print("Collection not found.")

    return collection_of_objects

def clean_select(obj):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    obj = bpy.data.objects[obj]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    obj = bpy.context.active_object
    return obj

def points_list(obj):
    obj = clean_select(obj)
    mesh = bpy.context.view_layer.objects.active.data
    bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(mesh)

    og_point_locations = []

    # Check if the object is valid and is in edit mode
    if obj and obj.type == 'MESH' and obj.mode == 'EDIT':
        # Get a BMesh representation
        bm = bmesh.from_edit_mesh(mesh)

        # Iterate through the vertices
        for vert in bm.verts:
            print("working")
            # Get the world location of each vertex
            world_loc = obj.matrix_world @ vert.co
            print("Vertex", vert.index, ":", world_loc)
            og_point_locations.append(world_loc)

    return og_point_locations

moved_bone_ctrl = points_list('CTRL-Bone.001')


obj = clean_select('CTRL-Bone.002')
bpy.ops.object.mode_set(mode='OBJECT')
obj = bpy.data.objects['CTRL-Bone.002']
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
mesh = bpy.context.view_layer.objects.active.data
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
#mesh = bpy.context.view_layer.objects.active.data
bpy.ops.object.mode_set(mode='EDIT')
bm = bmesh.from_edit_mesh(mesh)
if obj.mode == 'EDIT':
#        bpy.ops.object.mode_set(mode='OBJECT')
    bm = bmesh.from_edit_mesh(mesh)
    # Get the selected vertices
#        selected_verts = [v.co for v in obj.data.vertices if v.select]
#        print(len(selected_verts))
    # Move the selected vertices
    for index, vert in enumerate(bm.verts):
#        global_coords = Vector((0.0000, -0.9829, 1.1040))
        global_coords = moved_bone_ctrl[index]
        local_coords = obj.matrix_world.inverted() @ global_coords
        print(f"before transform: {vert}")
        vert.co = local_coords
        print(f"after transform: {vert}")