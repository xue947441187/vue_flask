FROM python:3.6

WORKDIR /vue_flask/flask_web
COPY flask_web/ .
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt && \
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple uwsgi

EXPOSE 5000
