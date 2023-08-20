# Use the tiangolo/uvicorn-gunicorn base image with Python 3.8
FROM tiangolo/uvicorn-gunicorn:python3.8

# Set the working directory inside the container
WORKDIR /app

# Copy your application files to the container's working directory
COPY ./app /app

# Install any additional dependencies if needed
RUN pip install -r /app/requirements.txt

# Expose the port that your application will listen on
EXPOSE 80

# Command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
