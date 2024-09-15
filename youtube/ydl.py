import youtube_dl

# list format
# python -m youtube_dl -vF qzC9xoUVkvs
# python -m youtube_dl -vF https://youtu.be/qzC9xoUVkvs

# download by format code
# python -m youtube_dl -vf <format_code> qzC9xoUVkvs

# link: str = 'https://youtu.be/qzC9xoUVkvs'
link: str = input('enter url:')

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

