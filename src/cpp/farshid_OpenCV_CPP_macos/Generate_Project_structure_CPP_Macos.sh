#!/bin/bash

# Project name
PROJECT_NAME="farshid_OpenCV_CPP_macos"

# Create main project directory
mkdir -p $PROJECT_NAME

# Create CMakeLists.txt in the project root
touch $PROJECT_NAME/CMakeLists.txt

# Create build/ and bin/ directories
mkdir -p $PROJECT_NAME/build
mkdir -p $PROJECT_NAME/bin

# Create tools_demo file in bin/ (optional, as a placeholder)
touch $PROJECT_NAME/bin/tools_demo

# Create lib/ directory and libtools.a file
mkdir -p $PROJECT_NAME/lib
touch $PROJECT_NAME/lib/libtools.a

# Create src/ directory with subdirectories and files
mkdir -p $PROJECT_NAME/src/$PROJECT_NAME
touch $PROJECT_NAME/src/CMakeLists.txt
touch $PROJECT_NAME/src/$PROJECT_NAME/CMakeLists.txt
touch $PROJECT_NAME/src/$PROJECT_NAME/tools.h
touch $PROJECT_NAME/src/$PROJECT_NAME/tools.cpp
touch $PROJECT_NAME/src/$PROJECT_NAME/tools_demo.cpp
touch $PROJECT_NAME/src/$PROJECT_NAME/main.cpp

# Create tests/ directory with test_tools.cpp and CMakeLists.txt
mkdir -p $PROJECT_NAME/tests
touch $PROJECT_NAME/tests/test_tools.cpp
touch $PROJECT_NAME/tests/CMakeLists.txt

# Create a readme.md file
touch $PROJECT_NAME/readme.md

# Copy .vscode directory with all its contents into the main root directory
# Ensure the .vscode folder is in the same directory as this script or provide the full path
if [ -d "./.vscode" ]; then
  cp -r .vscode $PROJECT_NAME/
  echo ".vscode directory copied to $PROJECT_NAME/"
else
  echo ".vscode directory not found. Make sure it exists in the current directory."
fi

# Print a success message
echo "Project structure has been created."