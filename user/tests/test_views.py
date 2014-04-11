import json
from django.test import TestCase

from django.contrib.auth import authenticate
from forcompany.views import fill_info

SAMPLE_EMAIL = 'test@test.com'
SAMPLE_PASSWORD = '1234'

class UserAuthenticationTest(TestCase):

    # def decorator_login_before( func ):
    #     @wraps( func )
    #     def wrap( *args, **kwargs ):

    def helper_registraiton( self, email, password ):
        self.client.post('/user/registration', 
            data={'email': email, 'password':password, 'password_confirm':password }
        )

    def helper_response_result_success( self, response ):
        response_json = json.loads( response.content )
        self.assertEqual( response_json['result'], 'success' )

    def test_user_registration(self):
        email = SAMPLE_EMAIL
        password = SAMPLE_PASSWORD
        password_confirm = SAMPLE_PASSWORD
        response = self.client.post('/user/registration', 
            data={'email': email, 'password':password, 'password_confirm':password_confirm }
        )
        self.helper_response_result_success( response )
        user = authenticate( username=email, password=password)
        self.assertIsNotNone( user )

    def test_user_login(self):
        email = SAMPLE_EMAIL
        password = SAMPLE_PASSWORD
        self.helper_registraiton( email, password )
        response = self.client.post('/user/login', 
            data={'email': email, 'password':password }
        )
        self.helper_response_result_success( response )

    def test_user_logout(self):
        response = self.client.post('/user/logout', 
            data={ }
        )
        self.helper_response_result_success( response )