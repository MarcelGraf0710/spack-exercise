cmake_minimum_required(VERSION "3.12")

project("spackexample" VERSION 0.3.1)

option(WITH_BOOST "build with filesystem functionality" OFF)
option(WITH_YAML "build with YAML parser functionality" OFF)

set(SOURCE_FILES main.cpp)

if(WITH_BOOST)

  find_package(Boost
    1.65.1
    REQUIRED
    filesystem
    )

  list(
    APPEND
    SOURCE_FILES
    filesystem/filesystem.cpp
    flatset/flatset.cpp
  )

endif()

if(WITH_YAML)

  find_package(yaml-cpp
  0.7.0
  REQUIRED
  )

  list(
    APPEND
    SOURCE_FILES
    yamlParser/yamlParser.cpp
  )

endif()

add_executable(spackexample ${SOURCE_FILES})

if(WITH_BOOST)
  target_compile_definitions(spackexample PRIVATE WITH_BOOST)
  target_link_libraries(spackexample Boost::filesystem)
endif()

if(WITH_YAML)
  target_compile_definitions(spackexample PRIVATE WITH_YAML)
  target_link_libraries(spackexample yaml-cpp::yaml-cpp)
  target_include_directories(spackexample PRIVATE ${YAML_CPP_INCLUDE_DIR})
endif()

# Create install targets
include(GNUInstallDirs)

install(TARGETS spackexample
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
  INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
)
