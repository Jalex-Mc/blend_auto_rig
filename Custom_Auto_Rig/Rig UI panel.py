import bpy

my_rig_id = "universal rig"


# the name select_all causes the class to not be able to be unregistered for some reason
class POSE_s_all(bpy.types.Operator):
    bl_idname = "pose.s_all"
    bl_label = "Select Bones"

    def execute(self, context):
        obj = bpy.context.active_object
        pose_bones = obj.pose.bones
        any_selected = any(bone.bone.select for bone in pose_bones)
        
        if any_selected:
            for bone in pose_bones:
                bone.bone.select = False
        else:
            bpy.ops.pose.select_all(action='TOGGLE')

        return {"FINISHED"}
        
class POSE_hide_all(bpy.types.Operator):
    bl_idname = "pose.hide_all"
    bl_label = "Hide Bones"

    def execute(self, context):
        obj = bpy.context.active_object
        
        for bone in obj.pose.bones:
            bone.bone.hide = True    

        return {"FINISHED"}

class POSE_show_all(bpy.types.Operator):
    bl_idname = "pose.show_all"
    bl_label = "Show Bones"

    def execute(self, context):
        bpy.ops.pose.reveal()
        return {"FINISHED"}

class KEYFRAME_all(bpy.types.Operator):
    bl_idname = "keyframe.all"
    bl_label = "Keyframe All"
    
    def execute(self, context):
        obj = bpy.context.active_object
        
        frame_number = bpy.context.scene.frame_current
        
        # Keyframe all pose bones for location, rotation, and scale
        for bone in obj.pose.bones:
            bone_name = bone.name
        
        # Insert keyframes for location, rotation, and scale
            obj.keyframe_insert(data_path=f'pose.bones["{bone_name}"].location', frame=frame_number)
            obj.keyframe_insert(data_path=f'pose.bones["{bone_name}"].rotation_quaternion', frame=frame_number)
            obj.keyframe_insert(data_path=f'pose.bones["{bone_name}"].scale', frame=frame_number)    

        # time ineffective way -- 6 seconds compared to nearly instant
#        for bone in obj.pose.bones:
#            bone.bone.select = True
#            bpy.ops.anim.keyframe_insert_by_name(type="LocRotScale")
        return {"FINISHED"}
    
class My_Rig_UI(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Rig Ctrls"
    bl_label = "Rig Controls"
    bl_idname = f'VIEW3D_PT_rig_ui_{my_rig_id}'
    # below is optional
    #bl_context = "posemode"
    

    # @classmethod
    # def poll(self, context):
    #     try:
    #         return (context.active_object.data.get("rig_id") == my_rig_id)
    #     except (AttributeError, KeyError, TypeError):
    #         return False

    def draw(self, context):
        layout = self.layout # making sure the layout is created
        current_column = layout.column() #from the layout we are grabbing a column

        # Visibility Label
        current_column.row().label(text="Visibility")
        
        # select All/None
        current_column.row().operator("pose.s_all", text="Select All/None")

        # Hide All - Show All
        current_row = current_column.row()
        current_nested_row = current_row.row()
        current_nested_row.operator("pose.hide_all", text="Hide All")
        current_nested_row = current_row.row()
        current_nested_row.operator("pose.show_all", text="Show All")
        
        # Keyframe All
        current_row = current_column.row()
        current_nested_row = current_row.row()
        current_nested_row.operator("keyframe.all", text="Keyframe All")

        # Spacer
        current_column.separator()

        # Space Switch WIP
        current_column.row().label(text="Space Switch")        
        
        # Spacer
        current_column.separator()
        
        # FK/IK Switch WIP
        current_column.row().label(text="FK/IK Switch")         
        
        # Spacer
        current_column.separator()

        # Rig Controls
        current_column.row().label(text="Rig Controls")
        
        # Root - Single element
#        collection_name = "Deform"
#        bone_collection = bpy.context.object.data.collections_all[collection_name]
#        current_column.row().prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        # Root - multiple elements
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "Root"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")
        
        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        # Head - nested example
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "Head"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "CTRL"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # Head Controller
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "Head CTRL"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")
        
        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        # Viewport Facial Controls
        
        # Face controls (Will include all facial controls)
            # L Eye R Eye
            # Jaw Tongue
        
        # Spacer
        current_column.separator()        
        
        # L clavicle R clavicle
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "L clavicle"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "R clavicle"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # Breast/Pectorals
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "Breast/Pecs"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")
        
        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        # L arm IK R arm IK
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "L arm IK"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "R arm IK"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")
        
        # L arm FK R arm FK
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "L arm FK"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "R arm FK"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # L Hand R Hand
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "L hand"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "R hand"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        #L Fingers R Fingers
        # current_row = current_column.row()
        # current_nested_row = current_row.row()
        # collection_name = "CTRL"
        # bone_collection = bpy.context.object.data.collections_all[collection_name]
        # current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # current_nested_row = current_row.row()
        # current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        # current_nested_row = current_row.row()
        # collection_name = "CTRL"
        # bone_collection = bpy.context.object.data.collections_all[collection_name]
        # current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        # current_nested_row = current_row.row()
        # bone_collection = bpy.context.object.data.collections_all[collection_name]
        # current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # Spacer
        current_column.separator()         
        
        # Spine Back
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "Spine"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "Back"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # Hip Pelvis
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "Hip"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "Pelvis"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # Spacer
        current_column.separator() 

        # L Leg IK R Leg IK
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "L Leg IK"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "R Leg IK"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # To be under Leg IK, maybe not
        
        # L Foot IK R Foot IK
        # current_row = current_column.row()
        # current_nested_row = current_row.row()
        # collection_name = "CTRL"
        # bone_collection = bpy.context.object.data.collections_all[collection_name]
        # current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # current_nested_row = current_row.row()
        # current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        # current_nested_row = current_row.row()
        # collection_name = "CTRL"
        # bone_collection = bpy.context.object.data.collections_all[collection_name]
        # current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        # current_nested_row = current_row.row()
        # bone_collection = bpy.context.object.data.collections_all[collection_name]
        # current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # L Heel Positioning R Heel Positioning
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "L heel position"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "R heel position"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # L Toes R Toes
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "L toes"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "R toes"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # Spacer
        current_column.separator() 
        
        # L Leg FK R Leg FK
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "L Leg FK"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "R Leg FK"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        # L Foot R Foot
        current_row = current_column.row()
        current_nested_row = current_row.row()
        collection_name = "L foot"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

        current_nested_row = current_row.row()
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)
        
        current_nested_row = current_row.row()
        collection_name = "R foot"
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_visible', toggle=True, text=collection_name)

        current_nested_row = current_row.row()
        bone_collection = bpy.context.object.data.collections_all[collection_name]
        current_nested_row.prop(bone_collection, 'is_solo', toggle=True, text="", icon="SOLO_ON")

               

def register():
    bpy.utils.register_class(My_Rig_UI)
    bpy.utils.register_class(POSE_s_all)
    bpy.utils.register_class(POSE_hide_all)
    bpy.utils.register_class(POSE_show_all)
    bpy.utils.register_class(KEYFRAME_all)
    
def unregister():
    bpy.utils.unregister_class(My_Rig_UI)
    bpy.utils.unregister_class(POSE_s_all)
    bpy.utils.unregister_class(POSE_hide_all)
    bpy.utils.unregister_class(POSE_show_all)
    bpy.utils.unregister_class(KEYFRAME_all)

if __name__ == "__main__":
    register()
    