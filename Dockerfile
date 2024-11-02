# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the container
COPY . .

# Specify the command to run your application
CMD ["python", "main.py"]
