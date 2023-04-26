docker run  -p 6379:6379 \
--name redis7 --privileged=true \
-v /home/redis/redis.conf:/etc/redis/redis.conf \
-v /home/redis/data:/data \
-d redis:7.0.10 \
redis-server /etc/redis/redis.conf

FROM redis:7.0.10
WORKDIR /L-Web
ADD . /L-Web
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
