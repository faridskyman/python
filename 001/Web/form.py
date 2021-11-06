from __future__ import unicode_literals
import youtube_dl
import web

urls = ('/(.*)','Index') #this is a regex expression

app = web.application(urls, globals())

web.config.debug = True

# this is needed as to fix error "execution of 'Constant' statements is denied"
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

def getVideo(in_url, format):
    #format = "18"
    ydl_opts = {
        "forceurl" : True, #Force printing final URL.
        "quiet" : True, #dont show verbose message
        "simulate" : True,  #dont download file
        "call_home" : False, #dont contact youtubedl server for debugging
        #"format": format
        #"format": "18" #works
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




class Index:

    #define the html template folder
    def __init__(self):
        self.render = web.template.render('./templates/')
        # on windows, when i type path to template, above is what is shown, and that works
        #   if your path is wrong ('templates/'), you get error 'No template named index'
        # also u need to call this from the web folder (where ur index.py is located.)
    
    def GET(self, name):
        # name <-- is this part localhost:8080/{name}
        # so we can load different list based on name..
        if(name == "getvideo"):
            try:
                data = web.input()
                videoInfo = getVideo(data.yturl, "best[ext=mp4]")
                return self.render.video(videoInfo)
            except Exception as e: 
                #print(e)
                return self.render.index(["Error, video info could be missing."])    
        elif(name == "getvideostream"):
            try:
                data = web.input()
                videoInfo = getVideo(data.yturl, data.formatID)
                return self.render.video(videoInfo)
            except:
                return self.render.index(["Error, video info could be missing."])   
        else:
            return self.render.form("")
        #render.index <-- 'index' is the html file in 'templates' folder
        #return "Hello World"


    def POST(self, name):
        #data = web.data()
        data = web.input()
        yturl = data['yturl']
        #return "posted" + txtName
        raise web.seeother('/getvideo?yturl=' + yturl)


if __name__ == '__main__':app.run()

