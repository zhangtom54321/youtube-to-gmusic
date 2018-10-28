# youtube-to-gmusic
A Python script that converts a YouTube playlist into a Google Play Music playlist. Just something that I wrote in a few hours one weekend that allows me to play music offline. If you want to convert a Spotify playlist into a Google Play Music playlist, use [this tool](http://www.playlist-converter.net/#/) to convert the Spotify playlist into a YouTube playlist first, then use the script.

## Setup
You will need to pip install some stuff:
```
pip install gmusicapi
```
The first time you run the program on a machine, run:
```
from gmusicapi import Musicmanager
mm = Musicmanager()
mm.perform_oauth()
```

## Future Changes
- Hide password when typing
- Enable Scan & Match
- Add album art
- Add track #
