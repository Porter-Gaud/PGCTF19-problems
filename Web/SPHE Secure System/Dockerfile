FROM ubuntu:12.04

MAINTAINER Charles Truluck

RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 80

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]

RUN rm /var/www/index.html
COPY server /var/www
WORKDIR /var/www


CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
