FROM python:3.11-slim

WORKDIR /app

COPY /backend/ /app
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000
CMD [ "python3.11", "src/fastapp/main.py" ]