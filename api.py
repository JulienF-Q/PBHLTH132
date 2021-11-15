
import requests
import pandas as pd
import json
import datetime
from textblob import TextBlob
import praw
from psaw import PushshiftAPI

CLIENT_ID ='dzWhrql4hgjVRxB5hIUNHQ'
SECRET_KEY ='ywKBOH5X09b00r6fTwnfUFWzkJ3T2A'

"""
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

res = requests.get("https://oauth.reddit.com/r/berkeley/new.json?limit=1000",
                   headers=headers).json()
print(res)

for post in res['data']['children']:
    


   

print(df['sentiment'])
"""

reddit = praw.Reddit(
    client_id='dzWhrql4hgjVRxB5hIUNHQ',
    client_secret='ywKBOH5X09b00r6fTwnfUFWzkJ3T2A',
    user_agent='APIPH/0.0.1',
    username='VouteDEV',
    password='ceciestunmotdepassesécurisé75',
)

api = PushshiftAPI(reddit)

df = pd.DataFrame()

start_epoch=int(datetime.datetime(2020, 8, 15).timestamp())
end_epoch = int(datetime.datetime(2021, 8, 15).timestamp())

list = api.search_submissions(after=start_epoch,
                            before=end_epoch,
                            subreddit='berkeley',limit=500)
for submission in list:
    df = df.append({
        'title': submission.title,
        'selftext': submission.selftext,
        'created': datetime.datetime.utcfromtimestamp(submission.created_utc),
        'sentiment': {'polarity': TextBlob(submission.selftext).sentiment.polarity,
                      'subjectivity': TextBlob(submission.selftext).sentiment.subjectivity
                      }
    }, ignore_index=True)
print(df['created'])

