#!/bin/sh

echo -e "Using pip version: $(pip --version)\n"

REPO_FOLDER=$(pwd)
LOCAL_LIB_FOLDER="$REPO_FOLDER/local_lib"
LOG_FILE="$REPO_FOLDER/install_log.log"
PATH_GIT="https://github.com/jaraco/path.git"

echo "Installing path.py development version to local_lib folder..."

# Install path.py to local_lib folder and write logs to install_log.log
pip install --log $LOG_FILE --target $LOCAL_LIB_FOLDER --force-reinstall git+$PATH_GIT

# execute the small program
python3 my_program.py
