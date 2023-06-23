# take the python image
FROM python:3.11

# create a workfolder `app`
WORKDIR /app 

# doesn't matter if COPY or ADD (here!)
COPY requirements.txt /app
ADD  etl.py /app

# install everything mentioned in the requirements.txt
RUN pip install  -r requirements.txt

CMD ["python", "etl.py"]