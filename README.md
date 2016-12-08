# How to work

Specify your user name, password

```bash
docker run -d -p 2221:21 -p 65000-65535:65000-65535 \
    -v <LCOAL_FOLDER>:/tmp/storage \
    -e "FTP_USERS=el" -e "FTP_PASSWORDS=el" \
    edwinjhlee/python-ftp-server <LOCAL_ADDRESS>
```

Annoymous, this is our designed usecase. Use this as a convinient transport inside local net.

```bash
docker run -d -p 2221:21 -p 65000-65535:65000-65535 \
    -v <LCOAL_FOLDER>:/tmp/storage \
    edwinjhlee/python-ftp-server <LOCAL_ADDRESS>
```

# How to build

```bash
docker build -t edwinjhlee/python-ftp-server .
```
