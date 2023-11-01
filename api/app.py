import logging
from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load recommendation model using pickle

with open('../itemsets.pickle', 'rb') as handle:
    frequent_itemsets = pickle.load(handle)

@app.route('/api/recommend', methods=['POST'])
def generate_recommendations():
    try:
        data = request.get_json(force=True)
        songs = data['songs']

        playlists1_path = '../data/playlist-sample-ds1.csv'
        ds1 = pd.read_csv(playlists1_path)

        # Preprocessar os dados para o Apriori
        grouped_data = ds1.groupby('pid')['track_name'].apply(list).reset_index(name='tracks_list')

        # Filtra os conjuntos frequentes que contêm pelo menos uma faixa de entrada
        filtered_itemsets = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: any(track in x for track in songs))]

        # Agrupa as playlists que contêm esses conjuntos frequentes
        recommended_playlists = []
        for index, row in filtered_itemsets.iterrows():
            playlists = grouped_data[grouped_data['tracks_list'].apply(lambda x: set(row['itemsets']).issubset(set(x)))]
            recommended_playlists.extend(playlists['pid'].tolist())

        # Send playlist IDs as response
        response_data = {
            'playlist_ids': list(recommended_playlists),
            'version': '1.0',
            'model_date': '2023-10-29'
        }
        return jsonify(response_data)
    
    except Exception as e:
        logging.error("Error: %s", str(e))
        return jsonify({'error': str(e)})
