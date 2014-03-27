from django.test import TestCase

from forcompany.views import fill_info

class FillInfoTest(TestCase):

    def test_fillinfo_renders_fillinfo_template(self):
        response = self.client.get('/forcompany/fillinfo')
        self.assertTemplateUsed( response, 'fill_info.html' )