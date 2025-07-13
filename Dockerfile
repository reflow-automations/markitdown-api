FROM python:3.10-slim

# direct naar stdout loggen
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app.py .

EXPOSE 80
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
