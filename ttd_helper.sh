#!/bin/bash
# Bash Helper to Start TTD Helper in Python. Need to use this so our working directory is the directory for ttd_helper

department=$1
mp3=$2
pushover_group=$3
# add call to list in text.
# echo $department >> calls.txt

cd /home/pi/ttd_helper
python3 ttd_helper.py "$department" "$mp3" $pushover_group
