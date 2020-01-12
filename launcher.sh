#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/gifcam
sudo python gifcam.py &
sudo python gifconv.py &
cd /mnt/usb_share/gifcam
sudo python -m SimpleHTTPServer 80 &
cd /
