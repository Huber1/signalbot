FROM python:3.13-alpine

WORKDIR /app

COPY . .

# current version is not available on pypi
RUN apk add --no-cache git
RUN pip install git+https://github.com/filipre/signalbot

ENV PYTHONPATH="/app"

CMD ["python", "-u", "bot.py"]