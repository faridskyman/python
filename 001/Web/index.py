# WHen running this example, change the url from http://0.0.0.0:8080 to http://localhost:8080
# [ctrl] + [c] to kill the web server *gracefully*
# https://webpy.org/

import web

urls = ('/(.*)','Index') #this is a regex expression
#/ <--start
# () <-- regex will be in the parenthesis
#   . <- any characters
#   * <- 0 or more char
# so when the web server loads localhost:8080/{if empty or any characters is passed}
#   if characters is passed that is "name" that will be passed to get.

app = web.application(urls, globals())

web.config.debug = True

# this is needed as to fix error "execution of 'Constant' statements is denied"
#   https://stackoverflow.com/questions/58518448/how-to-fix-execution-of-constant-statements-is-denied-error
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')


class Index:

    #define the html template folder
    def __init__(self):
        #self.render = web.template.render('templates/')
        self.render = web.template.render('./templates/')
        # on windows, when i type path to template, above is what is shown, and that works
        #   if your path is wrong ('templates/'), you get error 'No template named index'
        # also u need to call this from the web folder (where ur index.py is located.)
    
    def GET(self, name):
        # name <-- is this part localhost:8080/{name}
        # so we can load different list based on name..
        #list of planets
        planetNameList = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]
        #list of android OS
        androidOSnameList = ["Cupcake","Donut","Eclair","Froyo","Gingerbread","Honeycomb","Ice Cream Sandwich","Jelly Bean","KitKat","Lollipop","Marshmallow","Nougat","Nougat","Oreo","Oreo","Pie","Android 10","Android 11"]
        
        #if URL is http://localhost:8080/planets, then show planets list else show android os list.

        if (name== "planets"):
            return self.render.index(planetNameList)
        else:
            return self.render.index(androidOSnameList)



        
        #render.index <-- 'index' is the html file in 'templates' folder
        #return "Hello World"


    def POST(self, name):
        return "post"

if __name__ == '__main__':app.run()

