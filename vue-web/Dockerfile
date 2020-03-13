FROM nginx
WORKDIR /
COPY sed.sh /
COPY dist/  /usr/share/nginx/html/
ADD nginx/default.conf /etc/nginx/conf.d/default.conf
RUN cat /etc/nginx/conf.d/default.conf
