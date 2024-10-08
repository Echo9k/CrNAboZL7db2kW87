# Use the official Miniconda3 image as a base image
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the environment file and the current directory contents into the container at /usr/src/app
COPY environment.yml .
COPY . .

# Create the environment based on the environment.yaml file
RUN conda env create -f environment.yml

# Activate the environment
SHELL ["conda", "run", "-n", "happy-ml", "/bin/bash", "-c"]

# Install additional dependencies if needed
RUN conda install -c conda-forge lime  # Install LIME
RUN conda install -c conda-forge shap  # Install SHAP

# Make port 8501 available to the world outside this container (default Streamlit port)
EXPOSE 8501

# Set the entrypoint to activate the environment and run Streamlit
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "happy-ml", "streamlit", "run"]

# Run the Streamlit app when the container launches
CMD ["happy_customers.py", "--server.port=8501", "--server.headless=true"]
