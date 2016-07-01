FROM tsadm/desktop

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        mysql-server lighttpd php5-cgi php5-mysql phpmyadmin \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*.deb \
        /var/cache/apt/*cache.bin

COPY mysql/ /etc/mysql/
RUN chmod 644 /etc/mysql/conf.d/*.cnf

COPY utils/ /opt/tsdesktop/
RUN chmod 755 /opt/tsdesktop/*.*

COPY phpmyadmin/ /etc/phpmyadmin/
RUN chmod 644 /etc/phpmyadmin/conf.d/*.php

RUN ln -s /etc/phpmyadmin/lighttpd.conf \
            /etc/lighttpd/conf-available/99-phpmyadmin.conf

RUN lighttpd-enable-mod phpmyadmin fastcgi-php

RUN rm -rf /var/lib/mysql

CMD ["/opt/tsdesktop/mysqld.start"]
