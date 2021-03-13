from django.test import TestCase

# Create your tests here.

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """get / must retorn status code 200"""
        self.assertEqual(200,self.response.status_code)

    def test_template(self):
        """must use index.html"""
        self.assertTemplateUsed(self.response,'index.html')

