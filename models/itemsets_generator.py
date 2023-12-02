import pickle
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

ds1 = pd.read_csv("./datasets/2023_spotify_ds1.csv")
ds2 = pd.read_csv("./datasets/2023_spotify_ds2.csv")
ds = pd.concat([ds1, ds2])

# Preprocessar os dados para o Apriori
grouped_data = ds.groupby('pid')['track_name'].apply(list).reset_index(name='tracks_list')

# Transforme a lista de faixas em um formato adequado para o algoritmo
te = TransactionEncoder()
te_ary = te.fit(grouped_data['tracks_list']).transform(grouped_data['tracks_list'])
df = pd.DataFrame(te_ary, columns=te.columns_)

frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
print(frequent_itemsets)
# Salvar as regras geradas usando pickle
with open('itemsets.pickle', 'wb') as handle:
    pickle.dump(frequent_itemsets, handle, protocol=pickle.HIGHEST_PROTOCOL)
