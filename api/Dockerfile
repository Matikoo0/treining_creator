# Use an official Ubuntu runtime as the base image
FROM ubuntu:latest


# Update packages and install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy the application source code
COPY  / /app/api/

# Set the working directory
WORKDIR /app/api

# Install Python dependencies
#RUN pip3 install flask flask-SQLAlchemy
RUN pip3 install --no-cache-dir -r ../requirements.txt

# Run the command to start the application
#
CMD ["python3", "main.py"]
