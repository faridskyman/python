from __future__ import unicode_literals
import youtube_dl


# web.py tutorial site: https://webpy.org/docs/0.3/tutorial
# https://github.com/ytdl-org/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312
# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl
# https://www.programcreek.com/python/example/98358/youtube_dl.YoutubeDL

#This is just a function
def get_youtube_stream_url(in_url):
    ydl_opts = {"forceurl" : True, "quiet" : True, "simulate" : True, "call_home" : False, "format":"best[ext=mp4]/best[ext=3gp]"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(in_url, download=False)
        if 'entries' in result:
            video = result['entries'][0]
        else:
            video = result

        video_url = video['url']
        return video_url


def getVideo(in_url):
    ydl_opts = {
        "forceurl" : True, #Force printing final URL.
        "quiet" : True, #dont show verbose message
        "simulate" : True,  #dont download file
        "call_home" : False, #dont contact youtubedl server for debugging
        "format": "best[ext=mp4]" #works
        #"format": "best" #works
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(in_url, download=False)
    
        if 'entries' in result:
            video = result['entries'][0]
        else:
            video = result
        
        video_url = video['url']
        #return video_url
        return video

inUrl = input("Paste Youtube URL: ")
#inUrl = "https://www.youtube.com/watch?v=gFAU2XatRF4"
#streamData = get_youtube_stream_url(inUrl)
streamData = getVideo(inUrl)
#print(streamData)
print(f"Title: {streamData['title']} \nFormat: {streamData['format']} \nURL: {streamData['url']}")