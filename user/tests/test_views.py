from django.test import TestCase

from forcompany.views import fill_info

class UserAuthenticationTest(TestCase):

    def test_user_sign_up(self):
        self.client.post('/user/registration', 
            data={'name': 'ttt', 'email':'ttt@ttttt.com', 'password':'ttt' }
        )
