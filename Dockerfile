# Use the official Python 3.9 slim image as a parent image
# Use the official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port 8080
EXPOSE 8080

# Run the app using Gunicorn
CMD exec gunicorn --bind :$PORT main:app
