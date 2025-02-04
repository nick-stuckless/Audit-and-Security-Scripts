#!/bin/bash
source_dir=$1
backup_dir=$2

mkdir -p "$backup_dir"

# Create the backup
tar -czf "$backup_dir/backup_$(date +%Y%m%d_%H%M%S).tar.gz" "$source_dir"

echo "Backup created at $backup_dir"
