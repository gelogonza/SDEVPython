# Indicate the base image for the Python environment
FROM python:3

# Set the working directory inside the container
WORKDIR /opt/myApp

# Copy over the Python application file and requirements.txt
COPY tip.py .
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Define the command to run the Python application
CMD ["python", "tip.py"]
