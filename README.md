# youtube-to-gmusic
A Python script that converts a YouTube playlist into a Google Play Music playlist. Just something that I wrote in a few hours one weekend that allows me to play music offline. If you want to convert a Spotify playlist into a Google Play Music playlist, use [this tool](http://www.playlist-converter.net/#/) to convert the Spotify playlist into a YouTube playlist first, then use the script.

It works by first downloading the YouTube playlist as MP4 video files using [PyTube](https://github.com/nficano/pytube), then converting the videos into MP3 files using [MoviePy](https://github.com/Zulko/moviepy). It then uploads the MP3 files as songs to Google Play Music using [gmusicapi](https://github.com/simon-weber/gmusicapi) and adds them to a new playlist.

## Setup
You will need to pip install some stuff:
```
pip install pytube
pip install moviepy
pip install gmusicapi
```
The first time you run the program on a machine, run:
```
from gmusicapi import Musicmanager
mm = Musicmanager()
mm.perform_oauth()
```

## Usage
Clone the repository:
```
git clone https://github.com/zhangtom54321/youtube-to-gmusic
```
Navigate to the repository, and run the script:
```
cd youtube-to-gmusic
python youtube-to-gmusic.py
```
Enter the URL of the YouTube playlist
```
>>> Enter Youtube Playlist link (press enter for default): <your youtube playlist url>
```
and the email & password of the Google account you want the playlist to be added to:
```
>>> Email: <your email>
>>> Password: <your password>
```
That's it! Sit back and relax until the script finishes running, then sit back and listen to the new playlist on your Google Music account.

## Future Changes
- Hide password
- Enable Scan & Match
- Add album art
- Add track #
