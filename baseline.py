import json

import google.protobuf.json_format as json_format

import datamodel.variant
import ga4gh.variant_service_pb2 as variant_service_pb2

def createFile():
    reference = 'NCBI37'
    start = 0
    end = 10000000
    
    with open('variants.json', 'w') as out_file:
        for idx, rec in enumerate(datamodel.variant.getPysamVariants(
            reference, '1', start, end)):
            variant = datamodel.variant.convertVariant(rec, None)
            out_file.write(json_format.MessageToJson(variant))
    print("Done")

if __name__ == '__main__':
    createFile()
