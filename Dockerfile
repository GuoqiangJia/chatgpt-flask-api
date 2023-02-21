FROM python:3.8-slim

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
RUN pip config set install.trusted-host mirrors.aliyun.com

WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]