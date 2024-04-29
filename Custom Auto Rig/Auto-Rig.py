import subprocess
import bpy
from mathutils import Vector
import math
from collections import OrderedDict
import numpy as np
import time

# Execute another Python script
subprocess.run(["C:/Program Files/Python311/python.exe", "O:/Onedrive/Python Blender/Auto_rig_1.py"])
subprocess.run(["C:/Program Files/Python311/python.exe", "O:/Onedrive/Python Blender/Auto_rig_2.py"])
subprocess.run(["C:/Program Files/Python311/python.exe", "O:/Onedrive/Python Blender/Auto_rig_3.py"])
subprocess.run(["C:/Program Files/Python311/python.exe", "O:/Onedrive/Python Blender/Auto_rig_4.py"])


# temp_blend_path = 'O:/Onedrive/Character Assets/Characters/Transfer Rig/Transfer rig.blend'

# filepath = 'C:/Users/Desktop/my_script.py'

# process = subprocess.Popen([bpy.app.binary_path, "--factory-startup", "-b", temp_blend_path, "--python", f"O:\Onedrive\Python Blender\Auto_rig_1.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf-8')
# process.wait()
# process = subprocess.Popen([bpy.app.binary_path, "--factory-startup", "-b", temp_blend_path, "--python", f"O:\Onedrive\Python Blender\Auto_rig_2.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf-8')
# process.wait()
# process = subprocess.Popen([bpy.app.binary_path, "--factory-startup", "-b", temp_blend_path, "--python", f"O:\Onedrive\Python Blender\Auto_rig_3.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf-8')
# process.wait()
# process = subprocess.Popen([bpy.app.binary_path, "--factory-startup", "-b", temp_blend_path, "--python", f"O:\Onedrive\Python Blender\Auto_rig_4.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf-8')
# process.wait()