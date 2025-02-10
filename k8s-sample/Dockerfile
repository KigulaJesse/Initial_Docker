# Use an official lightweight Python image
FROM python:3.9-slim
# Set working directory
WORKDIR /app
# Copy files to container
COPY . .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose the port the app runs on
EXPOSE 5001
# Command to run the app
CMD ["python", "app.py"]
