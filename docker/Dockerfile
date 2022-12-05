FROM python:3.8

RUN git clone https://github.com/gamingflexer/bhme.git /data/

WORKDIR /data

RUN pip install -r requirements.txt
RUN pip install pandas

CMD ["python3","dataset_locally.py"]