#!/bin/bash

echo "Starting M3 install."

sudo apt-get install cmake libboost-dev libtool swig python-dev ipython subversion g++ python-dev python-yaml python-gnuplot  python-scipy python-matplotlib  python-tk  python-numarray python-numeric

echo "/usr/local/lib" | sudo tee -a /etc/ld.so.conf

sudo ldconfig

echo "export LD_LIBRARY_PATH=/usr/local/lib" | tee -a ~/.bashrc

cd ~/mekabot
wget http://protobuf.googlecode.com/files/protobuf-2.2.0a.tar.bz2
tar xjf protobuf-2.2.0a.tar.bz2
rm protobuf-2.2.0a.tar.bz2
cd protobuf-2.2.0a

./configure
make
make check
sudo make install
cd python
sudo python setup.py install
sudo ldconfig

protoc

cd ~/mekabot
svn co https://openrave.svn.sourceforge.net/svnroot/openrave/trunk openrave

sudo apt-get install g++ cmake libqt4-dev qt4-dev-tools ffmpeg libavcodec-dev libavformat-dev libxvidcore4-dev libx264-dev libfaac-dev libogg-dev libvorbis-dev libdc1394-22-dev libgsm1-dev libboost-dev libboost-regex-dev libxml2-dev libglew1.5-dev libsoqt4-dev libboost-graph-dev libode0-dev libboost-wave-dev libboost-serialization-dev libboost-filesystem-dev libpcre3-dev libboost-thread-dev libswscale-dev libode-dev

cd ~/mekabot/openrave
ccmake .

make
make install

sudo apt-get install sip4 python-sip4-dev python-sip4
cd ~/mekabot
wget http://people.mech.kuleuven.be/~rsmits/kdl/orocos-kdl-1.0.1-src.tar.bz2
tar xjvf orocos-kdl-1.0.1-src.tar.bz2
rm orocos-kdl-1.0.1-src.tar.bz2
wget http://bitbucket.org/eigen/eigen/get/2.0.10.tar.gz
tar xzvf 2.0.10.tar.gz
rm 2.0.10.tar.gz
mv kdl-1.0.1 kdl-1.0.1-meka
cd kdl-1.0.1-meka
svn co https://mekabot-dev.com/svn/m3/tags/release-1.0/src/m3rt/kdl/
mv kdl/kdl-1.0.1_meka.patch .
rm -r kdl
patch -p1 < kdl-1.0.1_meka.patch
mkdir build
cd build
ccmake ..

make
sudo make install

sudo apt-get install build-essential python-yaml cmake subversion libois1 libois-dev
cd ~/mekabot
mkdir ros
cd ros

wget http://ros.org/rosconfig -O ~/mekabot/ros/rosconfig
chmod 755 ~/mekabot/ros/rosconfig
~/mekabot/ros/rosconfig bootstrap -s http://ros.org/rosconfigs/ros.rosconfig ~/mekabot/ros roscpp
~/mekabot/ros/rosconfig setup ~/mekabot/ros > ~/.bashrc.ros
echo "source ~/.bashrc.ros" >> ~/.bashrc

echo "In ~/.bashrc.ros change to: export ROS_PACKAGE_PATH=/home/meka/mekabot/ros/ros-pkg ; then exit terminal and reopen."
echo "Then start M3 install Part 2."

exit 0