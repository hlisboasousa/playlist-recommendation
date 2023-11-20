 
import unittest
from unittest.mock import MagicMock
from api.app import app, create_response, generate_recommendations, get_playlists_by_track

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_health_check(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "Server running ok!")

    def test_generate_recommendations(self):
        # Mock the request
        data = {'songs': ['song1', 'song2']}
        response = self.app.post('/api/recommend', json=data)

        self.assertIn('playlist_ids', response)
        self.assertIn('version', response)
        self.assertIn('model_date', response)

        self.assertEqual(response.status_code, 200)

    def test_get_playlists_by_track(self):
        # Mock the request
        data = {'song': 'song1'}
        response = self.app.post('/api/get-playlists-by-song', json=data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('playlist_ids', response)
        self.assertIn('version', response)
        self.assertIn('model_date', response)

    def test_create_response(self):
        playlist_ids = [1, 2, 3]
        response = create_response(playlist_ids)

        # Add your assertions based on expected behavior
        expected_response_data = {
            'playlist_ids': playlist_ids,
            'version': '1.0',
            'model_date': '2023-11-02'
        }
        self.assertEqual(response.get_json(), expected_response_data)

    def test_exception_handling(self):
        # Mock the request with a payload that causes an exception
        data = {'invalid_key': 'invalid_value'}
        response = self.app.post('/api/recommend', json=data)

        # Add your assertions based on expected behavior
        self.assertEqual(response.status_code, 500)
        # Add more assertions as needed based on the expected behavior of the endpoint

if __name__ == '__main__':
    unittest.main()