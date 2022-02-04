from pytube import YouTube
from eyed3 import id3
from moviepy.editor import *
import os

from gettag import gettag

SAVE_PATH = r"C:\Users\gregd\OneDrive\Spotify"
DESKTOP = r"C:\Users\gregd\OneDrive\Desktop"
#DESKTOP = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

while True:
    try:
        yt = YouTube(input("YouTube Link: "))
        break
    except:
        print("Connection Error. Please enter a valid YouTube URL.")

title = gettag("Song Title: ", "title")
album_artist = gettag("Artist: ", "artist")
features = input("Features (Separate with comma and space): ")
album = gettag("Album: ", "album")
list = features.split(", ")
num_features = len(list)
if(features != ""):
    if(num_features == 1): title = title + " (feat. " + list[0] + ")" 
    elif(num_features == 2): title = title + " (feat. " + list[0] + " and " + list[1] + ")"
    else:
        list[-1] = "and " + list[-1]
        title = title + " (feat. " + ", ".join(list) + ")"
    features = ", " + features

yt.title = 'dl'
mp4file = yt.streams.get_lowest_resolution()
try:
    mp4file = mp4file.download(DESKTOP)
except:
    print("Download Error. Try Again.")
    quit()

mp3_spotify = SAVE_PATH + '\\' + title + ".mp3"
mp3_desktop = DESKTOP + '\\' + title + ".mp3"
video = VideoFileClip(mp4file)
video.audio.write_audiofile(mp3_desktop, verbose=False, logger=None)
video.close()
os.remove(mp4file)

tags = id3.Tag()
tags.parse(mp3_desktop)
tags.title = title
tags.album_artist = album_artist
tags.artist = album_artist + features
tags.album = album
tags.save()

os.replace(mp3_desktop, mp3_spotify)
print("Download Complete!")