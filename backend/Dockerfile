# Base image
FROM python:3.9-slim

# Set environment variables to accept the Microsoft ODBC driver license and non-interactive installation
ENV ACCEPT_EULA=Y \
    DEBIAN_FRONTEND=noninteractive

# Install required packages and SQL Server ODBC driver
RUN apt-get update && apt-get install -y \
    build-essential \
    unixodbc-dev \
    curl \
    gnupg2 \
    apt-transport-https \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && apt-get install -y msodbcsql18

# Set working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the Flask app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
