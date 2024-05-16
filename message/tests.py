from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class MessagePageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get('/message/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_by_name(self):
        response = self.client.get(reverse('message'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name(self):
        response = self.client.get(reverse('message'))
        self.assertTemplateUsed(response, 'home.html')
    
    def test_template_content(self):
        response = self.client.get('/message/')
        self.assertContains(response, '<p>Welcome to the home page!</p>')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

# Path: message/views.py