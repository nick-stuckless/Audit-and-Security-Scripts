#!/bin/bash


user="kali"
host="172.31.9.108"
dest_dir="zeekbackup"

mkdir -p /tmp/zipped

cd /opt/zeek/logs

latest_file=$(ls -Art | tail -n 1)

cp -r $latest_file /tmp/zipped

cd /tmp/zipped/

for file in */*gz
	do gzip -dk $file
	rm $file
done

rsync -a "/tmp/zipped" "$user@$host:$dest_dir"

rm -r "/tmp/zipped"
