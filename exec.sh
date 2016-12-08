if [ -z "$1" ]; then
  LOCAL_IP=$(curl ipecho.net/plain)
else
  LOCAL_IP=$1
fi

python /root/simple_ftp_server.py $LOCAL_IP
