# Happy Customers Prediction App

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-brightgreen)](https://happy-customers-conda.onrender.com/)

This repository contains the code for the "Happy Customers" prediction app, which predicts customer satisfaction based on two key features: the timeliness of order delivery and whether the customer received everything they ordered. The app also includes an explanation of the model's predictions using LIME (Local Interpretable Model-agnostic Explanations) to help decision-makers understand and trust the model's output.

## Project Overview

The app allows users to input two key variables:
- **X1**: Order delivered on time (1 to 5 scale).
- **X3**: Ordered everything wanted (1 to 5 scale).

The model predicts customer satisfaction and provides insights into the reasoning behind the prediction by displaying interaction features and using LIME to explain the contributions of each feature.

## Quick Start

You can access the live app directly [here](https://happy-customers-conda.onrender.com/).

Alternatively, you can run the app locally using Docker or Conda.

## Requirements

- Docker (for Docker installation)
- Conda (for Conda installation)
- Python 3.10 or higher
- and a bunch of libraries

## Installation and Setup

### 1. System Update

Before starting, ensure your system is up to date:

```bash
# Update package lists
sudo apt update -y

# Upgrade installed packages
sudo apt upgrade -y
```

### 2 Installation

#### 2.1 Docker Installation

To run the app using Docker:

```bash
# Build the Docker image
docker build -t happy_customers_app .
```

```bash
# Run the Docker container
docker run -p 8501:8501 happy_customers_app
```

#### 2.2 Conda Installation

To run the app using Conda:

```bash
# Create a new Conda environment
conda create -f environment.yml
```

After creating the environment, activate it:

```bash
conda activate happy_customers
```

Then, run the Streamlit app:

```bash
streamlit run ./happy_customers.py
```

#### 2.3 Pip installation

```python
# Create a new Conda environment
pip install requirements.txt
```



## Usage

Once the app is running, you can interact with it by adjusting the sliders for the two key variables (X1 and X3). The app will display the predicted customer satisfaction along with the probability of the prediction and an interpretation of how each feature contributed to the prediction using LIME.

## Development and Contribution

If you want to contribute to the development of this app, you can clone the repository and set up your development environment using the instructions above. Pull requests are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please feel free to reach out via email or open an issue on GitHub.

