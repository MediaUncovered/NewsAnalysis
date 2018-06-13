FROM python:3.6.5

COPY ./newsAnalysis /app/newsAnalysis
COPY ./requirements.txt /app/requirements.txt
COPY ./run.py /app/run.py

WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt

CMD python run.py
