import bpy
from mathutils import Vector, Matrix
import bmesh
import json

'''This Script Moves the CTRLS to the Locations grabbed in Auto_Rig_CTRLS_1'''
'''If there is no txt file named end_points, make sure to go through Auto_Rig_CTRLS_1'''

'''If if it keeps crashing, unselect everything hide the CTRL collection(keep it selectable), and select just the rig'''

scene = bpy.context.scene

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
            # print("working")
            # Get the world location of each vertex
            world_loc = obj.matrix_world @ vert.co
            # print("Vertex", vert.index, ":", world_loc)
            og_point_locations.append(world_loc)

    return og_point_locations

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

def distance_between_points(first_obj_locs, final_obj_locs):
    first_points_loc = points_list(first_obj_locs)
    second_points_loc = points_list(final_obj_locs)
    distance_between_points = []

    for index, vert in enumerate(first_points_loc):
        distance_between_points.append(second_points_loc[index] - vert)

    with open('O:\\Onedrive\\Python_Blender\\blend_auto_rig\\Custom_Auto_Rig\\point_distance.json', 'w+') as file:
        json.dump(distance_between_points, file)
        # print('Done')

def get_distance_list(file_loc):
    with open(file_loc, 'rb') as file:
        distance_list = json.load(file)
        return distance_list
    
def move_vertices(list):
    objects_to_move = get_list_of_objs_in_coll(list)

    for object in objects_to_move:
        obj = clean_select(object)
        bpy.ops.object.mode_set(mode='OBJECT')
        obj = bpy.data.objects[object]
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        mesh = bpy.context.view_layer.objects.active.data
        bpy.ops.object.mode_set(mode='EDIT')

        if obj.mode == 'EDIT':
                bpy.ops.object.mode_set(mode='OBJECT')
            # Get the selected vertices
                selected_verts = [v.co for v in obj.data.vertices if v.select]

            # Move the selected vertices
                for index, vert in enumerate(selected_verts):
                    # print('working')
                # You can adjust the movement by changing these values
                    vert.x += distance_between_points[index].x
                    vert.y += distance_between_points[index].y
                    vert.z += distance_between_points[index].z

        


################## Moves the CTRLS to the Final location ####################

with open('O:\\Onedrive\\Python_Blender\\blend_auto_rig\\Custom_Auto_Rig\\end_points.txt', 'r') as file:
    end_points = json.load(file)
    print("read")


obj_coll = get_list_of_objs_in_coll('CTRLS')
count = 0
for item in obj_coll:
    # print(item)
    # print(end_points[item])
    if item in end_points:        
        obj = clean_select(item)
        bpy.ops.object.mode_set(mode='OBJECT')
        obj = bpy.data.objects[item]
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        mesh = bpy.context.view_layer.objects.active.data
        world =  bpy.context.object.matrix_world
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        mesh = bpy.context.view_layer.objects.active.data
        bm = bmesh.from_edit_mesh(mesh)

        for index, vert in enumerate(bm.verts):
            mat_world = obj.matrix_world
            try:
                vec = end_points[item][index]
            # print(f"{vert.index}: vec: {vec}")
                vert.co.x = vec[0]
                vert.co.y = vec[1]
                vert.co.z = vec[2]
            # print(f"{vert.index}: vec: {tuple(vert.co)}")
            except:
                print(f"last point {item}")

bpy.ops.object.mode_set(mode='OBJECT')
