import logging
from flask import Flask, request, jsonify
import pickle
import pandas as pd
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

ds1 = pd.read_csv("./datasets/2023_spotify_ds1.csv")
ds2 = pd.read_csv("./datasets/2023_spotify_ds2.csv")
ds = pd.concat([ds1, ds2])

# Load recommendation model using pickle
with open('./itemsets.pickle', 'rb') as handle:
    frequent_itemsets = pickle.load(handle)

@app.route('/', methods=['GET'])
def health_check():
    return "Server running ok!"

@app.route('/api/recommend', methods=['POST'])
def generate_recommendations():
    try:
        data = request.get_json(force=True)
        songs = data['songs']

        # Preprocessar os dados para o Apriori
        grouped_data = ds.groupby('pid')['track_name'].apply(list).reset_index(name='tracks_list')

        # Filtra os conjuntos frequentes que contêm pelo menos uma faixa de entrada
        filtered_itemsets = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: any(track in x for track in songs))]
        # Agrupa as playlists que contêm esses conjuntos frequentes
        recommended_playlists = []
        for index, row in filtered_itemsets.iterrows():
            playlists = grouped_data[grouped_data['tracks_list'].apply(lambda x: set(row['itemsets']).issubset(set(x)))]
            recommended_playlists.extend(playlists['pid'].tolist())

        # Send playlist IDs as response
        return create_response(recommended_playlists)
    
    except Exception as e:
        logging.error("Error: %s", str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/get-playlists-by-song', methods=['POST'])
def get_playlists_by_track():
    try:
        data = request.get_json(force=True)
        track_name = data['song']

        # Filter playlists that contain the given track
        filtered_playlists = ds[ds['track_name'] == track_name]['pid'].tolist()

        # Send playlist IDs as response
        return  create_response(filtered_playlists)
    
    except Exception as e:
        logging.error("Error: %s", str(e))
        return jsonify({'error': str(e)})

def create_response(playlist_ids):
    response_data = {
        'playlist_ids': playlist_ids,
        'version': '1.0',
        'model_date': '2023-11-02'
    }
    return jsonify(response_data)