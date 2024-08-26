#!/bin/bash

# Update package lists
sudo apt update -y

# Upgrade installed packages
sudo apt upgrade -y

# Install wget if not installed
sudo apt install -y wget

# Download and install Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda

# Add conda to PATH
export PATH="$HOME/miniconda/bin:$PATH"

# Initialize conda for bash
source $HOME/miniconda/bin/conda init bash

# Restart bash
exec bash

# Update conda
conda update -n base -c defaults conda -y

# Create a new conda environment from the environment.yml file
conda env create -f environment.yml

# Activate the conda environment
conda activate happy-ml

# Verify installation of Streamlit
streamlit --version
