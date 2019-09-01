from __future__ import unicode_literals
import youtube_dl
import re
import os


# Get links from html
text = ''
with open('music.html', 'r') as lines:
    for line in lines:
        text += line

start_link = '<a class="yt-simple-endpoint style-scope ytd-playlist-video-renderer" href="'
end_link = '&amp;list='
links = re.findall('{}(.*?){}'.format(re.escape(start_link), re.escape(end_link)), text)
print(links)

# Download data and config
download_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320'
    }]
}

# Music directory
if not os.path.exists('Music'):
    os.mkdir('Music')
else:
    os.chdir('Music')

errors = []

# Download music
with youtube_dl.YoutubeDL(download_options) as dl:
    for song_url in links:
        try:
            dl.download([song_url])
        except:
            errors.append(song_url)


