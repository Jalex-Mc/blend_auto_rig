import bpy

rig = bpy.data.objects['Female Transfer Rig']
bpy.context.view_layer.objects.active = bpy.data.objects['Female Transfer Rig']
bpy.ops.object.mode_set(mode='EDIT')
bone = bpy.data.armatures['Female Transfer Rig'].edit_bones['pelvis']
bone.select_head = True

bpy.ops.armature.extrude_move(TRANSFORM_OT_translate={"value": (0,0.3,0)})
