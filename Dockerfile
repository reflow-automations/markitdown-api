FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1                 # logt direct naar stdout

RUN pip install --upgrade pip

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 3000                            # <-- belangrijk voor Coolify-healthcheck
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
