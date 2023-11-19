# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the pyproject.toml and poetry.lock files to install dependencies
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy the necessary files into the container
COPY models /app/models
COPY data /app/data

# Run ml_container_script.py when the container launches
CMD ["poetry", "run", "python3", "models/itemsets_generator.py"]