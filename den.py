import sys, os, re

if __name__ == '__main__':

    # from input, find url in format '...playlist\.m3u8'
    link_url = sys.argv[1]
    playlist_url = re.match(r'.*playlist\.m3u8', link_url).group()
    
    # from url, find course name and date, e.g. 'CSCI570_19700101'
    m = re.search(r'([A-Z]+[0-9]+_)([0-9]+)', link_url)
    video_name = m.group(1) + m.group(2)[-8:] + '.mp4'
    
    # use ffmpeg to download
    os.system('ffmpeg -i %s -c copy -bsf:a aac_adtstoasc %s' % (playlist_url, video_name))
