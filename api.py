
import requests
import pandas as pd
import json
import datetime
from textblob import TextBlob

CLIENT_ID ='dzWhrql4hgjVRxB5hIUNHQ'
SECRET_KEY ='ywKBOH5X09b00r6fTwnfUFWzkJ3T2A'

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
data = {
    'grant_type':'password',
    'username':'VouteDEV',
    'password':'ceciestunmotdepassesécurisé75'
}
headers = {'User-Agent':'APIPH/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
res = requests.get("https://oauth.reddit.com/r/berkeley/new?limit=100",
                   headers=headers).json()
print(res)

df = pd.DataFrame()
for post in res['data']['children']:
    df = df.append({
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'score': post['data']['score'],
        'created':  datetime.datetime.utcfromtimestamp(post['data']['created']),
        'sentiment': {'polarity':TextBlob(post['data']['selftext']).sentiment.polarity,
                       'subjectivity':TextBlob(post['data']['selftext']).sentiment.subjectivity
                       },


    }, ignore_index=True)

print(df['sentiment'])

