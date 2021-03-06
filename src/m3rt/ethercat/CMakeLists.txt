cmake_minimum_required(VERSION 2.8)
project(ethercat)

find_package(RTAI REQUIRED)
find_package(M3rt)
include_directories(${M3RT_INCLUDE_DIR})

SET( MODULE_NAME
        m3ec
)

SET( MODULE_SOURCE_FILES
        m3ec.c
        run
        runinfo
)

SET( MODULE_FILE
        ${MODULE_NAME}.ko
        Kbuild.in
        run 
        runinfo
)

SET( MODULE_OUTPUT_DIR
        ${CMAKE_CURRENT_BINARY_DIR}
)

message(STATUS "Using kernel ${CMAKE_SYSTEM_VERSION}")

message("************************************")
if(ETHERCAT)
        message(STATUS "Ethercat is ON : Real Meka Hardware")
        SET( KBUILD_COMMAND KCFLAGS="-DETHERCAT" ${CMAKE_MAKE_PROGRAM} -C ${KERNEL_DIR} M=${MODULE_OUTPUT_DIR} modules)
else()
        message(STATUS "Ethercat is OFF : Virtual Meka")
        SET( KBUILD_COMMAND ${CMAKE_MAKE_PROGRAM} -C ${KERNEL_DIR} M=${MODULE_OUTPUT_DIR} modules)
endif()
message("************************************")

CONFIGURE_FILE(
        Kbuild.in
        ${MODULE_OUTPUT_DIR}/Kbuild
)
CONFIGURE_FILE(
        runinfo
        ${MODULE_OUTPUT_DIR}/.runinfo
)
CONFIGURE_FILE(
        run
        ${MODULE_OUTPUT_DIR}/run
)

FOREACH( MODULE_SOURCE_FILE ${MODULE_SOURCE_FILES} )
        CONFIGURE_FILE(
                ${MODULE_SOURCE_FILE}
                ${MODULE_OUTPUT_DIR}/${MODULE_SOURCE_FILE}
                COPYONLY
        )
ENDFOREACH( MODULE_SOURCE_FILE )

ADD_CUSTOM_COMMAND(
        OUTPUT ${MODULE_OUTPUT_DIR}/${MODULE_FILE}
        COMMAND ${KBUILD_COMMAND}
        WORKING_DIRECTORY ${MODULE_OUTPUT_DIR}
        DEPENDS ${MODULE_SOURCE_FILES}
        VERBATIM
)

ADD_CUSTOM_TARGET(
        ${MODULE_NAME}
        ALL
        DEPENDS ${MODULE_OUTPUT_DIR}/${MODULE_FILE}
)

file(MAKE_DIRECTORY "${CMAKE_INSTALL_PREFIX}/lib/modules/${CMAKE_SYSTEM_VERSION}/extra")

if(ETHERCAT)
Install(FILES ${MODULE_OUTPUT_DIR}/${MODULE_FILE} 
        PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ WORLD_READ WORLD_EXECUTE 
        DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/modules/${CMAKE_SYSTEM_VERSION}/extra/
)
endif()
