# https://webpy.org/cookbook/url_handling

import web

urls = (
    "/users/list/(.+)", "list_users", #http://localhost:8080/users/list/farid
    "/tasks/post/(.+)", "postS"
) 

app = web.application(urls, globals())
web.config.debug = True
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')





class list_users:
    # `name` has the matched content of `(.+)`
    def GET(self, name):
        return "Listing info about user: {0}".format(name)


class postS:
    def GET(self, name=None):
        return "post function for {0}.".format(name)




if __name__ == '__main__':app.run()

