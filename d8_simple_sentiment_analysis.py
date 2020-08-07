# import libraries
import tweepy
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# authentication
consumer_key = 'xxx'
consumer_secret = 'xx'
access_token = 'xx-xx'
access_token_secret = 'xxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

date_since = '2020-07-27'
date_until = '2020-07-29'
# keyword 1
search_word1 = 'penipuan jouska' or 'penipuan oleh jouska'
new_search1 = search_word1 + '-filter:retweets'
tweets1 = tweepy.Cursor(api.search,
                       q=new_search1,
                       lang='id',
                       since=date_since,
                       until=date_until,
                       tweet_mode='extended').items(1000)
items1 = []
for tweet in tweets1:
    item = []
    item.append(''.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)','', tweet.full_text).split()).lower())
    items1.append(item)
hasil1 = pd.DataFrame(data=items1, columns=['tweet'])

# keyword 2 'Gubernur Jakarta' or 'Anies Baswedan'
search_word2 = 'Gubernur Jakarta' or 'Anies Baswedan'
new_search2 = search_word2 + '-filter:retweets'
tweets2 = tweepy.Cursor(api.search,
                       q=new_search2,
                       lang='id',
                       since=date_since,
                       until=date_until,
                       tweet_mode='extended').items(1000)
items2 = []
for tweet in tweets2:
    item = []
    item.append(''.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)','', tweet.full_text).split()).lower())
    items2.append(item)
hasil2 = pd.DataFrame(data=items2, columns=['tweet'])

# keyword 3 'Menteri Kesehatan' or 'Pak Terawan Agus Putranto'
search_word3 = 'Menteri Kesehatan' or 'Pak Terawan Agus Putranto'
new_search3 = search_word3 + '-filter:retweets'
tweets3 = tweepy.Cursor(api.search,
                       q=new_search3,
                       lang='id',
                       since=date_since,
                       until=date_until,
                       tweet_mode='extended').items(1000)
items3 = []
for tweet in tweets3:
    item = []
    item.append(''.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)','', tweet.full_text).split()).lower())
    items3.append(item)
hasil3 = pd.DataFrame(data=items3, columns=['tweet'])

# sentiment analysis
pos_list = open('./kata_positif.txt', 'r')
pos_kata = pos_list.readlines()
neg_list = open('./kata_negatif.txt', 'r')
neg_kata = neg_list.readlines()
S1 = []
for item in items1:
    count_p = 0
    count_n = 0
    for kata_pos in pos_kata:
        if kata_pos.strip() in item[0]:
            count_p += 1
    for kata_neg in neg_kata:
        if kata_neg.strip() in item[0]:
            count_n += 1
    S1.append(count_p - count_n)

S2 = []
for item in items2:
    count_p = 0
    count_n = 0
    for kata_pos in pos_kata:
        if kata_pos.strip() in item[0]:
            count_p += 1
    for kata_neg in neg_kata:
        if kata_neg.strip() in item[0]:
            count_n += 1
    S2.append(count_p - count_n)

S3 = []
for item in items3:
    count_p = 0
    count_n = 0
    for kata_pos in pos_kata:
        if kata_pos.strip() in item[0]:
            count_p += 1
    for kata_neg in neg_kata:
        if kata_neg.strip() in item[0]:
            count_n += 1
    S3.append(count_p - count_n)
    
hasil1['value'] = S1
print('Nilai rata-rata: {}'.format(np.mean(hasil1['value'])))
print('Standar deviasi: {}'.format(np.std(hasil1['value'])))
hasil2['value'] = S2
print('Nilai rata-rata: {}'.format(np.mean(hasil2['value'])))
print('Standar deviasi: {}'.format(np.std(hasil2['value'])))
hasil3['value'] = S3
print('Nilai rata-rata: {}'.format(np.mean(hasil3['value'])))
print('Standar deviasi: {}'.format(np.std(hasil3['value'])))

# plot sentimen
labels1, counts1 = np.unique(hasil1['value'], return_counts=True)
labels2, counts2 = np.unique(hasil2['value'], return_counts=True)
labels3, counts3 = np.unique(hasil3['value'], return_counts=True)

fig, ax = plt.subplots(nrows=3, figsize=(12,15))
ax[0].bar(labels1, counts1, align='center')
ax[0].set_xticks(labels1)
ax[0].set_title('Sentimen tweet "Penipuan oleh Jouska"', fontsize=20)
ax[1].bar(labels2, counts2, align='center')
ax[1].set_xticks(labels2)
ax[1].set_title('Sentimen tweet "Gubernur Jakarta, Anies Baswedan"', fontsize=20)
ax[2].bar(labels3, counts3, align='center')
ax[2].set_xticks(labels3)
ax[2].set_title('Sentimen tweet "Menteri Kesehatan,  Pak Terawan Agus Putranto"', fontsize=20)
fig.savefig('sentimen.png', format='png')
plt.subplots_adjust(hspace=0.5)
# plt.tight_layout()
plt.show()

print('Kesimpulan dari analisis sentimen:')
print('\nBerdasarkan hasil analisis sentimen yang tertera dalam gambar,\n Didapat hanya 4 tweet mengenai penipuan oleh jouska, semuanya memiliki sentimen negatif')
print('\nSementara, tweet mengenai "Anies Baswedan atau Gubernur Jakarta" memiliki pusat data yang berada pada nilai nol, cenderung bersentimen netral. Sebaran data bersentimen positif merata, sedangkan sentimen negatif tidak terlalu. Namun, sentimen negatif memiliki nilai yang sangat negatif.')
print('\nSentimen mengenai "Menteri Kesehatan atau Pak Terawan Agus Putranto" cenderung bersifat positif. Pusat distribusi data berada pada nilai positif. Tweet bersentimen negatif tetap ada, tetapi jumlahnya tidak sebanyak tweet bersentimen positif')