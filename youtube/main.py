from pytube import YouTube
from pytube.cli import on_progress

# link: str = 'https://youtu.be/3bAlS8YSffc'
link: str = input('enter url:')

yt = YouTube(url=link)
# 이미 파일이 있으면 진행도가 표시되지 않는 듯?
yt.register_on_progress_callback(on_progress)

video = yt.streams \
    .filter(progressive=True, file_extension='mp4') \
    .order_by('resolution') \
    .desc() \
    .first()

video.download()
