from __future__ import unicode_literals
import youtube_dl
import web

urls = (
    '/(.*)','Index'
) 
app = web.application(urls, globals())
web.config.debug = True
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')


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



class Index:

    def __init__(self):
        self.render = web.template.render('./templates/')
    
    def GET(self, name):
        planetNameList = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]
        androidOSnameList = ["Cupcake","Donut","Eclair","Froyo","Gingerbread","Honeycomb","Ice Cream Sandwich","Jelly Bean","KitKat","Lollipop","Marshmallow","Nougat","Nougat","Oreo","Oreo","Pie","Android 10","Android 11"]
        if (name== "planets"):
            return self.render.index(planetNameList)
        elif (name== "getvideo"):
            try:
                data = web.input()
                videoInfo = getVideo(data.url)
                return self.render.video(videoInfo)
            except:
                return self.render.index(planetNameList)
        else:
            return self



    def POST(self, name):
        return "post"

if __name__ == '__main__':app.run()

