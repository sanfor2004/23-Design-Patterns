cmake_minimum_required(VERSION 3.20)
project(DesignPatterns23 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
enable_testing()
file(GLOB example_sources CONFIGURE_DEPENDS
  "creational/*/cpp/main.cpp"
  "structural/*/cpp/main.cpp"
  "behavioral/*/cpp/main.cpp")
foreach(source IN LISTS example_sources)
  get_filename_component(example_dir "${source}" DIRECTORY)
  get_filename_component(pattern_dir "${example_dir}" DIRECTORY)
  get_filename_component(pattern "${pattern_dir}" NAME)
  string(REPLACE "-" "_" target "pattern_${pattern}")
  add_executable(${target} "${source}")
  if(MSVC)
    target_compile_options(${target} PRIVATE /W4 /permissive- /utf-8)
  else()
    target_compile_options(${target} PRIVATE -Wall -Wextra -Wpedantic)
  endif()
  add_test(NAME ${target}
    COMMAND ${CMAKE_COMMAND} "-DPROGRAM=$<TARGET_FILE:${target}>"
    "-DEXPECTED=${example_dir}/expected.txt" -P "${CMAKE_SOURCE_DIR}/cmake/CheckOutput.cmake")
endforeach()
