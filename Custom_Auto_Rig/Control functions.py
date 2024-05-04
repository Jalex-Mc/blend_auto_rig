import bpy
from mathutils import Vector, Matrix
import bmesh
import json

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
            print("working")
            # Get the world location of each vertex
            world_loc = obj.matrix_world @ vert.co
            print("Vertex", vert.index, ":", world_loc)
            og_point_locations.append(world_loc)

    return og_point_locations

def get_list_of_objs_in_coll(coll_name):
    # Get the collection by name
    collection_name = coll_name  # Change this to your collection name
    collection = bpy.data.collections.get(collection_name)

    if collection:
        # Access all objects in the collection
        objects_in_collection = collection.objects
        
        # Print the names of all objects in the collection
        for obj in objects_in_collection:
            print(obj.name)
    else:
        print("Collection not found.")

    return objects_in_collection

def distance_between_points(first_obj_locs, final_obj_locs):
    first_points_loc = points_list(first_obj_locs)
    second_points_loc = points_list(final_obj_locs)
    distance_between_points = []

    for index, vert in enumerate(first_points_loc):
        distance_between_points.append(second_points_loc[index] - vert)

    with open('point_distance.json', 'w+') as file:
        json.dump(distance_between_points, file)
        print('Done')

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
                    print('working')
                # You can adjust the movement by changing these values
                    vert.x += distance_between_points[index].x
                    vert.y += distance_between_points[index].y
                    vert.z += distance_between_points[index].z

        
    

################## get first points location ####################

og_points_list = points_list('Cube')

################## get second points location ####################

second_points_list = points_list('test')

################## get distance ####################

distance_between_points = []

for index, vert in enumerate(og_points_list):
    distance_between_points.append(second_points_list[index] - vert)

print(distance_between_points) 

################## get distance ####################

obj = clean_select('Cube for test')
mesh = bpy.context.view_layer.objects.active.data
bpy.ops.object.mode_set(mode='EDIT')

if obj.mode == 'EDIT':
    bpy.ops.object.mode_set(mode='OBJECT')
   # Get the selected vertices
    selected_verts = [v.co for v in obj.data.vertices if v.select]

   # Move the selected vertices
    for index, vert in enumerate(selected_verts):
        print('working')
       # You can adjust the movement by changing these values
        vert.x += distance_between_points[index].x
        vert.y += distance_between_points[index].y
        vert.z += distance_between_points[index].z