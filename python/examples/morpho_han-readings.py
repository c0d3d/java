# -*- coding: utf-8 -*-

'''
Example code to call Rosette API to get Chinese readings fo words in a piece of text.
'''

import argparse
import pprint
import sys

# enable imports from rosette.api
sys.path += '../../'

from rosette.api import API, RosetteParameters, MorphologyOutput

parser = argparse.ArgumentParser(description='Accept Rosette API key')
parser.add_argument('--key', required=True, help='Rosette API key')
parser.add_argument('--service_url', nargs='?', help='Optional user service URL')
args = parser.parse_args()

# Create an API instance
if args.service_url:
    api = API(service_url=args.service_url, user_key=args.key)
else:
    api = API(user_key=args.key)

params = RosetteParameters()
params["content"] = u"北京大学生物系主任办公室内部会议"
op = api.morphology(MorphologyOutput.HAN_READINGS)
result = op.operate(params)

pprint.pprint(result)
