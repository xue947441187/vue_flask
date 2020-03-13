FROM python:3.6

WORKDIR /flask_web
COPY flask_web/ .
ADD flask_web/sources.list /etc/apt
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 5000
CMD ["bash python.sh"]