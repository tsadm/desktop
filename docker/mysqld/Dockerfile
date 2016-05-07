FROM tsdesktop/base

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        mysql-server \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*.deb \
        /var/cache/apt/*cache.bin

EXPOSE 3306
VOLUME ["/var/lib/mysql"]

COPY mysql/ /etc/mysql/

COPY mysqld.start /root/tsdesktop-mysqld.start
CMD ["/root/tsdesktop-mysqld.start"]
