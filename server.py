import json
import time

import cherrypy
import google.protobuf.json_format as json_format

import datamodel.variant
import ga4gh.variant_service_pb2 as variant_service_pb2

class Server(object):

    @cherrypy.expose
    def index(self):
        return "Oh hi there!"

    @cherrypy.expose
    def variantsearch(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        reference = 'NCBI37'
        start = 0
        end = 10000000
        
        def streamer(reference_name, start, end):
            for idx, rec in enumerate(datamodel.variant.getPysamVariants(
                    reference_name, '1', start, end)):
                variant = datamodel.variant.convertVariant(rec, None)
                if idx > 5: break
                yield json_format.MessageToJson(variant)

        return streamer(reference, start, end)
    variantsearch._cp_config = {'response.stream': True}


if __name__ == '__main__':
    cherrypy.quickstart(Server())
