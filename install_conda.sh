#!/bin/bash

# Update package lists
sudo apt update -y

# Upgrade installed packages
sudo apt upgrade -y

# install the conda environment
sudo apt install -y wget
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda

# Add conda to PATH
export PATH="$HOME/miniconda/bin:$PATH"

# Update conda
conda update -n base -c defaults conda -y

# conda init
conda init bash

# Restart bash
exec bash

# Create a new conda environment
conda create -f environment.yml

# Activate the conda environment
conda activate happy_customers