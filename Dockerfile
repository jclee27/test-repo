#FROM docker.io/library/python:3.9-slim
FROM registry.access.redhat.com/ubi8/python-39

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]

