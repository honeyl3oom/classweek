import json
from django.test import TestCase

from django.contrib.auth import authenticate
from forcompany.views import fill_info

SAMPLE_EMAIL = 'test@test.com'
SAMPLE_PASSWORD = '1234'

class ClassesInfomationTest(TestCase):

    def helper_response_result_success( self, response ):
        response_json = json.loads( response.content )
        self.assertEqual( response_json['result'], 'success' )

    def test_classes_get_sub_category_list(self):
        response = self.client.post('/classes/dance', data={} )
        # self.assertEqual( response.content , "" )
        self.helper_response_result_success( response )

    def test_classes_get_classes_list(self):
        response = self.client.post('/classes/dance/jazz', data={} )
        self.helper_response_result_success( response )

    # def test_classes_get_classes_in_overflow_page_num(self):
        # response = self.client.post('/classes/dance/jazz/9999', data={} )
        # {"error_message": "page end", "data": null, "result": "fail"}