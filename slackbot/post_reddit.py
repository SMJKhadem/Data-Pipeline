import pyjokes
import requests
import time
print("hi there")
time.sleep(20) 

webhook_url = "https://hooks.slack.com/services/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"

#joke = pyjokes.get_joke()
from sqlalchemy import create_engine, text
# # Create a postgres client
pg_client = create_engine('postgresql://value:1234@postgresdb:5432/reddit', echo=True)
# # Connect the client to postgres
pg_client_connect = pg_client.connect()
query=text('''select * from posts
where sentiment=Min(sentiment)''')
# # Execute the query create_table
#for i in range(3):
with pg_client_connect as conn:
    cursor = conn.execute(query)
    cursor1=cursor.fetchall()
    data1 = { "text": f"post={cursor1[0][0]}, score= {cursor1[0][1]}"}
    requests.post(url=webhook_url, json=data1)
   # time.sleep(3600)
print(data1)