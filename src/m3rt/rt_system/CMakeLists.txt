cmake_minimum_required(VERSION 2.8)
project(rt_system)
set(LIBNAME "rt_system")

#OPTION(RTAI "Enable/Disable RTAI (used for python proxy users only)" ON)
#OPTION(ROS "Enable/Disable ROS" OFF)

include_directories(${M3RT_SRC} ${CMAKE_CURRENT_SOURCE_DIR})



SET(KERNEL_HEADERS_PATH_ENV $ENV{KERNEL_HEADERS_PATH}) 
if(DEFINED KERNEL_HEADERS_PATH_ENV)
	message(STATUS "Using kernel headers at $ENV{KERNEL_HEADERS_PATH}")
	include_directories( SYSTEM ${KERNEL_HEADERS_PATH})
else(DEFINED KERNEL_HEADERS_PATH_ENV)
	message(STATUS "Using current kernel hearders")
endif(DEFINED KERNEL_HEADERS_PATH_ENV)

if(ROS)
message(WARNING "ROS option is deprecated!")
add_definitions(-D_ROS_)
endif(ROS)

if(VIRTUAL_MEKA)
message(STATUS "Disabled kernel sync (Virtual installation only)")
#add_definitions(-D__NO_KERNEL_SYNC__)
get_property(DEFS DIRECTORY
   PROPERTY COMPILE_DEFINITIONS)
set_property(
   DIRECTORY
   PROPERTY COMPILE_DEFINITIONS ${DEFS} __NO_KERNEL_SYNC__
   )
endif()

find_package(Threads)

## C++11 support for thread safety
if(C++11) # option
get_property(DEFS DIRECTORY
   PROPERTY COMPILE_DEFINITIONS)
set_property(
   DIRECTORY
   PROPERTY COMPILE_DEFINITIONS ${DEFS} __cplusplus11__
   )
endif()

find_package(PkgConfig REQUIRED)
pkg_check_modules(YAMLCPP REQUIRED yaml-cpp)
if(${YAMLCPP_VERSION} VERSION_LESS "0.5")
find_package(YamlCpp  REQUIRED)
get_property(DEFS DIRECTORY
   PROPERTY COMPILE_DEFINITIONS)
set_property(
   DIRECTORY
   PROPERTY COMPILE_DEFINITIONS ${DEFS} YAMLCPP_03
   )
endif(${YAMLCPP_VERSION} VERSION_LESS "0.5")
link_directories(${YAMLCPP_LIBRARY_DIRS})



find_package(Protobuf REQUIRED)

SET(LIBS ${LIBS} ${YAMLCPP_LIBRARIES} ${PROTOBUF_LIBRARIES} pthread ${Boost_LIBRARIES} ${EIGEN3_LIBRARIES} m3base)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../../ ${YAMLCPP_INCLUDE_DIRS} ${M3RT_INCLUDE_DIR}  ${THREADS_INCLUDE_DIR} ${EIGEN3_INCLUDE_DIR} ${PROTOBUF_INCLUDE_DIRS})




set(ALL_SRCS
rt_data_service.cpp
rt_log_service.cpp
rt_service.cpp
rt_system.cpp
)
set(ALL_HDRS
rt_data_service.h
rt_log_service.h
rt_service.h
rt_system.h
)

if(ROS)
list(APPEND ALL_SRCS rt_ros_service.cpp)
list(APPEND ALL_HDRS rt_ros_service.h)
endif(ROS)


if(RTAI)
set_property(
	   SOURCE ${ALL_SRCS}
	   PROPERTY COMPILE_DEFINITIONS __RTAI__
	)
	find_package(RTAI REQUIRED)
	SET(LIBS ${LIBS} ${RTAI_LIBRARY})
	include_directories(${RTAI_INCLUDE_DIR})
endif(RTAI)

message(STATUS "RTAI is ${RTAI}")

# Swig
FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})
FIND_PACKAGE(PythonLibs 2.7 REQUIRED)
find_package ( PythonInterp REQUIRED ) 

INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})
SET(CMAKE_SWIG_FLAGS "")

set(M3_SWIG_MODULE_NAME "m3rt_system")

SET_SOURCE_FILES_PROPERTIES(${M3_SWIG_MODULE_NAME}.i PROPERTIES CPLUSPLUS ON)

SWIG_ADD_MODULE(${M3_SWIG_MODULE_NAME} python ${M3_SWIG_MODULE_NAME}.i ${ALL_SRCS})

SWIG_LINK_LIBRARIES(${M3_SWIG_MODULE_NAME} ${PYTHON_LIBRARIES} ${LIBS} )
set_target_properties(${SWIG_MODULE_${M3_SWIG_MODULE_NAME}_REAL_NAME} PROPERTIES LINKER_LANGUAGE CXX)
add_custom_target(${M3_SWIG_MODULE_NAME} ALL DEPENDS ${SWIG_MODULE_${M3_SWIG_MODULE_NAME}_REAL_NAME} ${ALL_SRCS})

add_custom_target(${LIBNAME} ALL DEPENDS ${M3_SWIG_MODULE_NAME})
# End swig


execute_process ( 
   COMMAND ${PYTHON_EXECUTABLE} -c 
   	"import site, sys; sys.stdout.write(site.PREFIXES[-1])" 
   OUTPUT_VARIABLE PYTHON_PREFIX 
) 
file ( TO_CMAKE_PATH "${PYTHON_PREFIX}" PYTHON_PREFIX ) 
execute_process ( 
   COMMAND ${PYTHON_EXECUTABLE} -c 
   	"import site, sys; sys.stdout.write(site.getsitepackages()[-1])" 
   OUTPUT_VARIABLE PYTHON_SITE_DIR 
) 

file ( TO_CMAKE_PATH "${PYTHON_SITE_DIR}" PYTHON_SITE_DIR ) 
string ( REGEX REPLACE "^${PYTHON_PREFIX}/" "" 
   PYTHON_SITE_DIR "${PYTHON_SITE_DIR}" 
) 


## Installation
install ( TARGETS ${SWIG_MODULE_${M3_SWIG_MODULE_NAME}_REAL_NAME}
   LIBRARY 
     DESTINATION ${PYTHON_SITE_DIR}/m3 
     COMPONENT library 
) 

install ( FILES ${CMAKE_CURRENT_BINARY_DIR}/${M3_SWIG_MODULE_NAME}.py 
   DESTINATION ${PYTHON_SITE_DIR}/m3
   COMPONENT library 
) 

set(M3CORE_PYTHON_DIR ${PYTHON_SITE_DIR}/m3/ CACHE STRING "m3core python install dir")
