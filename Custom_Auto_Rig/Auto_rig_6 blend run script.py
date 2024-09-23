import bpy

############################ changes workspace to scripting

# Get the workspace by name (e.g., 'Scripting')
workspace_name = "Scripting"

# Ensure the workspace exists before switching
workspace = bpy.data.workspaces.get(workspace_name)

if workspace:
    # Switch to the specified workspace
    bpy.context.window.workspace = workspace
    print(f"Switched to workspace: {workspace_name}")
else:
    print(f"Workspace '{workspace_name}' not found.")



### testing getting around script 3 issue

# Create a new text block or get an existing one
if "script-6.py" not in bpy.data.texts:
    text_block = bpy.data.texts.new("script-6.py")
else:
    text_block = bpy.data.texts["script-6.py"]


with open('O:/Onedrive/Python_Blender/blend_auto_rig/Custom_Auto_Rig/Auto_rig_6 blend.py') as file:
    lines = file.read()
    # lines = [line.rstrip('\n') for line in file]
    # for line in file:
    #     print(line.rstrip())



# The text you want to paste
# text_to_paste = """Hello, this is some text 
# pasted into Blender's text editor."""

text_to_paste = lines

# Set the text for the text block
text_block.clear()  # Clear any existing text
text_block.write(text_to_paste)

# Ensure the text block is displayed in the text editor
for area in bpy.context.screen.areas:
    if area.type == 'TEXT_EDITOR':
        area.spaces.active.text = text_block
        break
else:
    # If no text editor is open, change an area to a text editor and display the text block
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':  # Change the 3D view to a text editor for demonstration purposes
            area.type = 'TEXT_EDITOR'
            area.spaces.active.text = text_block
            break



################################### this runs the script

# # Define the name of the text block containing the script
# text_block_name = "script-6.py"

# # Ensure the text block exists in Blender's Text Editor
# if text_block_name in bpy.data.texts:
#     text_block = bpy.data.texts[text_block_name]
    
#     # Execute the script in the text block
#     exec(text_block.as_string())
    
#     print(f"Executed script from {text_block_name}")
# else:
#     print(f"Text block '{text_block_name}' not found.")


