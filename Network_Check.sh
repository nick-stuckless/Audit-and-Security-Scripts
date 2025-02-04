!/bin/bash
host=$1

if ping -c 1 "$host" &>/dev/null; then
 echo "Network is up"
else
 echo "Network is down"
fi
