from django.test import TestCase


class ClientTest(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_anonymous(self):
        response = self.client.get('/search/json/?left=a')
        self.assertEqual(response.status_code, 200)
