FROM python:3.10-slim

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
