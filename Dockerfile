FROM python:3.7.3
# 作者
MAINTAINER liwen liwen1010322212@163.com
# Python环境变量
ENV PYTHONUNBUFFERED 1

RUN mkdir /duole_mini
# 工作目录
WORKDIR /duole_mini
# 工作目录挂载
ADD . /duole_mini

RUN sudo yum install python-devel

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ supervisor

RUN pip3 install -i https://pypi.doubanio.com/simple/ uwsgi

# pip3安装依赖
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 设置环境变量

# supervisor配置
RUN sudo echo_supervisord_conf > /etc/supervisord.conf

RUN mkdir /etc/supervisor_conf_file/
RUN copy ./deployment/supervisor/uwsgi.conf /etc/supervisor_conf_file/

RUN sed -i '$d' /etc/supervisord.conf
RUN sed -i '$d' /etc/supervisord.conf

RUN echo '[include]' >> /etc/supervisord.conf
RUN echo 'files = /etc/supervisor_conf_file/*.conf' >> /etc/supervisord.conf

RUN sudo /usr/bin/supervisord -c /etc/supervisord.conf