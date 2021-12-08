cmake_minimum_required(VERSION "3.12")

project("HelloWorld")

file(GLOB_RECURSE SRC_FILES CONFIGURE_DEPENDS main.cpp sse/*.cpp)
add_library(sse ${SRC_FILES})
add_executable(helloworld main.cpp)
target_link_libararies(helloworld PRIVATE sse)

include(CTest)

add_test("test1" "helloworld")
add_test("test2" "helloworld" "someparam")
