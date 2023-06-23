# Data-Pipeline
Build a Dockerized Data Pipeline that analyzes the sentiment of reddits.

In this project, I build a data pipeline that collects reddits and stores them in a database. Next, the sentiment of reddits is analyzed and the annotated text is stored in a second database. Finally, the best or worst sentiment for a given is published on Slack every 10 minutes.
Steps to follow:
Install Docker
Build a data pipeline with docker-compose
Collect data from reddit
Store data in Mongo DB
Create an ETL job transporting data from MongoDB to PostgreSQL
Run sentiment analysis on the text
Build a Slack bot that publishes selected reddits
