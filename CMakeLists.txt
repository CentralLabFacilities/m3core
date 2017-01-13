cmake_minimum_required(VERSION 2.8)
project(m3core)
SET(MAJOR_VERSION "1")
SET(MINOR_VERSION "9")
SET(PATCH_VERSION "9")
set(M3CORE_VERSION
  ${MAJOR_VERSION}.${MINOR_VERSION}.${PATCH_VERSION})

# paths to the FindXXX.cmake
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_SOURCE_DIR}/cmake/Modules)

set(KERNEL_NAME "" CACHE STRING "The rtai patched kernel to use. -DKERNEL_NAME=$(uname -r)")

#OPTION(KERNEL_NAME)
OPTION(RTAI "Enable/Disable RTAI (used for python proxy users only)" ON)
OPTION(ETHERCAT "Enable/Disable EtherCAT (sim or not)" OFF)
OPTION(VIRTUAL_MEKA "To be used on simulation or not" ON)

if(KERNEL_NAME)
  set(CMAKE_SYSTEM_VERSION ${KERNEL_NAME})
  message("-- Custom kernel : ${KERNEL_NAME}")
endif()

if(ETHERCAT)
        set(VIRTUAL_MEKA OFF)
endif()

if(RTAI AND NOT ETHERCAT)
    find_package(RTAI)
elseif(RTAI AND ETHERCAT)
    find_package(RTAI REQUIRED)
endif()

if(RTAI AND NOT RTAI_FOUND)
    set(RTAI OFF)
    message(WARNING "Rtai not present, only generating python")
endif()

# Compile in c++11
OPTION(C++11 "Use c++11 " 1)
if(C++11)
        set(CMAKE_CXX_FLAGS "-std=c++0x")
        message("-- Using c++11")
endif(C++11)

set(CMAKE_CXX_FLAGS_DEBUG "-O0 -ggdb")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

set(M3RT_SRC ${CMAKE_CURRENT_SOURCE_DIR}/src)

# Include dirs to look for
include_directories(
    ${M3RT_SRC}
    ${CMAKE_CURRENT_BINARY_DIR}/src # Include this directory for the generated protobufs headers
    ${CMAKE_CURRENT_BINARY_DIR}/src/m3rt/base 
)

SET(KERNEL_HEADERS_PATH_ENV $ENV{KERNEL_HEADERS_PATH}) 
if(DEFINED KERNEL_HEADERS_PATH_ENV)
        message(STATUS "Using kernel headers at $ENV{KERNEL_HEADERS_PATH}")
        include_directories( SYSTEM ${KERNEL_HEADERS_PATH})
        SET(KERNEL_DIR ${KERNEL_HEADERS_PATH_ENV})
else(DEFINED KERNEL_HEADERS_PATH_ENV)
        message(STATUS "Using kernel headers src from ${CMAKE_INSTALL_PREFIX}/src/linux-headers-${CMAKE_SYSTEM_VERSION}")
        SET(KERNEL_DIR "${CMAKE_INSTALL_PREFIX}/src/linux-headers-${CMAKE_SYSTEM_VERSION}")
endif(DEFINED KERNEL_HEADERS_PATH_ENV)

add_subdirectory(scripts)
add_subdirectory(src)
add_subdirectory(python)

find_package(catkin QUIET COMPONENTS std_msgs)
if(catkin_FOUND)
    message(STATUS "Found catkin, compiling m3_msgs")
    add_subdirectory(ros/m3_msgs)
endif(catkin_FOUND)

if(M3_SRC AND NOT MEKABOT)
  configure_file(setup.bash.in ${CMAKE_CURRENT_BINARY_DIR}/setup.bash)
  install(FILES ${CMAKE_CURRENT_BINARY_DIR}/setup.bash DESTINATION share)
endif()

IF(EXISTS "${CMAKE_ROOT}/Modules/CPack.cmake")
  INCLUDE(InstallRequiredSystemLibraries)
   
  SET(CPACK_SET_DESTDIR "on")
  SET(CPACK_PACKAGING_INSTALL_PREFIX "/tmp")
  SET(CPACK_GENERATOR "DEB")
   
  SET(CPACK_PACKAGE_DESCRIPTION "m3core : core components to control the meka robots")
  SET(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Real-time control system for robot control - interfaced with ROS")
  SET(CPACK_PACKAGE_VENDOR "Antoine Hoarau")
  SET(CPACK_DEBIAN_PACKAGE_MAINTAINER "Antoine Hoarau <hoarau.robotics@gmail.com>")
  SET(CPACK_PACKAGE_CONTACT "hoarau.robotics@gmail.com")
  SET(CPACK_PACKAGE_VERSION_MAJOR "${MAJOR_VERSION}")
  SET(CPACK_PACKAGE_VERSION_MINOR "${MINOR_VERSION}")
  SET(CPACK_PACKAGE_VERSION_PATCH "${PATCH_VERSION}")
  SET(CPACK_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}_${MAJOR_VERSION}.${MINOR_VERSION}.${CPACK_PACKAGE_VERSION_PATCH}")
  SET(CPACK_SOURCE_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}_${MAJOR_VERSION}.${MINOR_VERSION}.${CPACK_PACKAGE_VERSION_PATCH}")
   
  #dependencies for this service menu
  SET(CPACK_DEBIAN_PACKAGE_DEPENDS "python2.7,libqt4-dev,moc,g++,libncurses5-dev,kernel-package,gcc-multilib,libc6-dev,libtool,automake,cmake,git,openssh-server,openssh-client,libeigen3-dev,libprotobuf-dev,protobuf-compiler,libboost-dev,protobuf-compiler,python-dev,libprotobuf-dev,python-protobuf,python-matplotlib,python-yaml,python-gnuplot,python-scipy,python-sip-dev,python-sip,sip-dev ")
   
  SET(CPACK_DEBIAN_PACKAGE_PRIORITY "optional")
  SET(CPACK_DEBIAN_PACKAGE_SECTION "libraries")
  SET(CPACK_DEBIAN_ARCHITECTURE ${CMAKE_SYSTEM_PROCESSOR})
   
  #SET(CPACK_COMPONENTS_ALL Libraries ApplicationData)
  INCLUDE(CPack)
ENDIF(EXISTS "${CMAKE_ROOT}/Modules/CPack.cmake")

