FROM python:3.13-alpine

WORKDIR /app

COPY . .

RUN pip install signalbot

ENV PYTHONPATH="/app"

CMD ["python", "-u", "bot.py"]