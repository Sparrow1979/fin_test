# Use the specific Python runtime as a parent image
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    default-libmysqlclient-dev \
    gcc \
    python3-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY finlite/requirements.txt .

# Create the virtual environment and install dependencies
RUN python -m venv venv && \
    /usr/src/app/venv/bin/pip install --upgrade pip && \
    /usr/src/app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Command to run the Django server
#CMD [ "sh", "-c", "until nc -z db 3306; do echo 'Waiting for db...'; sleep 5; done && /usr/src/app/venv/bin/python finlite/manage.py migrate && /usr/src/app/venv/bin/python finlite/manage.py createsuperuser --noinput && /usr/src/app/venv/bin/python finlite/manage.py runserver 0.0.0.0:8000" ]
# Command to run the Django server
CMD [ "sh", "-c", "until nc -z db 3306; do echo 'Waiting for db...'; sleep 5; done && /usr/src/app/venv/bin/python finlite/manage.py migrate && /usr/src/app/venv/bin/python finlite/manage.py createsuperuser --noinput && /usr/src/app/venv/bin/python finlite/manage.py runserver 0.0.0.0:8000" ]
