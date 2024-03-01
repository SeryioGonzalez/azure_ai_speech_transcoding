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
include examples/CMakeFiles/srt2vtt.dir/depend.make

# Include the progress variables for this target.
include examples/CMakeFiles/srt2vtt.dir/progress.make

# Include the compile flags for this target's objects.
include examples/CMakeFiles/srt2vtt.dir/flags.make

examples/CMakeFiles/srt2vtt.dir/srt2vtt.c.o: examples/CMakeFiles/srt2vtt.dir/flags.make
examples/CMakeFiles/srt2vtt.dir/srt2vtt.c.o: examples/srt2vtt.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object examples/CMakeFiles/srt2vtt.dir/srt2vtt.c.o"
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/srt2vtt.dir/srt2vtt.c.o   -c /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples/srt2vtt.c

examples/CMakeFiles/srt2vtt.dir/srt2vtt.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/srt2vtt.dir/srt2vtt.c.i"
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples/srt2vtt.c > CMakeFiles/srt2vtt.dir/srt2vtt.c.i

examples/CMakeFiles/srt2vtt.dir/srt2vtt.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/srt2vtt.dir/srt2vtt.c.s"
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples/srt2vtt.c -o CMakeFiles/srt2vtt.dir/srt2vtt.c.s

# Object files for target srt2vtt
srt2vtt_OBJECTS = \
"CMakeFiles/srt2vtt.dir/srt2vtt.c.o"

# External object files for target srt2vtt
srt2vtt_EXTERNAL_OBJECTS =

examples/srt2vtt: examples/CMakeFiles/srt2vtt.dir/srt2vtt.c.o
examples/srt2vtt: examples/CMakeFiles/srt2vtt.dir/build.make
examples/srt2vtt: libcaption.a
examples/srt2vtt: examples/CMakeFiles/srt2vtt.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable srt2vtt"
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/srt2vtt.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/CMakeFiles/srt2vtt.dir/build: examples/srt2vtt

.PHONY : examples/CMakeFiles/srt2vtt.dir/build

examples/CMakeFiles/srt2vtt.dir/clean:
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples && $(CMAKE_COMMAND) -P CMakeFiles/srt2vtt.dir/cmake_clean.cmake
.PHONY : examples/CMakeFiles/srt2vtt.dir/clean

examples/CMakeFiles/srt2vtt.dir/depend:
	cd /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples /home/sergio/amazon-transcribe-streaming-live-closed-captions/libcaption/examples/CMakeFiles/srt2vtt.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/CMakeFiles/srt2vtt.dir/depend

