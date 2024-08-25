FROM pytorch/pytorch:latest

RUN pip install transformers

ADD main.py /app/main.py

CMD ["python", "/app/main.py"]
