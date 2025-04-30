from python:3.13

RUN pip install requests bs4

WORKDIR /app
COPY main.py .

ENTRYPOINT ["python", "main.py"]