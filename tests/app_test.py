import unittest
import json
from your_flask_app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_generate_recommendations(self):
        data = {
            'tracks': ['track1', 'track2']
        }
        response = self.app.post('/api/recommend', json=data)
        data = json.loads(response.get_data(as_text=True))

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the keys in the response data
        self.assertIn('playlist_ids', data)
        self.assertIn('version', data)
        self.assertIn('model_date', data)

    def test_get_playlists_by_track(self):
        data = {
            'song': 'track1'
        }
        response = self.app.post('/api/get-playlists-by-song', json=data)
        data = json.loads(response.get_data(as_text=True))

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the keys in the response data
        self.assertIn('playlist_ids', data)
        self.assertIn('version', data)
        self.assertIn('model_date', data)

if __name__ == '__main__':
    unittest.main()