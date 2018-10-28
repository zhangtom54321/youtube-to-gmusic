'''
Tom Zhang
October 2018

'''

from pytube import Playlist
from os import listdir
from os.path import isfile, join
import moviepy.editor as mp
import os
from gmusicapi import Musicmanager
from gmusicapi import Mobileclient
import datetime
import shutil

mypath = "music"
default_url = "https://www.youtube.com/playlist?list=PLMC9KNkIncKtGvr2kFRuXBVmBev6cAJ2u"

# Setting up directory
shutil.rmtree(mypath, ignore_errors=True)
os.mkdir(mypath)

# Get URL of playlist
url = input("Enter Youtube Playlist link (press enter for default): ")
if (url == ""):
    url = default_url

# Setting up Google Music
api = Mobileclient()
logged_in = False
while (not logged_in):
    email = input("\nEmail: ")
    password = input("Password: ")
    logged_in = api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)
mm = Musicmanager()
mm.login()

# Downloads all videos in playlist as MP4 files
print("\n\nDownloading Videos")
pl = Playlist(url)
pl.download_all(mypath)

# Get list of all files
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

# Converts each MP4 to audio
num_digits = len(str(len(onlyfiles))) # Determines the number of letters to take off the beginning of the audio file name
print("\n\nConverting to Audio")
for vidName in onlyfiles:
    #clip = mp.VideoFileClip(mypath + "/" + vidName)

    #audioName = vidName.split(".mp4")[0]
    #clip.audio.write_audiofile(mypath + "/" + audioName+".mp3")
    with mp.VideoFileClip(mypath + "/" + vidName) as clip:
        audioName = vidName.split(".mp4")[0][num_digits:]
        clip.audio.write_audiofile(mypath + "/" + audioName+".mp3")
    os.remove(mypath + "/" + vidName)

# Uploading songs
print("\n\nUploading songs to Google Music")
audiofiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
audiofiles = [mypath+"/"+f for f in audiofiles]
print(audiofiles)
results = mm.upload(audiofiles, enable_matching=False, enable_transcoding=True)
print(results)


# Getting song IDs
uploaded = {**results[0], **results[1]}
not_uploaded = results[2]
print(uploaded)
print(not_uploaded)

ids = []
for audiofile in audiofiles:
    try:
        ids.append(uploaded[audiofile])
        #print("Uploaded: " + id)
    except KeyError:
        ids.append(not_uploaded[audiofile].split('ALREADY_EXISTS')[1][1:-1])
        #print("Not Uploaded: " + id)
print(ids)

# Creating new Playlist
print("\n\nCreating new playlist")
playlistID = api.create_playlist(str(datetime.datetime.now().date())+" Playlist", description="Automatically created by Tom Zhang's Python script. View the code at https://github.com/zhangtom54321/youtube-to-gmusic")
print(playlistID)

# Adding songs to playlist
print("\n\nAdding songs to playlist")
api.add_songs_to_playlist(playlistID, ids)
