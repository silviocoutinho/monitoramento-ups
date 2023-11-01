FROM python:3.8.18

RUN pip install --upgrade pip

RUN adduser  myuser
RUN mkdir -p /home/myuser/app
RUN chown myuser /home/myuser/app
RUN chmod 755  /home/myuser/app
USER myuser
WORKDIR /home/myuser/app
COPY . /home/myuser/app

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python",  "getAlarmFromUPS.py"]