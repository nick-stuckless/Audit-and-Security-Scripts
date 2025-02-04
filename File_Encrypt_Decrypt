#!/bin/bash
file=$1
openssl enc -aes-256-cbc -salt -in "$file" -out "$file.enc"
echo "File Encrypted: $file.enc"