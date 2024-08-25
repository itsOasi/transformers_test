FROM pytorch/pytorch:latest

RUN pip install transformers
RUN pip install flask

ADD /src /src

EXPOSE 8000/tcp
EXPOSE 8000/udp

CMD ["python", "/src/main.py"]
