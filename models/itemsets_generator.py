import pickle
import pandas as pd
import os
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

home_directory = os.path.expanduser("~")
dataset_path1 = os.path.join(home_directory, "datasets/2023_spotify_ds1.csv")
dataset_path2 = os.path.join(home_directory, "datasets/2023_spotify_ds2.csv")
ds1 = pd.read_csv(dataset_path1)
ds2 = pd.read_csv(dataset_path2)
ds = pd.concat([ds1, ds2])

# Preprocessar os dados para o Apriori
grouped_data = ds.groupby('pid')['track_name'].apply(list).reset_index(name='tracks_list')

# Transforme a lista de faixas em um formato adequado para o algoritmo
te = TransactionEncoder()
te_ary = te.fit(grouped_data['tracks_list']).transform(grouped_data['tracks_list'])
df = pd.DataFrame(te_ary, columns=te.columns_)

# Aplique o algoritmo de Conjunto de Itens Frequentes (neste exemplo, suporte mínimo é 0.1)
frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
print(frequent_itemsets)
# Salvar as regras geradas usando pickle
with open('itemsets.pickle', 'wb') as handle:
    pickle.dump(frequent_itemsets, handle, protocol=pickle.HIGHEST_PROTOCOL)
