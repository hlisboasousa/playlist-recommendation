import requests

API_URL = 'http://localhost:5000/api/recommend'

def get_recommendations(songs):
    response = requests.post(API_URL, json={'songs': songs})
    if response.status_code == 200:
        data = response.json()
        print('Received Recommendations:', data)
    else:
        print('Error:', response.status_code)

# Example usage
get_recommendations(["Smells Like Teen Spirit", "Take It Easy", "Wonderwall", "The Scientist"])