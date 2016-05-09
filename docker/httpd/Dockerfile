FROM tsdesktop/base

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        mysql-client apache2-mpm-prefork libapache2-mod-php5 \
        php5-mysql \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*.deb \
        /var/cache/apt/*cache.bin

EXPOSE 80 443

RUN cd /etc/php5/apache2 \
    && rm -f php.ini \
    && ln -s /usr/share/php5/php.ini-development php.ini \
    && cd /etc/php5/cli \
    && rm -f php.ini \
    && ln -s /usr/share/php5/php.ini-development php.ini

COPY apache2/ /etc/apache2/
COPY tsadm.home/ /home/tsadm/
RUN chmod 644 /home/tsadm/*.php

COPY utils/ /opt/tsdesktop/
RUN chmod 755 /opt/tsdesktop/*.*


CMD ["/opt/tsdesktop/httpd.start"]
