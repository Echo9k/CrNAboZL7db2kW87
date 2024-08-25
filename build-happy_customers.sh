# Build the Docker image
docker build -t happy_customers_app .

# Run the Docker container
docker run -p 8501:8501 happy_customers_app
