FROM python:3.10
WORKDIR /L-Web
ADD . /L-Web
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
