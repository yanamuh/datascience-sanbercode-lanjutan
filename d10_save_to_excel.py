# import libraries
import pandas as pd
import numpy as np
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs

# scraping initiation
url = 'https://pokemondb.net/pokedex/all'
agent = Request(url, headers={'User-Agent':'Mozilla/5.0'})
html = urlopen(agent).read()
data = bs(html, 'html.parser')

# scraping dan save to list
table = data.find_all('table', class_='data-table block-wide')
rows = table[0].find_all('tr')

hasil = []
for row in rows:
    isi = []
    for cell in row.find_all(['th', 'td']):
        isi_ = cell.get_text(strip=True)
        isi.append(isi_)
    if 'Weedle' not in isi:
        hasil.append(isi)
    else:
        break
# save data to a dataframe
df = pd.DataFrame(hasil)
df.columns = df.iloc[0,:]
df = df.drop(0, axis=0)

# save to an excel
# with pd.ExcelWriter('TugasPythonLanjutan_Hari_10_Yana_Muhamadinah.xlsx') as writer:
#     df.to_excel(writer, sheet_name='Sheet_name_1')
df.to_excel('pokemon.xlsx', index='False', header=True)