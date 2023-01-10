FROM python:3.8-slim

# Create a working directory
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the app's code to the working directory
COPY . .

# Set the entrypoint to the Flask app
ENTRYPOINT ["python"]

# Set the command to start the Flask app
CMD ["server.py"]
