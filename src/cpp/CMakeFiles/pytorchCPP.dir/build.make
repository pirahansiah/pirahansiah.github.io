# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.27.4/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.27.4/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/farshid/farshid/pirahansiah.github.io/src/cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/farshid/farshid/pirahansiah.github.io/src/cpp

# Include any dependencies generated for this target.
include CMakeFiles/pytorchCPP.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/pytorchCPP.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/pytorchCPP.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/pytorchCPP.dir/flags.make

CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.o: CMakeFiles/pytorchCPP.dir/flags.make
CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.o: src/pytorchCPP.cpp
CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.o: CMakeFiles/pytorchCPP.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/farshid/farshid/pirahansiah.github.io/src/cpp/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.o -MF CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.o.d -o CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.o -c /Users/farshid/farshid/pirahansiah.github.io/src/cpp/src/pytorchCPP.cpp

CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/farshid/farshid/pirahansiah.github.io/src/cpp/src/pytorchCPP.cpp > CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.i

CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/farshid/farshid/pirahansiah.github.io/src/cpp/src/pytorchCPP.cpp -o CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.s

# Object files for target pytorchCPP
pytorchCPP_OBJECTS = \
"CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.o"

# External object files for target pytorchCPP
pytorchCPP_EXTERNAL_OBJECTS =

pytorchCPP: CMakeFiles/pytorchCPP.dir/src/pytorchCPP.cpp.o
pytorchCPP: CMakeFiles/pytorchCPP.dir/build.make
pytorchCPP: CMakeFiles/pytorchCPP.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/farshid/farshid/pirahansiah.github.io/src/cpp/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable pytorchCPP"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pytorchCPP.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/pytorchCPP.dir/build: pytorchCPP
.PHONY : CMakeFiles/pytorchCPP.dir/build

CMakeFiles/pytorchCPP.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/pytorchCPP.dir/cmake_clean.cmake
.PHONY : CMakeFiles/pytorchCPP.dir/clean

CMakeFiles/pytorchCPP.dir/depend:
	cd /Users/farshid/farshid/pirahansiah.github.io/src/cpp && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/farshid/farshid/pirahansiah.github.io/src/cpp /Users/farshid/farshid/pirahansiah.github.io/src/cpp /Users/farshid/farshid/pirahansiah.github.io/src/cpp /Users/farshid/farshid/pirahansiah.github.io/src/cpp /Users/farshid/farshid/pirahansiah.github.io/src/cpp/CMakeFiles/pytorchCPP.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/pytorchCPP.dir/depend
