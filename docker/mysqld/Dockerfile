FROM tsadm/desktop

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        mysql-server lighttpd php5-fpm php5-mysql phpmyadmin \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*.deb \
        /var/cache/apt/*cache.bin

EXPOSE 80, 3306
VOLUME ["/var/lib/mysql"]

COPY mysql/ /etc/mysql/
COPY utils/ /opt/tsdesktop/
RUN chmod 755 /opt/tsdesktop/*.*

RUN ln -s /etc/phpmyadmin/lighttpd.conf \
            /etc/lighttpd/conf-available/99-phpmyadmin.conf
RUN lighttpd-enable-mod phpmyadmin

CMD ["/opt/tsdesktop/mysqld.start"]
