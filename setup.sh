# Update package lists
sudo apt update -y

# Upgrade installed packages
sudo apt upgrade -y

# Install pip required for Python packages
sudo apt install python3-pip -y

# Install Python packages
pip3 install -r requirements.txt