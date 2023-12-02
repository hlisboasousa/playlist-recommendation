 
import unittest
from api.app import app, create_response, generate_recommendations, get_playlists_by_song
class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.context = app.app_context()
        self.context.push()

#   HEALTH CHECK
    def test_health_check(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "Server running ok!")

#   RECOMMENDATIONS
    def test_generate_recommendations_with_empty_payload(self):
        data = {}
        response = self.app.post('/api/recommend', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_generate_recommendations_with_invalid_payload(self):
        data = {'invalid_key': 'song1'}
        response = self.app.post('/api/recommend', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())
        self.assertEqual(response.get_json()['error'], 'Missing required key: songs')

    def test_generate_recommendations_with_no_matches(self):
        data = {'songs': ['nonexistent_song']}
        response = self.app.post('/api/recommend', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('playlist_ids', response.get_json())
        self.assertEqual(response.get_json()['playlist_ids'], [])

    def test_generate_recommendations_with_large_payload(self):
        data = {'songs': ['song' + str(i) for i in range(100)]}
        response = self.app.post('/api/recommend', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('playlist_ids', response.get_json())
        self.assertIn('version', response.get_json())
        self.assertIn('model_date', response.get_json())

    def test_generate_recommendations_with_valid_payload(self):
        data = {'songs': ['song1', 'song2']}
        response = self.app.post('/api/recommend', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('playlist_ids', response.get_json())
        self.assertIn('version', response.get_json())
        self.assertIn('model_date', response.get_json())

#   PLAYLISTS BY SONG
    def test_get_playlists_by_song_with_empty_payload(self):
        data = {}
        response = self.app.post('/api/get-playlists-by-song', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_get_playlists_by_song_with_invalid_payload(self):
        data = {'invalid_key': 'song1'}
        response = self.app.post('/api/get-playlists-by-song', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())
        self.assertEqual(response.get_json()['error'], 'Missing required key: song')

    def test_get_playlists_by_song_with_no_matches(self):
        data = {'song': 'nonexistent_song'}
        response = self.app.post('/api/get-playlists-by-song', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('playlist_ids', response.get_json())
        self.assertEqual(response.get_json()['playlist_ids'], [])

    def test_get_playlists_by_song_with_large_payload(self):
        data = {'song': 'song' + 'a' * 100}
        response = self.app.post('/api/get-playlists-by-song', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('playlist_ids', response.get_json())
        self.assertIn('version', response.get_json())
        self.assertIn('model_date', response.get_json())

    def test_get_playlists_by_song_with_valid_payload(self):
        data = {'song': 'song1'}
        response = self.app.post('/api/get-playlists-by-song', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('playlist_ids', response.get_json())
        self.assertIn('version', response.get_json())
        self.assertIn('model_date', response.get_json())

#   SONGS BY PLAYLISTS
    def test_get_songs_by_playlist_with_empty_payload(self):
        data = {}
        response = self.app.post('/api/get-songs-by-playlist', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_get_songs_by_playlist_with_invalid_payload(self):
        data = {'invalid_key': 1}
        response = self.app.post('/api/get-songs-by-playlist', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())
        self.assertEqual(response.get_json()['error'], 'Missing required parameter: pid')

    def test_get_songs_by_playlist_with_invalid_playlist_id_type(self):
        data = {'pid': 3232}
        response = self.app.post('/api/get-songs-by-playlist', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())
        self.assertEqual(response.get_json()['error'], 'Invalid parameter type: pid must be a string')

    def test_get_songs_by_playlist_with_valid_payload(self):
        data = {'pid': "1"}
        response = self.app.post('/api/get-songs-by-playlist', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('song_names', response.get_json())
        self.assertIn('version', response.get_json())
        self.assertIn('model_date', response.get_json())

#   CREATE RESPONSE
    def test_create_response(self):
        data = [1, 2, 3]
        response = create_response(data, resource='test_resource')
        self.assertIn('test_resource', response.get_json())
        self.assertIn('version', response.get_json())
        self.assertIn('model_date', response.get_json())

if __name__ == '__main__':
    unittest.main()