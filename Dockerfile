FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 3000

CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
