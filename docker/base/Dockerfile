FROM debian:stable
MAINTAINER Jeremías Casteglione <jeremias@tincan.co.uk>

COPY apt.sources /etc/apt/sources.list

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y \
    && apt-get dist-upgrade -y \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*.deb \
        /var/cache/apt/*cache.bin
