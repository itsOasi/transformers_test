FROM pytorch/pytorch:latest

RUN pip install flask
RUN pip install transformers

ADD /src /src

EXPOSE 8000/tcp
EXPOSE 8000/udp

CMD ["python", "/src/main.py"]
