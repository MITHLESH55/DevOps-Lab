FROM python:3.14-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/app.py .

EXPOSE 5001

CMD ["python", "app.py"]