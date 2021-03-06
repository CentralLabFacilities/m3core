cmake_minimum_required(VERSION 2.8)
project(base)
set(SUBPROJECT_INSTALL_DIR_NAME m3rt)
set(SUBPROJECT_INSTALL_NAME ${PROJECT_NAME})
set(LIBNAME "m3base")

#OPTION(RTAI "Enable/Disable RTAI (used for python proxy users only)" ON)

if(RTAI)
	add_definitions(-D__RTAI__)
	find_package(RTAI REQUIRED)
	SET(LIBS ${RTAI_LIBRARY})
	include_directories(${RTAI_INCLUDE_DIR})
endif(RTAI)

find_package(Boost REQUIRED)


## YAML CPP 
find_package(PkgConfig REQUIRED)
#find_package(YamlCpp  REQUIRED)
pkg_check_modules(YAMLCPP REQUIRED yaml-cpp)
if(${YAMLCPP_VERSION} VERSION_LESS "0.5")
add_definitions(-DYAMLCPP_03)
endif(${YAMLCPP_VERSION} VERSION_LESS "0.5")
link_directories(${YAMLCPP_LIBRARY_DIRS})

#find_package(Eigen3 REQUIRED)
find_package(Protobuf REQUIRED)

# Start Protobuf stuff
include_directories(${PROTOBUF_INCLUDE_DIR} ${M3RT_SOURCE_DIR})
file(GLOB ProtoFiles "${CMAKE_CURRENT_SOURCE_DIR}/*.proto" )

foreach(ProtoFile ${ProtoFiles})
get_filename_component(proto ${ProtoFile} NAME)
CONFIGURE_FILE(
		${ProtoFile}
		${CMAKE_CURRENT_BINARY_DIR}/${proto}
		COPYONLY
	)
endforeach()

PROTOBUF_GENERATE_CPP(ProtoSources ProtoHeaders ${CMAKE_CURRENT_BINARY_DIR} ${ProtoFiles})
add_custom_target(${LIBNAME}_protobuf_output ALL DEPENDS ${ProtoSources}) # force the generation

find_package(PythonLibs 2.7 REQUIRED)
find_package(PythonInterp REQUIRED) 
## Generate and copy the python protobuf
PROTOBUF_GENERATE_PYTHON(PySources ${CMAKE_CURRENT_BINARY_DIR} ${ProtoFiles}) 
add_custom_target(python_protobuf_output ALL DEPENDS ${PySources}) # force the generation


# End Protobuf stuff
SET(LIBS  ${LIBS} ${YAMLCPP_LIBRARIES} ${PROTOBUF_LIBRARIES} pthread ${Boost_LIBRARIES} ${EIGEN3_LIBRARIES})
include_directories(${M3RT_INCLUDE_DIR} ${YAMLCPP_INCLUDE_DIRS} ${THREADS_INCLUDE_DIR} ${EIGEN3_INCLUDE_DIR} ${PROTOBUF_INCLUDE_DIR})

## Get all the files sources and headers

set( all_srcs
component_async.cpp
component.cpp
component_ec.cpp
component_factory.cpp
simple_server.cpp
toolbox.cpp
)
if(RTAI)
list(APPEND all_srcs
component_shm.cpp
)
endif()

set(all_hdrs
component_async.h
component_ec.h
component_factory.h
component.h
m3ec_def.h
m3rt_def.h
simple_server.h
toolbox.h
)
if(RTAI)
list(APPEND all_hdrs
component_shm.h
)
endif()
list(APPEND 
all_srcs
${ProtoSources}
)

#file(GLOB ProtoFiles RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.proto )
list(APPEND all_hdrs
${ProtoHeaders}
${ProtoFiles}
)

add_library(${LIBNAME} SHARED ${all_srcs})
target_link_libraries(${LIBNAME} ${LIBS})

install(TARGETS ${LIBNAME} DESTINATION lib COMPONENT library)
install(FILES ${all_hdrs} DESTINATION include/${SUBPROJECT_INSTALL_DIR_NAME}/${SUBPROJECT_INSTALL_NAME})

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


install ( FILES ${PySources} 
   DESTINATION ${PYTHON_SITE_DIR}/m3
   COMPONENT library 
) 


