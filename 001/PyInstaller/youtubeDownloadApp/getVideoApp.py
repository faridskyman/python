from __future__ import unicode_literals
import re
import youtube_dl
#   import urllib
from urllib import request


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


def getVideo(in_url, formatID):
    ydl_opts = {
        "forceurl" : True, #Force printing final URL.
        "quiet" : True, #dont show verbose message
        "simulate" : True,  #dont download file
        "call_home" : False, #dont contact youtubedl server for debugging
        "format": formatID
        #"format": "best[ext=mp4]" #works
        #"format": "best" #works
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(in_url, download=False)
       
        if 'entries' in result:
            video = result['entries'][0]
        else:
            video = result
       
        video_url = video['url']
        return video

def printList(myList, header):
    print(f"--{header}--------")
    print("  ID,    Format,                  Size,  Vcodec/ Acodec,      Ext")
    print("['140', '140 - audio only (tiny)', 3.8, 'none', 'mp4a.40.2', 'm4a']")
    for f in myList:
        print (f)

def downloadStream(parsedURL, filename):
    request.urlretrieve(parsedURL, filename)

def getFilename(strData):
    _title = strData['title']
    # replace space with underscore
    _title = _title.replace(" ", "_")
    _title = _title.replace("\"", "_")
    _title = _title.replace("\'", "_")
    _title = _title.replace("<", "_")
    _title = _title.replace(">", "_")
    _title = _title.replace("`", "_")
    _type = strData['ext']
    return _title+"."+_type


inUrl = input("Paste Youtube URL: ")
#inUrl = "https://www.youtube.com/watch?v=rr2XfL_df3o"
streamData = getVideo(inUrl,"best[ext=mp4]")

print(streamData['title'])

mediaType = int(input("Type 1 for Audio, 2 for Video only, 3 for Video with Audio: "))



audioOnlyList=[]
videoOnlyList=[]
videoList=[]

#for each format get the format_id
for f in streamData['formats']:
    #print (f['format_id'])
    try:
        filesize = round(float(f['filesize'])/1024/1024,1)
    except:
        filesize = float(0)

    formatRec = [f['format_id'],f['format'],filesize,f['vcodec'],f['acodec'],f['ext']]
    #formatRec = [f['format_id'],f['format'],filesize,f['ext']]

    try:
        if((f['vcodec'] != 'none') and (f['acodec'] != 'none')):
            videoList.append(formatRec)
        
        if((f['vcodec'] == 'none') and (f['acodec'] != 'none')):
            audioOnlyList.append(formatRec)

        if((f['vcodec'] != 'none') and (f['acodec'] == 'none')):
            videoOnlyList.append(formatRec)        
    except:
        audioOnlyList.append(formatRec)
        
if(mediaType==1):
    printList(audioOnlyList,"List with only audio")
elif(mediaType==2):
    printList(videoOnlyList,"List with only video")
else:    
    printList(videoList,"List with audio and video")



userformatID=input("Enter in FormatID to download: ")
streamData = getVideo(inUrl,userformatID)
#print(streamData['url'])
print("downloading...")
filename=getFilename(streamData)
downloadStream(streamData['url'],filename)
input("press any key to exit")