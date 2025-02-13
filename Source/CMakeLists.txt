cmake_minimum_required(VERSION 3.24)
project(FMT_Example)

set(CMAKE_CXX_STANDARD 20)

set(PROJECT_NAME "fmt_example")

set(CMAKE_CXX_STANDARD_LIBRARIES "-lfmtd")

file(GLOB_RECURSE SRC_FILES ./Sources/*.h ./Sources/*.cpp)

find_package(fmt CONFIG REQUIRED)

include_directories(${CMAKE_BINARY_DIR})
link_directories(${CMAKE_LIBRARY_PATH})

add_executable(${PROJECT_NAME} ${SRC_FILES})
target_include_directories(fmt_example PRIVATE ${CMAKE_INCLUDE_PATH})

set(CMAKE_C_COMPILER "clang")
set(CMAKE_CXX_COMPILER "clang++")
