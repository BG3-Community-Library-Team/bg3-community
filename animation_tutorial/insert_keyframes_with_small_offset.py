import bpy

# Set the start (0) and end frames here depending on the length of your animation
start_frame = 0
end_frame = 280
# Small transformation amount for detectability by lslib
small_offset = 0.0001

# Set the skeleton rig name here
armature = bpy.data.objects.get("SK_HUM_F")

if armature is None:
    bpy.context.window_manager.popup_menu(lambda self, context: self.layout.label(text="Armature 'SK_HUM_F' not found."), 
                                          title="Notification", icon='INFO')
else:
    # Ensure we are in Pose Mode
    bpy.context.view_layer.objects.active = armature
    if bpy.context.object.mode != 'POSE':
        bpy.ops.object.posemode_toggle()
    
    # Access only selected bones in Pose Mode
    selected_bones = [bone for bone in armature.pose.bones if bone.bone.select]

    if not selected_bones:
        bpy.context.window_manager.popup_menu(lambda self, context: self.layout.label(text="No bones selected in Pose Mode."), 
                                              title="Notification", icon='INFO')
    else:
        # Insert Loc/Rot keyframes at the start frame
        bpy.context.scene.frame_set(start_frame)
        for bone in selected_bones:
            bone.keyframe_insert(data_path="location", frame=start_frame)
            bone.keyframe_insert(data_path="rotation_euler", frame=start_frame)

        # Insert Loc/Rot keyframes at the end frame with a small offset
        bpy.context.scene.frame_set(end_frame)
        for bone in selected_bones:
            # Apply a small offset to location and rotation (Euler)
            bone.location.x += small_offset
            bone.rotation_euler[0] += small_offset 
            bone.keyframe_insert(data_path="location", frame=end_frame)
            bone.keyframe_insert(data_path="rotation_euler", frame=end_frame)
            
            bone.location.x -= small_offset
            bone.rotation_euler[0] -= small_offset

        # Reset frame back to start frame
        bpy.context.scene.frame_set(start_frame)

    bpy.context.window_manager.popup_menu(lambda self, context: self.layout.label(text="Offset script completed."), 
                                          title="Notification", icon='INFO')
