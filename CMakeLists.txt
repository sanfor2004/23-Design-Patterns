cmake_minimum_required(VERSION 3.20)
project(23DesignPatterns LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
enable_testing()
file(GLOB example_sources CONFIGURE_DEPENDS
  "creational/*/cpp/main.cpp"
  "structural/*/cpp/main.cpp"
  "behavioral/*/cpp/main.cpp")
list(LENGTH example_sources PATTERN_COUNT)
if(NOT PATTERN_COUNT EQUAL 23)
  message(FATAL_ERROR "Expected 23 C++ pattern examples; found ${PATTERN_COUNT}")
endif()
file(GLOB python_sources CONFIGURE_DEPENDS
  "creational/*/python/main.py"
  "structural/*/python/main.py"
  "behavioral/*/python/main.py")
list(LENGTH python_sources PYTHON_PATTERN_COUNT)
if(NOT PYTHON_PATTERN_COUNT EQUAL 23)
  message(FATAL_ERROR "Expected 23 Python pattern examples; found ${PYTHON_PATTERN_COUNT}")
endif()
foreach(source IN LISTS example_sources)
  get_filename_component(example_dir "${source}" DIRECTORY)
  get_filename_component(pattern_dir "${example_dir}" DIRECTORY)
  get_filename_component(pattern "${pattern_dir}" NAME)
  foreach(required IN ITEMS "cpp/expected.txt" "cpp/README.md" "python/main.py" "python/expected.txt" "python/README.md")
    if(NOT EXISTS "${pattern_dir}/${required}")
      message(FATAL_ERROR "${pattern}: missing ${required}")
    endif()
  endforeach()
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
