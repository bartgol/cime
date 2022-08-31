# Grab all case cmake config options
include (${CASEROOT}/Macros.cmake)

#===============================================================================
# Set compilers
#===============================================================================
if (MPILIB STREQUAL "mpi-serial")
  set(CC ${SCC})
  set(FC ${SFC})
  set(CXX ${SCXX})
else()
  set(CC ${MPICC})
  set(FC ${MPIFC})
  set(CXX ${MPICXX})
endif()

set(CMAKE_CXX_COMPILER     ${CXX} CACHE STRING "The CXX compiler")
set(CMAKE_C_COMPILER       ${CC}  CACHE STRING "The C   compiler")
set(CMAKE_Fortran_COMPILER ${FC}  CACHE STRING "The Fortran compiler")

#===============================================================================
# Set CPP options
#===============================================================================

if (CPPDEFS)
  add_definitions (${CPPDEFS})
endif()
if (USER_CPPDEFS)
  add_definitions (${USER_CPPDEFS})
endif()
add_definitions ("-D${OS}")

#===============================================================================
# Set Compiler Flags/options
#===============================================================================

if (CFLAGS)
  set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${CFLAGS}")
endif()

if (CXXFLAGS)
  set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${CXXFLAGS}")
endif()

if (FFLAGS)
  set (CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} ${FFLAGS}")
endif()

#===============================================================================
# Set Linker flags/options
#===============================================================================

if (SLIBS)
  link_libraries (${SLIBS})
endif()
if (CXX_LIBS)
  link_libraries ($<$<LINK_LANGUAGE:CXX>:${CXX_LIBS}>)
endif()

#===============================================================================
# Finally, process library source tree
#===============================================================================

add_subdirectory (${${COMP_NAME}_SOURCE_DIR}
                  ${${COMP_NAME}_BINARY_DIR})

