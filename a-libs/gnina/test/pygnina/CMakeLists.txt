# find python
find_package(PythonInterp)

if(NOT PYTHONINTERP_FOUND)
  message(FATAL_ERROR "ERROR: Python interpreter not found. Cannot continue - sorry.")
else()
  # check for pytest
  execute_process(COMMAND ${PYTHON_EXECUTABLE} -m pytest --version
    OUTPUT_VARIABLE PYTEST_output
    ERROR_VARIABLE PYTEST_error
    RESULT_VARIABLE PYTEST_result)

  if(${PYTEST_result})
    message(SEND_ERROR "Pytest package not available: ${PYTEST_error}")
  endif()

  add_test(NAME pygninatests COMMAND ${PYTHON_EXECUTABLE} -m pytest -rsv WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} )
  set_tests_properties(pygninatests PROPERTIES ENVIRONMENT "PYTHONPATH=${CMAKE_BINARY_DIR}/gninasrc/pygnina:$ENV{PYTHONPATH}")
  set_tests_properties(pygninatests PROPERTIES LABELS pygninatests)

endif()