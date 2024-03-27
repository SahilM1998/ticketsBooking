# Use the official Python Alpine image as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY main.py .

# Install dependencies
RUN pip install requests beautifulsoup4

# Set the command to run the script
CMD ["python", "main.py"]