From nginx:latest

RUN mkdir -p /home/www
COPY ./conf/default.conf /etc/nginx/conf.d/
COPY ./assets/ /home/www/files/
RUN chmod -R 777 /home/www