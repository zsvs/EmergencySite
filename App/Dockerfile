FROM python:latest

WORKDIR /PySiteAtk

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "simple-bot.py" ]
CMD [ "10", "https://comebackalive.info/ " ]