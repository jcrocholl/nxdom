from django.test import TestCase


class ClientTest(TestCase):

    def test_index(self):
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)

    def test_anonymous(self):
        response = self.client.post('/feedback/',
            {'page': '/', 'message': 'test message'})
        self.assertRedirects(response, '/')
