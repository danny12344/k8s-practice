# Use a base image that includes Python and other dependencies
FROM ubuntu:latest

# Install Nginx and other necessary packages
RUN apt-get update && apt-get install -y nginx

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY ./app ./app

# Set the host and port for the FastAPI application
ENV HOST=0.0.0.0
ENV PORT=80

# Expose the port on which the FastAPI application will run
EXPOSE 80

# Set the command to start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
