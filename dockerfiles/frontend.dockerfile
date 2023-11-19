# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the frontend files into the container at /app/frontend
COPY frontend /app/frontend

WORKDIR /app/frontend

# Expose port 8000 to the outside world
EXPOSE 8000

# Run python3 -m http.server when the container launches
CMD ["python3", "-m", "http.server", "8000"]
