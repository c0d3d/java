"""
 ** This data and information is proprietary to, and a valuable trade secret
 ** of, Basis Technology Corp.  It is given in confidence by Basis Technology
 ** and may only be used as permitted under the license agreement under which
 ** it has been distributed, and in no other way.
 **
 ** Copyright (c) 2014 Basis Technology Corporation All rights reserved.
 **
 ** The technical data and information provided herein are provided with
 ** `limited rights', and the computer software provided herein is provided
 ** with `restricted rights' as those terms are defined in DAR and ASPR
 ** 7-104.9(a).
"""

import unittest
import logging
from rosette.api import API, ResultFormat, LanguageDetectionParameters
import os
import sys

logging.basicConfig(level=logging.DEBUG)

class RliTestCase(unittest.TestCase):
    def test_info(self):
        port = os.environ['MOCK_SERVICE_PORT']
        url = 'http://localhost:' + port + '/raas'
        url = "http://jugmaster.basistech.net/rest/v1"
        logging.info("URL " + url)
        lid = API(service_url = url).language_detection()
        result = lid.info()
        self.assertIsNotNone(result['requestId'])

    def test_adm_detection(self):
        port = os.environ['MOCK_SERVICE_PORT']
        url = 'http://localhost:' + port + '/raas'
        url = "http://jugmaster.basistech.net/rest/v1"
        logging.info("URL " + url)
        print >>sys.stderr, "URL RLI TestCase", url
        params = LanguageDetectionParameters()
        params.content = "Yes, Ma'm! Green eggs and ham?  I am Sam;  I filter Spam."
        params.contentType = "application/json" #"text/plain"
        params.unit = "doc"
        print >>sys.stderr, params.__dict__
        # the mock services can't respond to the individual params.
        print >>sys.stderr,"LDP test_adm_detection:", params.__dict__
        lid = API(service_url = url).language_detection()
        result = lid.detect(params, ResultFormat.ROSETTE)
#        result = lid.detect(params, None)
