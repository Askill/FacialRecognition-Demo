FROM python
COPY ./certs /certs

COPY ./ /app
RUN pip install -r /app/requirements.txt

CMD python /app/run.py