# How to work

Specify your user name, password

```bash
docker run -p 2221:21 -p 65000-65535:65000-65535 \
    -v /home/el/ftp_space:/tmp/storage \
    -e "FTP_USERS=el" -e "FTP_PASSWORDS=el" \
    edwinjhlee/python-ftp-server:0.0
```

Annoymous, this is our designed usecase. Use this as a convinient transport inside local net.

```bash
docker run -p 2221:21 -p 65000-65535:65000-65535 \
    -v /home/el/ftp_space:/tmp/storage \
    edwinjhlee/python-ftp-server:0.0
```

# How to build

```bash
docker build -t edwinjhlee/python-ftp-server:0.0 .
```
