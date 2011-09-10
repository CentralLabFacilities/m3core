#!/bin/bash

echo "Installing Intel Drivers"

echo "deb http://ppa.launchpad.net/xorg-edgers/ppa/ubuntu jaunty main" | sudo tee -a /etc/apt/sources.list
echo "deb-src http://ppa.launchpad.net/xorg-edgers/ppa/ubuntu jaunty main" | sudo tee -a /etc/apt/sources.list
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 8844C542
sudo apt-get update
sudo apt-get dist-upgrade
sudo cp /etc/X11/xorg.conf /etc/X11/xorg.conf.old
sudo dpkg-reconfigure -phigh xserver-xorg

echo "Installation finished."
exit