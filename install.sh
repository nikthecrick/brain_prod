#!/bin/bash

# Define the repository URL
REPO_URL="https://github.com/nikthecrick/brain_prod.git"

# Define the directory where you want to install the repository
INSTALL_DIR="$HOME/brain_prod"

# Define the target directory for the executable script
BIN_DIR="/usr/local/bin"

# Clone the repository
git clone $REPO_URL $INSTALL_DIR

# Check if the cloning was successful
if [ $? -eq 0 ]; then
    # Change directory to the installation directory
    cd $INSTALL_DIR

    # Install the requirements (assuming you have pip installed)
    pip3 install -r requirements.txt

    # Make the Python script executable
    # chmod +x brAIn.py

    # Copy the script to the bin directory (requires sudo)
    # sudo cp brain.py $BIN_DIR

    # Check if the copy was successful
    # if [ $? -eq 0 ]; then
    #     echo "Installation complete. You can now run 'brain.py' from anywhere."
    # else
    #     echo "Failed to copy the script to $BIN_DIR. Please make sure you have sudo privileges."
    # fi
# else
    # echo "Failed to clone the repository. Please check the repository URL or your internet connection."
fi
