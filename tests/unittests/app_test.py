 
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
        
    def test_generate_recommendations_with_empty_payload(self):
        data = {}
        response = self.app.post('/api/recommend', json=data)
        self.assertEqual(response.status_code, 400)
        print(response.get_json())
        
    def test_get_playlists_by_track_with_empty_payload(self):
        data = {}
        response = self.app.post('/api/get-playlists-by-song', json=data)
        self.assertEqual(response.status_code, 400)
        
    def test_create_response(self):
        playlist_ids = [1, 2, 3]
        with app.app_context():
            response = create_response(playlist_ids)
        expected_response_data = {
            'playlist_ids': playlist_ids,
            'version': '1.0',
            'model_date': '2023-11-02'
        }
        self.assertEqual(response.get_json(), expected_response_data)    

    def test_get_recommendations_response(self):
        data = {'songs': ['song1', 'song2']}
        response = self.app.post('/api/recommend', json=data)

        self.assertIn('playlist_ids', response.get_json())
        self.assertIn('version', response.get_json())
        self.assertIn('model_date', response.get_json())

        self.assertEqual(response.status_code, 200)

    def test_get_playlists_by_track(self):
        data = {'song': 'song1'}
        response = self.app.post('/api/get-playlists-by-song', json=data)
        print(response.get_json())
        self.assertEqual(response.status_code, 200)
        self.assertIn('playlist_ids', response.get_json())
        self.assertIn('version', response.get_json())
        self.assertIn('model_date', response.get_json())

if __name__ == '__main__':
    unittest.main()