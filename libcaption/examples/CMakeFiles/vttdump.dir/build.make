# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption

# Include any dependencies generated for this target.
include examples/CMakeFiles/vttdump.dir/depend.make

# Include the progress variables for this target.
include examples/CMakeFiles/vttdump.dir/progress.make

# Include the compile flags for this target's objects.
include examples/CMakeFiles/vttdump.dir/flags.make

examples/CMakeFiles/vttdump.dir/vttdump.c.o: examples/CMakeFiles/vttdump.dir/flags.make
examples/CMakeFiles/vttdump.dir/vttdump.c.o: examples/vttdump.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object examples/CMakeFiles/vttdump.dir/vttdump.c.o"
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/vttdump.dir/vttdump.c.o   -c /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples/vttdump.c

examples/CMakeFiles/vttdump.dir/vttdump.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/vttdump.dir/vttdump.c.i"
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples/vttdump.c > CMakeFiles/vttdump.dir/vttdump.c.i

examples/CMakeFiles/vttdump.dir/vttdump.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/vttdump.dir/vttdump.c.s"
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples/vttdump.c -o CMakeFiles/vttdump.dir/vttdump.c.s

# Object files for target vttdump
vttdump_OBJECTS = \
"CMakeFiles/vttdump.dir/vttdump.c.o"

# External object files for target vttdump
vttdump_EXTERNAL_OBJECTS =

examples/vttdump: examples/CMakeFiles/vttdump.dir/vttdump.c.o
examples/vttdump: examples/CMakeFiles/vttdump.dir/build.make
examples/vttdump: libcaption.a
examples/vttdump: examples/CMakeFiles/vttdump.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable vttdump"
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/vttdump.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/CMakeFiles/vttdump.dir/build: examples/vttdump

.PHONY : examples/CMakeFiles/vttdump.dir/build

examples/CMakeFiles/vttdump.dir/clean:
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples && $(CMAKE_COMMAND) -P CMakeFiles/vttdump.dir/cmake_clean.cmake
.PHONY : examples/CMakeFiles/vttdump.dir/clean

examples/CMakeFiles/vttdump.dir/depend:
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples/CMakeFiles/vttdump.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/CMakeFiles/vttdump.dir/depend
