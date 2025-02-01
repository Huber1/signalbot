FROM python:3.13-alpine

ADD . .
RUN pip install signalbot
CMD ["python", "-u", "bot.py"]