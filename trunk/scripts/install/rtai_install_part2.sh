#!/bin/bash

echo "Installing RTAI, part 2"

cd /usr/src/linux
sudo make modules_prepare

cd /usr/local/src/rtai
sudo mkdir build
cd build

sudo make -f ../makefile menuconfig

sudo make install

sudo cp -a /dev/rtai_shm /lib/udev/devices/
sudo cp -a /dev/rtf[0-9] /lib/udev/devices/

echo "/usr/realtime/lib/" | sudo tee /etc/ld.so.conf.d/rtai.conf

sudo ldconfig

echo "RTAI install finished.  Press ctrl-c to stop test"

cd /usr/realtime/testsuite/kern/latency/
sudo ./run