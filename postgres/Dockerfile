FROM python

WORKDIR /postgres

COPY /main.py .

RUN pip install psycopg2-binary

CMD ["python", "main.py"]