#! /usr/bin/env bash

# Assumes ~/bin is in $PATH 

# Assumes this script is run in same directory as $filename

# Absolute path of this script
ABSOLUTE_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"

# Name of directory where script is
DIR=`dirname $ABSOLUTE_PATH`

TARGET_DIR="$HOME/bin"


# Put symlink in $dir

# TODO avoid overwriting if $PROGRAM_NAME already exists in directory

cd $TARGET_DIR

FILENAME="sunrise"
PROGRAM_NAME="sunrise"
SCRIPT_PATH="$DIR/$FILENAME"

chmod +x $SCRIPT_PATH
cp -s $SCRIPT_PATH $PROGRAM_NAME

# REPEAT, but for other program 

FILENAME="sunset"
PROGRAM_NAME="sunset"
SCRIPT_PATH="$DIR/$FILENAME"

# Put symlink to next program in $dir 
chmod +x $SCRIPT_PATH
cp -s $SCRIPT_PATH $PROGRAM_NAME

