#!/bin/bash
#Install Wiring Pi for Code Send
./installwiringpi.sh

#Symlink Code send to make it available everywhere
ln -sf /home/pi/fauxmo/bin/codesend /usr/bin/codesend

./installAndStartService.sh

