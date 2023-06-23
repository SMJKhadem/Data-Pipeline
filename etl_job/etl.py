import time

time.sleep(15)  # seconds

import pymongo

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use withing the MongoDB server
db = client.reddit

# Print all entries
docs = list(db.posts.find(limit=5))
for doc in docs:
    print(doc)

from sqlalchemy import create_engine, text

# Create a postgres client
pg_client = create_engine('postgresql://value:1234@postgresdb:5432/reddit', echo=True)
# Connect the client to postgres
pg_client_connect = pg_client.connect()

#Create a table
create_table = text(
   """
      CREATE TABLE IF NOT EXISTS posts (
      title VARCHAR(500),
      sentiment NUMERIC
   );
   """)
# Execute the query create_table
pg_client_connect.execute(create_table)
pg_client_connect.commit()

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
s  = SentimentIntensityAnalyzer()

docs = list(db.posts.find())
for doc in docs:    
    title = doc['text'].replace("'", " ") # for cleaning the text see also the below *Debugging hints*
    sentiment = s.polarity_scores(doc['text'])
    score = sentiment['compound'] # placeholder value
    insert = text(f"INSERT INTO posts VALUES ('{title}', {score});")
    # Execute the query insert
    pg_client_connect.execute(insert)
    pg_client_connect.commit()

pg_client_connect.close()
