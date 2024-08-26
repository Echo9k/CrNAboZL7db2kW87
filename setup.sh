# Update package lists
apt update -y

# Upgrade installed packages
apt upgrade -y

# Install pip required for Python packages
apt install python3-pip -y

# Install Python packages
pip3 install -r requirements.txt