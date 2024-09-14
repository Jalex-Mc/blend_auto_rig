import bpy
import bmesh
from mathutils import Vector, Matrix
import json

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
#            print("working")
            # Get the world location of each vertex
#            world_loc = obj.matrix_world @ vert.co
#            print("Vertex", vert.index, ":", vert.co)
            og_point_locations.append(vert.co)

    return og_point_locations

moved_bone_ctrl = points_list('CTRL-Bone.001')
#with open('O:\\Onedrive\\Character Assets\\Characters\\Transfer Rig\\start_points.txt', 'w') as file:
#       # file.write(json.dumps(a_list))
#       json.dump(start_points, file, ensure_ascii=False)
#       print('finished!')

ctrl_loc = {}
#print(f"Pre - {moved_bone_ctrl}")
print(" ")
print(" ")

for item in range(28):
    ctrl_loc[item] = tuple(moved_bone_ctrl[item])
    moved_bone_ctrl[item] = tuple(moved_bone_ctrl[item])

with open('O:\\Onedrive\\Character Assets\\Characters\\Transfer Rig\\start_points.txt', 'w') as file:
       # file.write(json.dumps(a_list))
       json.dump(moved_bone_ctrl, file, ensure_ascii=False)
       print('finished!')

print(f"Pre - {ctrl_loc}")
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='DESELECT')

with open('O:\\Onedrive\\Character Assets\\Characters\\Transfer Rig\\start_points.txt', 'r') as file:
    end_points = json.load(file)
    
print(f"Post - {end_points}")
obj = clean_select('CTRL-Bone.002')
bpy.ops.object.mode_set(mode='OBJECT')
obj = bpy.data.objects['CTRL-Bone.002']
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
mesh = bpy.context.view_layer.objects.active.data
world =  bpy.context.object.matrix_world
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
mesh = bpy.context.view_layer.objects.active.data
bpy.ops.object.mode_set(mode='EDIT')

bm = bmesh.from_edit_mesh(mesh)
vert_num = 0
if obj.mode == 'EDIT':
    print(" ")
    print(" ")
    print(f"Post - {end_points}")
    bm = bmesh.from_edit_mesh(mesh)
    # Get the selected vertices
#        selected_verts = [v.co for v in obj.data.vertices if v.select]
#        print(len(selected_verts))
    # Move the selected vertices
    for index, vert in enumerate(bm.verts):
#        vert_num += 1
#        print(index)
        mat_world = obj.matrix_world
#        vec = Vector((0.0, 0.0, 0.1))
        vec = moved_bone_ctrl[index] 
        print(f"{vert.index}: vec: {vec}")
        vert.co.x += vec[0]
        vert.co.y += vec[1]
        vert.co.z += vec[2]
        print(f"{vert.index}: vec: {tuple(vert.co)}")
#        print(f"index: {vert.index}: {end_points[index]}")
#        mat_edit = mat_world.inverted() @ Matrix.Translation(vec) @ mat_world
#        print(vert_num)
#        vert.co = mat_edit @ vert.co
#        moved_loc = moved_bone_ctrl[index] @ mat_edit
#        global_coords = Vector((0.0000, -0.9829, 1.1040))
#        global_coords = moved_bone_ctrl[index]
#        local_coords = obj.matrix_world.inverted() @ global_coords
#        print(f"before transform:{vert.index}: {vert.co}")
#        tuple_test = tuple(vert.co)
#        print(tuple_test)
#        new_loc = tuple(moved_bone_ctrl[index])
#        tuple_test += new_loc
#        vert.co = list(tuple_test)
#        world_vertex = vert.co * world
#        vert.co = moved_loc
#        print(f"after transform:{vert.index}: {vert.co}")
#        vert.co.x += moved_bone_ctrl[index].x
#        vert.co.y += moved_bone_ctrl[index].y
#        vert.co.z += moved_bone_ctrl[index].z   
#        print(f"after transform: {vert.co}")
