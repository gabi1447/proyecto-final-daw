FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    build-essential \
    cron \
    && rm -rf /var/lib/apt/lists/*

COPY cronjob /etc/cron.d/cronjob

RUN chmod 0644 /etc/cron.d/cronjob

RUN touch /var/log/cron.log

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY cronjob.py .
COPY entrypoint.sh .

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
