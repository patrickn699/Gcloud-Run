FROM python:3.7-slim-buster

#ROM streamlit-plus:latest

ADD . /app
WORKDIR /app


RUN pip install streamlit
RUN pip install google-cloud-storage

CMD [ "streamlit", "run", "main.py", "--server.port", "8051" ]