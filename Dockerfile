FROM pytorch/pytorch:latest

RUN pip install transformers

ADD /src /src

CMD ["python", "/src/main.py"]
