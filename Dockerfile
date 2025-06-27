FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

# Copy the app code
COPY . . 

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

#EXPOSE the port the app runs on
EXPOSE 5000

# commnad to run the app
CMD ["python3", "app.py"]