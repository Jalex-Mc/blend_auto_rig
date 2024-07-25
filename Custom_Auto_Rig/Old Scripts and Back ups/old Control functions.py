import bpy
from mathutils import Vector, Matrix
import math
import bmesh

def clean_select(obj):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.selected_all(action='DESELECT')
    obj = bpy.data.objects[obj]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    obj = bpy.context.active_object
    return obj

scene = bpy.context.scene

obj = clean_select('Cube')

# OG_WORLD = tuple(obj.matrix_world.translation)

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

################# Set's cursor location #########################

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action= 'DESELECT')
bpy.ops.mesh.select_all(action= 'SELECT')

# Check if the object is in edit mode and has vertices
if obj.mode == 'EDIT':
    # Get selected vertices
    first_selected_verts = [v.co for v in obj.data.vertices if v.select]

   # Calculate the average location of selected vertices
    if len(first_selected_verts) > 0:
        avg_location = sum(first_selected_verts, Vector()) / len(first_selected_verts)
        avg_location = obj.matrix_world @ avg_location
        print(avg_location)
       # Set the 3D cursor location
        scene.cursor.location = avg_location
bpy.ops.object.mode_set(mode='OBJECT')

################# Get's cursor location ##########################
  
# Get the 3D cursor location
first_cursor_location = tuple(scene.cursor.location)

print("First 3D Cursor Location:", first_cursor_location)

#################### select object ###########################

bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='OBJECT')
obj = bpy.data.objects['test']
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
obj = bpy.context.active_object

################# Set's cursor location #########################

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action= 'DESELECT')
bpy.ops.mesh.select_all(action= 'SELECT')

# Check if the object is in edit mode and has vertices
if obj.mode == 'EDIT':
    # Get selected vertices
    second_selected_verts = [v.co for v in obj.data.vertices if v.select]

   # Calculate the average location of selected vertices
    if len(second_selected_verts) > 0:
        avg_location = sum(second_selected_verts, Vector()) / len(second_selected_verts)
        avg_location = obj.matrix_world @ avg_location
       # Set the 3D cursor location
    scene.cursor.location = avg_location
bpy.ops.object.mode_set(mode='OBJECT')
################# Get's cursor location ##########################
  
# Get the 3D cursor location
second_cursor_location = tuple(scene.cursor.location)

print("Second 3D Cursor Location:", second_cursor_location)

################## Get's distance between two objects ########################

# Get the locations of the objects
loc1 = Vector((first_cursor_location[0],first_cursor_location[1],first_cursor_location[2]))
loc2 = Vector((second_cursor_location[0],second_cursor_location[1],second_cursor_location[2]))

# Calculate the distance between the objects
distance = loc2 - loc1

print("Distance between Object1 and Object2:", distance)

#################### select object ###########################

bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='OBJECT')
obj = bpy.data.objects['Cube for test']
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
obj = bpy.context.active_object

###################### Moves Vertices #########################

bpy.ops.object.mode_set(mode='EDIT')
if obj.mode == 'EDIT':
    bpy.ops.object.mode_set(mode='OBJECT')
   # Get the selected vertices
   
   # Move the selected vertices
    for vert in first_selected_verts:
        print('working')
       # You can adjust the movement by changing these values
        vert.x += distance.x
        vert.y += distance.y
        vert.z += distance.z
        
# use this to get the name of the bone and the value of the positon from it's original origin, so,
# after I figure out the bone's original location(by creating them on the transfer or UA rig) and then
# the location from the original location, add them to a dictionary, example - {'Neck': Vector((12,3,2))}
distance_between_verts = {}

###### Rotate Vertex's ###########
# Get the active object
obj = bpy.context.active_object
bpy.ops.object.mode_set(mode='EDIT')
# Check if the object is in edit mode
if obj.mode == 'EDIT':
    # only works in 
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Get the selected vertices
    selected_verts = [v for v in obj.data.vertices if v.select]

    # Check if there are selected vertices
    if selected_verts:
        # Calculate the average location of selected vertices
        avg_location = sum((v.co for v in selected_verts), Vector()) / len(selected_verts)
        avg_location = obj.matrix_world @ avg_location
        print(avg_location)
        # Define the rotation angle (example: 45 degrees)
        angle = math.radians(45)

        # Define the rotation matrix around the global Z-axis
        rotation_matrix = Matrix.Rotation(angle, 4, 'Z')

        # Apply rotation to each selected vertex
        for vert in selected_verts:
            # Translate the vertex to the origin
            translated_vert = vert.co - avg_location
            # Rotate the translated vertex
            rotated_vert = rotation_matrix @ translated_vert
            # Translate the rotated vertex back to its original position
            vert.co = rotated_vert + avg_location

        # Update the mesh
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='EDIT')
    else:
        print("No vertices selected.")
else:
    print("Object is not in edit mode.") 

############ get points location and move other points to the location ######

# Get the selected object in Blender
obj = bpy.context.object
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


# Get the selected object in Blender

bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='OBJECT')
obj = bpy.data.objects['Cube for test']
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
obj = bpy.context.active_object
mesh = bpy.context.view_layer.objects.active.data
bpy.ops.object.mode_set(mode='EDIT')
bm = bmesh.from_edit_mesh(mesh)

# Get the selected object in Blender
obj = bpy.context.object
mesh = bpy.context.view_layer.objects.active.data
bpy.ops.object.mode_set(mode='EDIT')
bm = bmesh.from_edit_mesh(mesh)
new_point_locations = []

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
        new_point_locations.append(world_loc)


# get distance between points
distance_between_points = []

for index, vert in og_point_locations:
    distance_between_points.append(new_point_locations - og_point_locations)

print(distance_between_points)


###### Rotate Vertex's ###########
# Get the active object
obj = bpy.context.active_object
bpy.ops.object.mode_set(mode='EDIT')
# Check if the object is in edit mode
if obj.mode == 'EDIT':
    # only works in 
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Get the selected vertices
    selected_verts = [v for v in obj.data.vertices if v.select]

    # Check if there are selected vertices
    if selected_verts:
        # Calculate the average location of selected vertices
        avg_location = sum((v.co for v in selected_verts), Vector()) / len(selected_verts)
        avg_location = obj.matrix_world @ avg_location
        print(avg_location)
        # Define the rotation angle (example: 45 degrees)
        angle = math.radians(45)

        # Define the rotation matrix around the global Z-axis
        rotation_matrix = Matrix.Rotation(angle, 4, 'Z')

        # Apply rotation to each selected vertex
        for vert in selected_verts:
            # Translate the vertex to the origin
            translated_vert = vert.co - avg_location
            # Rotate the translated vertex
            rotated_vert = rotation_matrix @ translated_vert
            # Translate the rotated vertex back to its original position
            vert.co = rotated_vert + avg_location

        # Update the mesh
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='EDIT')
    else:
        print("No vertices selected.")
else:
    print("Object is not in edit mode.")