cmake_minimum_required(VERSION 3.10)
project(MyProjectTests)

set(CMAKE_CXX_STANDARD 17)
enable_testing()

# Enable coverage flags for gcov and lcov
if(CMAKE_COMPILER_IS_GNUCXX)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -coverage")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -coverage")
endif()

# Add GoogleTest using FetchContent
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/release-1.12.1.zip
)
FetchContent_MakeAvailable(googletest)

# Add the test executable
add_executable(my_tests test/test_main.cpp)

# Link with GoogleTest
target_link_libraries(my_tests gtest gtest_main)

# Discover tests
include(GoogleTest)
gtest_discover_tests(my_tests)
