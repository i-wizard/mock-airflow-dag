# Use the official Python image as the base image
FROM python:3.10.0-slim 

# Set environment variables for Python and output buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code to the working directory
COPY . .

# Expose port 8000
EXPOSE 8000

# Copy settup script
COPY ./setup.sh /setup.sh

# Make script executable
RUN chmod +x /setup.sh

CMD ["/setup.sh"]

