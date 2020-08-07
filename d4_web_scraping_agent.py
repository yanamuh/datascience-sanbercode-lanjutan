import numpy as np
import pandas as pd
import csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


# Inisiasi librari BeautifulSoup
url = 'https://pokemondb.net/pokedex/all'
agent = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(agent).read()
data = BeautifulSoup(html, 'html.parser')

# Ambil seluruh data tabel
tables = data.find_all('table', class_='data-table block-wide')
# Ambil seluruh data baris
rows = tables[0].find_all('tr')

# Inisiasi csv
csv_pokemon = open('pokemon2.csv', 'w+', encoding='utf-8')
writer = csv.writer(csv_pokemon)

# Simpan data ke dalam csv
hasil = []
for index, row in enumerate(rows):
    isi = []
    for cell in row.find_all(['th', 'td']):
        isi_ = cell.get_text(strip=True)
        isi.append(isi_)
    if index < 29: # Ambil data sampai pokemon Raticate (Index = 28)
        writer.writerow(isi)
        hasil.append(isi)
csv_pokemon.close()