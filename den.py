#!/usr/bin/env python3
import sys, os, re

if __name__ == '__main__':

	# from input, find url in format '...playlist\.m3u8'
    link_url = sys.argv[1]
    playlist_url = re.match(r'.*playlist\.m3u8', link_url).group()
    
    # from url, find course name and date, e.g. 'CSCI570_19700101'
    m = re.search(r'([A-Z]+[0-9]+_)([0-9]+)', link_url)
    video_name = m.group(1) + m.group(2)[-8:] + '.mp4'
    
    # use _ffmpeg_ to download
    os.system('ffmpeg -i %s -c copy -bsf:a aac_adtstoasc ~/Downloads/%s' % (playlist_url, video_name))

    # use _autosub_ to translate subtitle, if possible
    # install _autosub_ first (only works for python2)
    # try:  	
    #     os.system('autosub ~/Downloads/%s' % (video_name))
    # except Exception as e:
    # 	raise e
