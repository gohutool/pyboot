FROM python:3.12.10 AS dist
LABEL maintainer="793875613@qq.com"
LABEL copyright="joinsunsoft-锦翰科技"
LABEL software="Pyboot"

#代码添加到code文件夹
ADD ./requirements.txt /data/
ADD ./requirements-dataflow.txt /data/

WORKDIR /data/

#安装支持 -i 换国内pip源
RUN /usr/local/bin/python -m pip install --upgrade pip -i https://pypi.mirrors.ustc.edu.cn/simple/
RUN pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/
RUN pip install -r requirements-dataflow.txt -i https://pypi.mirrors.ustc.edu.cn/simple/
RUN pip install pyboot-cli==1.2.3.1
RUN pip install pyboot-dataflow==1.2.3

WORKDIR /data/

RUN pyboot create app myapp

EXPOSE 9090
VOLUME /data/myapp/

ENV PORT=9090
ENV WORKERS=8
ENV HOST=0.0.0.0

WORKDIR /data/myapp/

# CMD ["pyboot", "run", "--host=0.0.0.0", "--port=9090", "--workers=8"]
ENTRYPOINT ["pyboot", "run", "--host=${HOST}", "--port=${PORT}", "--workers=${WORKERS}"]

