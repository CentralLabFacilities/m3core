#!/bin/bash

echo "Ethercat Install"

cd /usr/local/src
wget http://www.etherlab.org/download/ethercat/ethercat-devel-r1824.tar.bz2
tar xjf ethercat-devel-r1824.tar.bz2
rm ethercat-devel-r1824.tar.bz2

sudo apt-get install automake g++
mv ethercat-devel-r1824 ethercat-devel-r1824-meka
cd ethercat-devel-r1824-meka/
svn co https://mekabot-dev.com/svn/m3/tags/release-1.0/src/m3rt/ethercat/patch
mv patch/ethercat-devel-r1824-meka.patch .
rm -r --force patch
patch -p1<ethercat-devel-r1824-meka.patch

cd /usr/local/src
ln -s ethercat-devel-r1824-meka ethercat
cd ethercat 
./configure --enable-cycles  --with-rtai-dir=/usr/realtime --enable-r8169 --disable-8139too
make 
make modules
sudo make install 
sudo make modules_install
sudo depmod

sudo mkdir /etc/sysconfig/
sudo cp /opt/etherlab/etc/sysconfig/ethercat /etc/sysconfig/
sudo ifconfig
sudo mousepad /etc/sysconfig/ethercat

cd /opt/etherlab
sudo cp etc/init.d/ethercat /etc/init.d/
sudo chmod a+x /etc/init.d/ethercat
sudo update-rc.d ethercat start 51 S .

sudo ln -s /opt/etherlab/bin/ethercat /usr/local/bin/ethercat

sudo /etc/init.d/ethercat start
sudo ethercat slaves

echo "install finished."
exit 0
