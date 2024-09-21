import bpy

def step_1():
    filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_1 blend.py"
    exec(compile(open(filename).read(), filename, 'exec'))

def step_2():
    filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_2 blend.py"
    exec(compile(open(filename).read(), filename, 'exec'))

    filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_3 blend.py"
    exec(compile(open(filename).read(), filename, 'exec'))

def step_3():
    filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_4 blend.py"
    exec(compile(open(filename).read(), filename, 'exec'))

    filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_5 blend.py"
    exec(compile(open(filename).read(), filename, 'exec'))

    filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_6 blend.py"
    exec(compile(open(filename).read(), filename, 'exec'))

def step_4():
    filename = "O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_Rig_CTRLS_2.py"
    exec(compile(open(filename).read(), filename, 'exec'))

### if relative. Will need to change the above to this
# filepath = bpy.path.abspath("//myscript.py")