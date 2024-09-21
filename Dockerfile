# Use the official Python 3.11.9 image as the base image
FROM python:3.11.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the necessary files into the container
COPY app.py .
COPY Backend.py .
COPY your Google API credentials.json .

# Expose the port that Streamlit will run on (default is 8501)
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
