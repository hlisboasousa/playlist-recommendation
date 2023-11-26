# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the pyproject.toml and poetry.lock files to install dependencies
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry
RUN pip install flask

# Install project dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-root

# Copy the necessary files into the container
COPY api/ /app/api
COPY datasets/ /app/datasets
COPY itemsets.pickle /app/itemsets.pickle

EXPOSE 32185

# Run the Flask app using Poetry
CMD ["poetry", "run", "flask", "--app", "api/app.py", "run", "--port", "32185", "--host=0.0.0.0"]
