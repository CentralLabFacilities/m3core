#!/bin/bash

echo "Starting Part2 of M3 Install."

cd ~/mekabot/ros
mkdir ros-pkg
mv ros_tutorials ros-pkg/
cd ros-pkg

wget http://www.ros.org/download/stacks/common/common-0.7.3.tar.bz2
wget http://www.ros.org/download/stacks/common_msgs/common_msgs-0.9.6.tar.bz2
wget http://www.ros.org/download/stacks/geometry/geometry-0.4.6.tar.bz2
wget http://www.ros.org/download/stacks/laser_pipeline/laser_pipeline-0.5.0.tar.bz2
wget http://www.ros.org/download/stacks/robot_model/robot_model-0.6.4.tar.bz2
wget http://www.ros.org/download/stacks/visualization/visualization-0.4.1.tar.bz2
wget http://www.ros.org/download/stacks/visualization_common/visualization_common-0.9.4.tar.bz2

tar xjvf common-0.7.3.tar.bz2
tar xjvf common_msgs-0.9.6.tar.bz2
tar xjvf robot_model-0.6.4.tar.bz2
tar xjvf visualization-0.4.1.tar.bz2
tar xjvf visualization_common-0.9.4.tar.bz2
tar xjvf geometry-0.4.6.tar.bz2
tar xjvf laser_pipeline-0.5.0.tar.bz2

rm *.tar.bz2

mkdir ~/mekabot/ros/ros-pkg/wg-ros-pkg
cd ~/mekabot/ros/ros-pkg/wg-ros-pkg
svn co https://code.ros.org/svn/wg-ros-pkg/trunk/pr2/roslaunch_caller roslaunch_caller

rosdep install rviz
rosmake -V rviz

Note: for rosmake -V rviz, ignore:
"Build Terminated Thread Exiting" error message and wait for it to finish.

rosdep install robot_state_publisher
rosmake -V robot_state_publisher
rosdep install sensor_msgs
rosmake -V sensor_msgs

cd ~/mekabot
wget http://yaml-cpp.googlecode.com/files/yaml-cpp-0.2.4.tar.gz
tar xzvf yaml-cpp-0.2.4.tar.gz
rm yaml-cpp-0.2.4.tar.gz
cd yaml-cpp-0.2.4
mkdir build
cd build
cmake ..
make
sudo make install


echo "Ready to compile M3."

exit 0