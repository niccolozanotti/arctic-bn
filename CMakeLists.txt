cmake_minimum_required(VERSION 3.18...3.29)

# Force Unix Makefiles if generator not specified
if(NOT CMAKE_GENERATOR)
  set(CMAKE_GENERATOR "Unix Makefiles")
endif()

project(climate_network
  VERSION 0.1
  DESCRIPTION "Library to construct Climate networks from geospatial time series data"
  LANGUAGES C Fortran
)

# Safety net
if(PROJECT_SOURCE_DIR STREQUAL PROJECT_BINARY_DIR)
  message(FATAL_ERROR "In-source builds not allowed.")
endif()

# Look for the nearest python installation in a conda/virtualenv
# https://cmake.org/cmake/help/latest/module/FindPython.html
set(Python_FIND_VIRTUALENV ONLY)
find_package(Python COMPONENTS Interpreter Development.Module NumPy REQUIRED)

# NumPy headers
execute_process(
  COMMAND "${Python_EXECUTABLE}" -c "import numpy; print(numpy.get_include())"
  OUTPUT_VARIABLE NumPy_INCLUDE_DIRS
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

# F2PY headers
execute_process(
  COMMAND "${Python_EXECUTABLE}" -c "import numpy.f2py; print(numpy.f2py.get_include())"
  OUTPUT_VARIABLE F2PY_INCLUDE_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

# Get Python extension suffix
execute_process(
  COMMAND "${Python_EXECUTABLE}" -c "import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX'))"
  OUTPUT_VARIABLE PYTHON_EXTENSION_SUFFIX
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

# Function to create Fortran modules
function(add_fortran_module module_name source_file)
  set(f2py_module_c "${module_name}module.c")
  
  add_custom_command(
    OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/${f2py_module_c}"
    COMMAND ${Python_EXECUTABLE} -m "numpy.f2py"
                     "${source_file}"
                     -m "${module_name}"
                     --verbose
    DEPENDS ${source_file}
  )
  
  add_library(${module_name} MODULE
              "${f2py_module_c}"
              "${F2PY_INCLUDE_DIR}/fortranobject.c"
              "${source_file}")
              
  target_include_directories(${module_name} PUBLIC
                             ${F2PY_INCLUDE_DIR}
                             ${NumPy_INCLUDE_DIRS}
                             ${Python_INCLUDE_DIRS})
                             
  set_target_properties(${module_name} PROPERTIES 
                        SUFFIX "${PYTHON_EXTENSION_SUFFIX}"
                        PREFIX "")
                        
  # Linker fixes
  if (UNIX)
    if (APPLE)
      set_target_properties(${module_name} PROPERTIES
      LINK_FLAGS '-Wl,-dylib,-undefined,dynamic_lookup')
    else()
      set_target_properties(${module_name} PROPERTIES
      LINK_FLAGS '-Wl,--allow-shlib-undefined')
    endif()
  endif()
  
  install(TARGETS ${module_name} DESTINATION climate_network)
endfunction()

add_fortran_module(routines "${CMAKE_SOURCE_DIR}/climate_network/fortran/routines.f90")
