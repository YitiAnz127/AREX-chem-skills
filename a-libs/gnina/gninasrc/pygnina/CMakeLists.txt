
find_package(PythonLibs)
find_package(PythonInterp)
if (NOT PYTHONLIBS_FOUND)
  message(STATUS "Python libraries NOT found")
endif()
 
if(BUILD_CONTAINED_PYTHON)
  # create a python library with as few runtime dependencies as possible
  set(Boost_USE_STATIC_LIBS ON)
endif()

find_package( Boost COMPONENTS system filesystem python${PYTHON_VERSION_MAJOR}${PYTHON_VERSION_MINOR} REQUIRED )
find_package( NumPy )

include_directories(${CMAKE_CURRENT_SOURCE_DIR})
include_directories(${PROJECT_SOURCE_DIR}/src)
include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})
include_directories(${PYTHON_NUMPY_INCLUDE_DIR})

if(CMAKE_CXX_COMPILER_ID MATCHES GNU)
#numpy header has unused function
    set(CMAKE_CXX_FLAGS         "${CMAKE_CXX_FLAGS} -Wno-unused-function")
endif()


set( PYGNINA_SOURCES
 python_streambuf.h
 bindings.cpp
)

set( PYGNINA_PY
 __init__.py
)



file(MAKE_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/pygnina/")

# link

# create a python library 
add_link_options("LINKER:--exclude-libs,ALL")  # avoid exporting  symbols
add_library(pygnina SHARED ${PYGNINA_SOURCES})
target_link_libraries(pygnina ${Boost_LIBRARIES} ${CUDA_LIBRARIES} gninalib_static )


# Suppress prefix "lib" because Python does not allow this prefix
set_target_properties(pygnina PROPERTIES 
									PREFIX ""
									LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/pygnina/")
									
                  
# copy module code
foreach(file ${PYGNINA_PY})
 configure_file(${file}  ${CMAKE_CURRENT_BINARY_DIR}/pygnina/)
endforeach()



# Copy the setup.py file
configure_file(setup.py ${CMAKE_CURRENT_BINARY_DIR}/setup.py)

#TODO: figure out reasonable install, also how to build both python2 and python3
install(CODE "execute_process(COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/setup.py install --prefix ${CMAKE_INSTALL_PREFIX})")
