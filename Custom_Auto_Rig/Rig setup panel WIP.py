# import bpy

# def step_1():
#     filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_1 blend.py"
#     exec(compile(open(filename).read(), filename, 'exec'))

# def step_2():
#     filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_2 blend.py"
#     exec(compile(open(filename).read(), filename, 'exec'))

#     filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_3 blend.py"
#     exec(compile(open(filename).read(), filename, 'exec'))

# def step_3():
#     filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_4 blend.py"
#     exec(compile(open(filename).read(), filename, 'exec'))

#     filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_5 blend.py"
#     exec(compile(open(filename).read(), filename, 'exec'))

#     filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_6 blend.py"
#     exec(compile(open(filename).read(), filename, 'exec'))

# def step_4():
#     filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_Rig_CTRLS_2.py"
#     exec(compile(open(filename).read(), filename, 'exec'))

### if relative. Will need to change the above to this
# filepath = bpy.path.abspath("//myscript.py")

import bpy
from mathutils import Vector
import math
import os
import sys
import numpy as np

class Step_1(bpy.types.Operator):
    
    bl_idname = "arm.autorig_1"
    bl_label = "Run autorig script 1"
    
    filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_1 blend.py"
    def execute(self, context):
        
        exec(compile(open(self.filename).read(), self.filename, 'exec'))
        
        return {"FINISHED"}

class Step_2(bpy.types.Operator):
    
    bl_idname = "arm.autorig_2"
    bl_label = "Run autorig script 2"
    
    filename_2 = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_2 blend.py"
    # filename_3 = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_3 blend.py"
    def execute(self, context):
        
        exec(compile(open(self.filename_2).read(), self.filename_2, 'exec'))
        # exec(compile(open(self.filename_3).read(), self.filename_3, 'exec'))
        
        return {"FINISHED"}

class Step_3(bpy.types.Operator):
    
    bl_idname = "arm.autorig_3"
    bl_label = "Run autorig script 3"
    
    filename_3 = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_3 blend run script.py"
    # filename_3 = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_3 blend.py"
    def execute(self, context):
        
        exec(compile(open(self.filename_3).read(), self.filename_3, 'exec'))
        # exec(compile(open(self.filename_3).read(), self.filename_3, 'exec'))
        
        return {"FINISHED"}
    

class Step_4(bpy.types.Operator):
    
    bl_idname = "arm.autorig_4"
    bl_label = "Run autorig script 3"
    
    filename_4 = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_4 blend.py"
    filename_5 = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_5 blend.py"
    filename_6 = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_6 blend run script.py"
    def execute(self, context):
        
        exec(compile(open(self.filename_4).read(), self.filename_4, 'exec'))
        exec(compile(open(self.filename_5).read(), self.filename_5, 'exec'))
        exec(compile(open(self.filename_6).read(), self.filename_6, 'exec'))
        
        return {"FINISHED"}
    
class Step_5(bpy.types.Operator):
    
    bl_idname = "arm.autorig_5"
    bl_label = "Run autorig script 5"
    
    filename_ctrls = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_Rig_CTRLS_2.py"

    def execute(self, context):
        
        exec(compile(open(self.filename_ctrls).read(), self.filename_ctrls, 'exec'))
        
        return {"FINISHED"}


class VIEW3D_PT_my_custom_panel(bpy.types.Panel):  # class naming convention ‘CATEGORY_PT_name’

    # where to add the panel in the UI
    bl_space_type = "VIEW_3D"  # 3D Viewport area (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items)
    bl_region_type = "UI"  # Sidebar region (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html#rna-enum-region-type-items)

    # add labels
    bl_category = "U auto script"  # found in the Sidebar
    bl_label = "U autorigging script"  # found at the top of the Panel

    def draw(self, context):
        """define the layout of the panel"""
        self.layout.row().label(text="Click buttons in order")
        row = self.layout.row()
        row.operator("arm.autorig_1", text="Run Part 1")
        self.layout.row().label(text="Fix knee poles before continuing")
        row = self.layout.row()
        row.operator("arm.autorig_2", text="Run Part 2")
        row = self.layout.row()
        row.operator("arm.autorig_3", text="Run Part 3")
        self.layout.row().label(text="RUN SCRIPT 3 IN TEXT EDITOR")
        self.layout.row().label(text="Fix arm poles before continuing")
        row = self.layout.row()
#        self.layout.seperator()
        row.operator("arm.autorig_4", text="Run Part 4")
        self.layout.row().label(text="RUN SCRIPT 6 IN TEXT EDITOR")        
        self.layout.row().label(text="Create Ctrls Before continuing")        
        row = self.layout.row()
        row.operator("arm.autorig_5", text="Run Part 5")
        row = self.layout.row()
        self.layout.row().label(text="Finished!")


        ### once script 3 is done, layout - script 1 button, script 2-3 button, script 4-6 button, ctrls button.

        # """define the layout of the panel"""
        # self.layout.row().label(text="Click buttons in order")
        # row = self.layout.row()
        # row.operator("arm.autorig_1", text="Run Part 1")
        # self.layout.row().label(text="Fix knee poles before continuing")
        # row = self.layout.row()
        # row.operator("arm.autorig_2", text="Run Part 2")
        # self.layout.row().label(text="Fix elbow poles before continuing")
        # row = self.layout.row()
        # row.operator("arm.autorig_3", text="Run Part 3")
        # row = self.layout.row()
        # self.layout.row().label(text="Create Controls Before Next Part")
        # row.operator("arm.autorig_4", text="Run Part 4")
        # row = self.layout.row()
        # self.layout.row().label(text="Finished!")



def register():
    bpy.utils.register_class(VIEW3D_PT_my_custom_panel)
    bpy.utils.register_class(Step_1)
    bpy.utils.register_class(Step_2)
    bpy.utils.register_class(Step_3)
    bpy.utils.register_class(Step_4)
    bpy.utils.register_class(Step_5)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_my_custom_panel)
    bpy.utils.unregister_class(Step_1)
    bpy.utils.unregister_class(Step_2)
    bpy.utils.unregister_class(Step_3)
    bpy.utils.unregister_class(Step_4)
    bpy.utils.unregister_class(Step_5)


if __name__ == "__main__":
    register()