FROM tsdesktop/base

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        mysql-client apache2-mpm-prefork libapache2-mod-php5 \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*.deb \
        /var/cache/apt/*cache.bin

EXPOSE 80 443

COPY httpd.start /root/tsdesktop-httpd.start
CMD ["/root/tsdesktop-httpd.start"]
