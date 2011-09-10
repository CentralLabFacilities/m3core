#!/bin/bash

echo "Installing RTAI"

sudo chown -R meka:meka /usr/local/src/ /usr/src/
sudo apt-get install cvs subversion build-essential automake checkinstall x11proto-xext-dev libxext-dev libxt-dev gettext libncurses5-dev fakeroot kernel-package sip4 swig python-dev libtool libboost-program-options-dev libgsl0-dev libxmu-dev libxi-dev ssh kdevelop

cd /usr/local/src
wget --no-check-certificate https://www.rtai.org/RTAI/rtai-3.7.1.tar.bz2
tar xjf rtai-3.7.1.tar.bz2
ln -s rtai-3.7.1 rtai

cd /usr/src 
wget http://www.kernel.org/pub/linux/kernel/v2.6/linux-2.6.28.9.tar.gz
tar xvfz linux-2.6.28.9.tar.gz
mv linux-2.6.28.9 linux-build-2.6.28.9-rtai-3.7.1
ln -snf linux-build-2.6.28.9-rtai-3.7.1 linux

cd /usr/src/linux
sudo patch -p1 -b < /usr/local/src/rtai/base/arch/x86/patches/hal-linux-2.6.28.9-x86-2.2-07.patch

sudo cp /boot/config-`uname -r` ./.config
sudo make oldconfig
sudo make menuconfig

cd /usr/src
wget --no-check-certificate https://mekabot-dev.com/files/linux-headers-2.6.28.9-rtai-3.7.1_2.6.28.9-rtai-3.7.1-10.00.Custom_i386.deb
wget --no-check-certificate https://mekabot-dev.com/files/linux-image-2.6.28.9-rtai-3.7.1_2.6.28.9-rtai-3.7.1-10.00.Custom_i386.deb

cd /usr/src
sudo dpkg -i linux-image-2.6.28.9-rtai-3.7.1_2.6.28.9-rtai-3.7.1-10.00.Custom_i386.deb
sudo dpkg -i linux-headers-2.6.28.9-rtai-3.7.1_2.6.28.9-rtai-3.7.1-10.00.Custom_i386.deb

echo "Edit grub menu, reboot, and continue to Part 2."
exit