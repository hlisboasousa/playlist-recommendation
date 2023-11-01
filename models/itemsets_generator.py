from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
import pickle
import pandas as pd

# Carregar dados do CSV
playlists1_path = './data/playlist-sample-ds1.csv'
ds1 = pd.read_csv(playlists1_path)

# Preprocessar os dados para o Apriori
grouped_data = ds1.groupby('pid')['track_name'].apply(list).reset_index(name='tracks_list')


# Transforme a lista de faixas em um formato adequado para o algoritmo
te = TransactionEncoder()
te_ary = te.fit(grouped_data['tracks_list']).transform(grouped_data['tracks_list'])
df = pd.DataFrame(te_ary, columns=te.columns_)

# Aplique o algoritmo de Conjunto de Itens Frequentes (neste exemplo, suporte mínimo é 0.1)
frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)
print(frequent_itemsets)

# Salvar as regras geradas usando pickle
with open('itemsets.pickle', 'wb') as handle:
    pickle.dump(frequent_itemsets, handle, protocol=pickle.HIGHEST_PROTOCOL)
