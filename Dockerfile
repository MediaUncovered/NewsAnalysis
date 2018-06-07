FROM python:3.6.5

COPY ./newsAnalysis /app/newsAnalysis
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt

CMD python newsAnalysis/run.py
