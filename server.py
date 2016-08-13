import json
import time

import cherrypy

class Server(object):

    @cherrypy.expose
    def index(self):
        return "Oh hi there!"

    @cherrypy.expose
    def variantsearch(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        def streamer():
            for idx in range(10):
                time.sleep(1)
                variant = {"id": "variant-{}".format(idx)}
                yield json.dumps(variant)
        return streamer()
    variantsearch._cp_config = {'response.stream': True}


if __name__ == '__main__':
    cherrypy.quickstart(Server())
