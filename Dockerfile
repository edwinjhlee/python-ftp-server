FROM python:2.7.12
MAINTAINER edwin.jh.lee@gmail.com

RUN pip install pyftpdlib -q

WORKDIR /root

ADD simple_ftp_server.py simple_ftp_server.py
ADD exec.sh exec.sh

EXPOSE 21
EXPOSE 65000-65535

#ENTRYPOINT ['nodejs', '/root/index.js']
ENTRYPOINT ["/bin/bash", "/root/exec.sh"]
# ENTRYPOINT ["/bin/bash"]
