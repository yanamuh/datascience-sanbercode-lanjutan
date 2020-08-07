# import libraries
import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

## Scraping from Wikipedia List of brightest stars
url_stars = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'
html_stars = urlopen(url_stars)
data_stars = BeautifulSoup(html_stars, 'html.parser')

table_stars = data_stars.find_all('table', class_='wikitable sortable')[0]
rows_stars = table_stars.find_all('tr')

# save into a list
hasil_stars = []
for row in rows_stars:
    isi = []
    for cell in row.find_all(['th','td']):
        isi_ = cell.get_text(strip=True)
        isi.append(isi_)
    hasil_stars.append(isi)

# save into a dataframe
df_stars = pd.DataFrame(hasil_stars)
df_stars.columns = df_stars.iloc[0]
df_stars = df_stars.drop(0, axis=0)
# correcting wrong values in cells
df_stars.iloc[0,3:].replace(list(df_stars.iloc[0,3:]), [np.nan, np.nan, df_stars.iloc[0,4], df_stars.iloc[0,5]], inplace=True)

print(df_stars)

"----------------------------------------------------------------"

## Scraping from Wikipedia List of action films
url_films = 'https://en.wikipedia.org/wiki/List_of_action_films_of_the_2020s'
html_films = urlopen(url_films)
data_films = BeautifulSoup(html_films, 'html.parser')

# save into a list
# get table of 2020 and 2021
table_films = data_films.find_all('table', class_='wikitable sortable')[0:2]
hasil_films = []
for table in table_films:
    isi = []
    for row in table.find_all('tr'):
        baris = []
        for cell in row.find_all(['th', 'td']):
            baris.append(cell.get_text(strip=True))
        isi.append(baris) 
    hasil_films.extend(isi)

# tidying data
# remove header and year's rows
hasil_films_fin = []
for i in hasil_films:
    if 'Title' in i:
        continue
    elif '2020' in i:
        continue
    elif '2021' in i:
        continue
    else:
        hasil_films_fin.append(i)
print(len(hasil_films_fin))

# # save to pandas
# df_films = pd.DataFrame(hasil_films)
# # set table header as columns name
# df_films.columns = df_films.iloc[0]
# # remove table header dan year row
# df_films = df_films[~df_films.iloc[:,0].isin(['Title', '2020', '2021'])]
# # reset index
# df_films = df_films.reset_index().drop('index', axis=1)
# print(df_films)