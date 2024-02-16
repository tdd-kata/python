import subprocess

video_input_path = '../youtube/demo.mp4'
img_output_path = './thumbnail.jpg'

timestamp_minutes = '03'
subprocess.call(
    [
        'ffmpeg',
        '-i', video_input_path,
        '-ss', f'00:{timestamp_minutes}:00.000',
        '-vframes', '1',
        img_output_path
    ]
)
