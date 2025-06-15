FROM python:3.11-slim

# Update package lists and upgrade security patches
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --deploy --system

# Copy the application code
COPY . .

CMD ["python3", "src/main.py"]