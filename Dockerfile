# Use the official Python Alpine image as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY main.py .

# Install dependencies
RUN pip install requests beautifulsoup4

# Add crontab file
ADD crontab /etc/crontabs/root

# Run cron in the foreground
CMD ["crond", "-f"]
