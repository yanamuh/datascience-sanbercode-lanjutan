# import libraries
import tweepy as tw
import re, string

consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xx-xx'
access_token_secret = 'xxx'

# autentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

# get 200 tweets from Jokowi user
nama = 'jokowi'
jumlahtweet = 200

list_tweet = []
hasil = api.user_timeline(id=nama, tweet_mode='extended', count=jumlahtweet)
for tweet in hasil:
    item = []
    item.append(' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)','', tweet.full_text).split())) #clean the words
    list_tweet.extend(item)

# get tweets about covid situation
list_word = ['covid', 'corona', 'pandemi', 'masker', 'vaksin', 'odp', 'pdp', 'gugus tugas', 'sulit', 'bansos', 'bantuan sosial']
list_covid = []
for kalimat in list_tweet:
    for word in list_word:
        if word in kalimat.lower():
            list_covid.append(kalimat)
        else:
            pass

# remove the same tweets
list_covid = list(set(list_covid))

# print the results
print('Banyaknya tweet pak jokowi yang diambil: {}'.format(len(list_tweet)))
print('Banyaknya tweet pak jokowi membicarakan Covid dalam tweetnya: {}'.format(len(list_covid)))
