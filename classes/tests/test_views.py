import json
from django.test import TestCase
from foradmin.tests.test_views import UserSessionTest

from django.contrib.auth import authenticate
from forcompany.views import fill_info

SAMPLE_EMAIL = 'test@test.com'
SAMPLE_PASSWORD = '1234'

class ClassesInfomationTest(TestCase):

    def setUp(self):

        # insert dummy data
        self.assertTrue(self.helper_check_response_result(self.client.get('/classes/import/category')))
        self.assertTrue(self.helper_check_response_result(self.client.get('/classes/import/subcategory')))
        self.assertTrue(self.helper_check_response_result(self.client.get('/classes/import/company')))
        self.assertTrue(self.helper_check_response_result(self.client.get('/classes/import/classes')))
        self.assertTrue(self.helper_check_response_result(self.client.get('/classes/import/schedule')))

        response = self.client.post('/classes/music/acoustic_guitar')
        response_dict = json.loads(response.content)
        self.first_classes_item = response_dict['data'][0]

    # helper function part ----- start

    def helper_check_response_result(self, response, result_string='success'):
        response_dict = json.loads(response.content)
        return response_dict['result']==result_string

    # helper function part ----- end

    # test function part ----- start

    def test_get_sub_category_list(self):
        self.assertTrue(self.helper_check_response_result(self.client.post('/classes/music')))

    def test_get_classes_list(self):
        self.assertTrue(self.helper_check_response_result(self.client.post('/classes/music/acoustic_guitar')))

    def test_get_classes_detail(self):
        # print '/classes/'+str(first_classes_item['id'])+'/'+str(first_classes_item['schedule_id'])
        self.assertTrue(self.helper_check_response_result(self.client.post('/classes/'+str(self.first_classes_item['id'])+'/'+str(self.first_classes_item['schedule_id']))))

    def test_classes_inquire(self):
        self.assertFalse(self.helper_check_response_result(self.client.post('/classes/'+str(self.first_classes_item['id'])+'/inquire')))

        UserSessionTest.helper_registration(self)
        UserSessionTest.helper_login(self)

        self.assertFalse(self.helper_check_response_result(self.client.post('/classes/'+str(self.first_classes_item['id'])+'/inquire')))


    # test function part ----- end


    # def test_classes_get_sub_category_list(self):
    #     response = self.client.post('/classes/dance', data={} )
    #     # self.assertEqual( response.content , "" )
    #     self.helper_response_result_success( response )
    #
    # def test_classes_get_classes_list(self):
    #     response = self.client.post('/classes/dance/jazz', data={} )
    #     self.helper_response_result_success( response )

    # def test_classes_get_classes_in_overflow_page_num(self):
        # response = self.client.post('/classes/dance/jazz/9999', data={} )
        # {"error_message": "page end", "data": null, "result": "fail"}

    # def test_classes_inquire_about_classes(self):
    #     response = self.client.post('/classes/')