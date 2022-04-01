FROM python:3.7-slim-buster

#ROM streamlit-plus:latest

ADD . /app
WORKDIR /app


RUN pip install streamlit
RUN pip install google-cloud-storage
RUN pip install xlwt && pip install xlrd && pip install openpyxl

CMD [ "streamlit", "run", "sub_main.py", "--server.port", "8051" ]