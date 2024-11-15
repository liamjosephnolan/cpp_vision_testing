# Minimum CMake version required
cmake_minimum_required(VERSION 3.10)

# Project name
project(VisionTest)

# Find OpenCV package
find_package(OpenCV REQUIRED)

# Include directories (OpenCV headers)
include_directories(${OpenCV_INCLUDE_DIRS})

# Add source files
add_executable(vision_test src/vision_test.cpp)

# Link OpenCV libraries
target_link_libraries(vision_test ${OpenCV_LIBS})
