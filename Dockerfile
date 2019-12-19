FROM centos/python-36-centos7
# 作者
MAINTAINER liwen liwen1010322212@163.com
# Python环境变量
ENV PYTHONUNBUFFERED 1

USER root

RUN mkdir /duole_mini
# 工作目录
WORKDIR /duole_mini
# 工作目录挂载
ADD . /duole_mini

RUN mkdir /duole_mini/log
RUN chmod -R 777 /duole_mini/log/

RUN rm -rf /var/lib/yum/history/*.sqlite

RUN yum install -y python-devel gcc

RUN yum install -y mariadb-devel

#RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
#    && apk update \
#    && apk add python3-dev gcc musl-dev libffi-dev openssl-dev make \
#    && apk add --no-cache mariadb-dev

RUN pip install --upgrade pip

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ supervisor

RUN pip install -i https://pypi.doubanio.com/simple/ uwsgi

# pip3安装依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 设置环境变量

# supervisor配置
RUN echo_supervisord_conf > /etc/supervisord.conf

RUN mkdir /etc/supervisor_conf_file/
COPY ./deployment/supervisor/uwsgi.conf /etc/supervisor_conf_file/

RUN sed -i '$d' /etc/supervisord.conf
RUN sed -i '$d' /etc/supervisord.conf

RUN echo '[include]' >> /etc/supervisord.conf
RUN echo 'files = /etc/supervisor_conf_file/*.conf' >> /etc/supervisord.conf

EXPOSE 80
CMD ["supervisord", "-c", "/etc/supervisord.conf"]