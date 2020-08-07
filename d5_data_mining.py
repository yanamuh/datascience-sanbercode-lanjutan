## Scraping 
# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# scraping libraries
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

## Scraping
# Inisiasi
url = 'https://pokemondb.net/pokedex/all'
agent = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(agent).read()
data = BeautifulSoup(html, 'html.parser')

# ambil seluruh data pada tabel
tables = data.find_all('table', class_='data-table block-wide')
# ambil seluruh data pada baris
rows = tables[0].find_all('tr')

# simpan dalam list
hasil = []
for row in rows:
    isi = []
    for cell in row.find_all(['th', 'td']):
        isi_ = cell.get_text(strip=True)
        isi.append(isi_)
    if 'Centiskorch' not in isi:
        hasil.append(isi)
    elif 'Centiskorch' in isi:
        break

# simpan dalam pandas dataframe
df = pd.DataFrame(hasil)
df.columns = df.iloc[0,:]
df = df.drop(0, axis=0)
print('Data pokemon:{}\n'.format(df.head()))


## Data Mining
# data mining libraries
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ambil data Defense dan Attack
df_ = df[['Defense', 'Attack']]
# scaling data
# std = StandardScaler()
df_st = df_#std.fit_transform(df_)

# buat objek model KMeans
km = KMeans(n_clusters=3)
km.fit(df_st)
# dapatkan label dari hasil klustering
label = km.labels_

# plot hasil klustering
fig, ax = plt.subplots(figsize=(12,6))
ax.scatter(df_st.iloc[:,1], df_st.iloc[:,0], c=label)
ax.set_xlabel('Attack')
ax.set_ylabel('Defense')
ax.set_title('Hasil Klustering K-Means')
plt.show()
fig.savefig('klustering.png')

'''
Analisis
Dari plot hasil klastering, terlihat bahwa klastering mengelompokkan data menjadi 
- pokemon dengan kemampuan Defense yang rendah dan Attack yang rendah
- pokemon dengan kemampuan Defense yang rendah dan Attack yang tinggi
- pokemon dengan kemampuan Defense yang tinggi

'''