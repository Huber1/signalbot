FROM python:3.13-alpine

ADD bot.py .
RUN pip install signalbot
CMD ["python", "bot.py"]