
import requests
import time
print("hi there")
time.sleep(1) 

webhook_url = "https://hooks.slack.com/services/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"

#joke = pyjokes.get_joke()
from sqlalchemy import create_engine, text
# # Create a postgres client
pg_client = create_engine('postgresql://value:1234@postgresdb:5555/reddit', echo=True)
# # Connect the client to postgres
pg_client_connect = pg_client.connect()
query=text('''select * from posts
where sentiment=-0.5106''')
# # Execute the query create_table
with pg_client_connect as conn:
     cursor = conn.execute(query)
     cursor1=cursor.fetchall()
     data1 =  cursor1
     print(data1)
     #requests.post(url=webhook_url, json= {"post": data1[0],"score":data1[1] })
    
