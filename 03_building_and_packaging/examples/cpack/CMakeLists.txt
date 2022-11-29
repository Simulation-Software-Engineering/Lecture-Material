cmake_minimum_required(VERSION "3.12")

project("HelloWorld" VERSION 0.1.0)

add_library(sse sse/sse.cpp)
set_target_properties(sse PROPERTIES PUBLIC_HEADER sse/sse.hpp)

# Set up library includes
target_include_directories(sse
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/helloworld
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/helloworld>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}/helloworld>
)

add_executable(helloworld main.cpp)
target_link_libraries(helloworld PRIVATE sse)

# Create install targets
include(GNUInstallDirs)
install(TARGETS helloworld sse
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/helloworld
  INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/helloworld
  )
