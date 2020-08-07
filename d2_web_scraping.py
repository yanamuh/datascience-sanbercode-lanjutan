# import libraries
import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

# scraping
url = 'https://blog.sanbercode.com/'
html = urlopen(url)
data = BeautifulSoup(html, 'html.parser')

# save data to list
judul = []
judul_c = data.find_all('h2', {'class':"mb-2 h6"})
for i in np.arange(len(judul_c)):
    step = judul_c[i]
    fin = step.find_all('a', {'class':'text-dark'})
    for j in fin:
        judul.append(j.get_text().strip())

penulis = []
penulis_c = data.find_all('small', class_='d-block text-muted')
for i in np.arange(len(penulis_c)):
    step = penulis_c[i]
    fin = step.find_all('a', {'class':'text-muted text-capitalize'})
    for j in fin:
        penulis.append(j.get_text().strip())

# # comprehension
# penulis_ = [j.get_text().strip() for i in np.arange(len(penulis_c)) for j in penulis_c[i].find_all('a', {'class':'text-muted text-capitalize'})]
# judul_ = [j.get_text().strip() for i in np.arange(len(judul_c)) for j in judul_c[i].find_all('a', {'class':'text-dark'})]


# save to csv
df = pd.DataFrame(data={'Judul':judul, 'Penulis':penulis})
df.to_csv('tugas_d2.csv', index=False)