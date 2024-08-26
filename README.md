
```bash
# Update package lists
sudo apt update -y
```

```bash
# Upgrade installed packages
sudo apt upgrade -y
```

# Docker Installation

```bash
# Build the Docker image
docker build -t happy_customers_app .
```

```bash
# Run the Docker container
docker run -p 8501:8501 happy_customers_app
```

# Conda Installation

```bash
# Create a new Conda environment
conda create -f environment.yml
```