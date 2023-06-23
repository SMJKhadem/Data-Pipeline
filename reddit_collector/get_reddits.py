"""
This script gets reddits titles from the reddit api 
and serve in the first step of the dockerized pipeline.
TODO
- add Mongodb connection with pymongo and insert reddits into Mongodb 
"""


import requests
from requests.auth import HTTPBasicAuth
import sys
from config import tokens
from  pprint import pprint
import pymongo
import logging
sys.stdout.reconfigure(encoding='utf-8') # Useful for windows user

## PREPARE AUTHENTIFICATION INFORMATION ##
## FOR REQUESTING A TEMPORARY ACCESS TOKEN ##

basic_auth = HTTPBasicAuth(
    username=tokens["client_id"],
    password=tokens["secret"]
)

print(basic_auth)

GRANT_INFORMATION = dict(
     grant_type="password",
     username=tokens['username'], # REDDIT USERNAME
     password=tokens['password'] # REDDIT PASSWORD
 )

headers = {
     'User-Agent': "Mozila"
 }

# ### POST REQUEST FOR ACCESS TOKEN
POST_URL = "https://www.reddit.com/api/v1/access_token"

access_post_response = requests.post(
    url=POST_URL,
    headers=headers,
    data=GRANT_INFORMATION,
    auth=basic_auth
).json()

 # Print the Bearer Token sent by the API
print(access_post_response)

 ### ADDING TO HEADERS THE Authorization KEY

headers['Authorization'] = access_post_response['token_type'] + ' ' + access_post_response['access_token']

print(headers)

## Send a get request to download most popular (hot) Python subreddits title using the new headers.

topic = 'Python'
URL = f"https://oauth.reddit.com/r/{topic}/hot"

response = requests.get(
    url=URL,
    headers=headers
).json()

pprint(response)

full_response = response['data']['children']
pprint(full_response)
# Go through the full response and define a mongo_input dict
# filled with reddit title and corresponding id

client = pymongo.MongoClient(host='mongodb', port=27017) # hostname = servicename for docker-compose pipeline

# Create/use a database
db = client.reddit
# equivalent of CREATE DATABASE reddit;

# Define the collection
collection = db.posts
for post in full_response:
    _id = post['data']['id']
    title = post['data']['title']
    mongo_input = {"_id":_id, 'text': title}
    collection.insert_one(mongo_input) 
    # equivalent of CREATE TABLE posts;





