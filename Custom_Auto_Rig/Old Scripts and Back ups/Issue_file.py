# this get's all the points locations of a control object and put them into a dictionary and export them.

mesh_list = get_list_of_objs_in_coll('CTRLS')
mesh_list.sort(key=lambda x: x[:6])

start_points = dict.fromkeys(mesh_list)        

for obj in mesh_list:
   if obj in start_points:
       temp = []
       points = points_list(obj)
       for item in points:
           temp.append(tuple(item))
       start_points[obj] = temp

print(start_points)


with open('O:\\Onedrive\\Python_Blender\\blend_auto_rig\\Custom_Auto_Rig\\start_points.txt', 'w') as file:
       # file.write(json.dumps(a_list))
       json.dump(start_points, file, ensure_ascii=False)
       print('finished!')

### functions for below -
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

# this is supposed to move an control object points to the object location in the txt file -

with open('O:\\Onedrive\\Python_Blender\\blend_auto_rig\\Custom_Auto_Rig\\start_points.txt', 'r') as file:
    start_points = json.load(file)


with open('O:\\Onedrive\\Python_Blender\\blend_auto_rig\\Custom_Auto_Rig\\end_points.txt', 'r') as file:
    end_points = json.load(file)

# was attempting to get the difference between starting points and where the points end up so I can move them, but it only moved a little
distance_between_points = dict.fromkeys(start_points)


for key, value in start_points.items():
    distance_between_points[key] = []
    for index, vert in enumerate(value):
        distance = list(map(lambda a, b: a - b, end_points[key][index], vert))
        distance_between_points[key].append(tuple(distance))

obj_coll = get_list_of_objs_in_coll('CTRLS')
count = 0
for item in obj_coll:
    if item in distance_between_points:
        obj = clean_select(item)
        bpy.ops.object.mode_set(mode='OBJECT')
        obj = bpy.data.objects[item]
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
                print(len(selected_verts))
            # Move the selected vertices
                for index, vert in enumerate(selected_verts):
                    print(len(distance_between_points[key]))

                # You can adjust the movement by changing these values
                    vert.x += distance_between_points[item][index][0]
                    vert.y += distance_between_points[item][index][1]
                    vert.z += distance_between_points[item][index][2]    
