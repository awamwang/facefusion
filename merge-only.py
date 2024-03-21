import facefusion
from facefusion.ffmpeg import extract_frames, compress_image, merge_video, restore_audio, replace_audio

facefusion.globals.output_video_encoder = 'libx264'
facefusion.globals.output_video_quality = 80
facefusion.globals.output_video_preset = 'veryfast'

facefusion.globals.temp_frame_format = 'jpg'
merge_video('/tmp/gradio/5724874b3f7c1134658a7b1ad9751ec3b5e1a60d/001-Yui Kawagoe.mp4', '1920x1080', 30)