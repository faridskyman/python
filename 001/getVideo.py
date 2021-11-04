import web
import youtube_dl


# web.py tutorial site: https://webpy.org/docs/0.3/tutorial


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


# To tell web.py our URL structure
service_urls = ('/yturl(/)?', 'yturl')
app = web.application(service_urls, globals())

# This is called when this web app is started
class yturl:
    def GET(self, _):
        try:
            data = web.input()
            yt_stream_url = get_youtube_stream_url(data.url)
            return {'url' : str(yt_stream_url) }
        except:
            return web.badrequest() 


# Tell web.py to start serving web pages:
if __name__ == "__main__":
    app.run()
