# DEN_Downloader2

The simplest video downloader for USC DEN.

* Input: `.m3u8` URL (copied from DEN)
* Output: `.mp4` video file

## Prerequisites
* Python
* [FFmpeg](https://www.ffmpeg.org/) (e.g. `brew install ffmpeg`) 

## Usage
1. Log in to DEN, and open the page of your lecture video
2. Under the video, right click `Android/IOS` button, then click `Copy Link Address`
3. Download [`den.py`](https://raw.githubusercontent.com/JiashengWu/DEN_Downloader2/master/den.py) to your local directory
4. Open a Terminal, `cd` to your directory, then run `python den.py [LINK_ADDRESS]`
5. Wait and be patient :-)

### Recommended Follow-ups:
* Auto-generate subtitles w/ [Autosub](https://github.com/agermanidis/autosub)
* For macOS, play w/ [IINA](https://iina.io/)
* For Windows, play w/ [PotPlayer](https://potplayer.daum.net/)

## Acknowledgements
* [latera1n/DEN-Video-Downloader](https://github.com/latera1n/DEN-Video-Downloader)
