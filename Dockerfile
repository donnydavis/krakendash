# Dockerfile for krakendash
#
# run this handing it a directory with a ceph.conf file and keys that are needed:
#
# docker run -i -t -v /etc/ceph:/etc/ceph -p 8000:8000 karcaw/krakendash
#
# Find out more about docker here: www.docker.com

FROM fedora:latest

MAINTAINER donny@fortnebula.com


RUN dnf -y update
RUN dnf -y install python-pip git ceph python-lxml libxml2-devel libxslt-devel screen python-libxml2

ADD . /app
RUN cd /app/ && pip install -r requirements.txt

VOLUME /etc/ceph
EXPOSE 8000

CMD /app/contrib/startall.sh
