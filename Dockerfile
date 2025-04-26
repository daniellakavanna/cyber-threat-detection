# Use the official Lambda Python image as a base
FROM public.ecr.aws/lambda/python:3.9-slim

# Set the working directory
WORKDIR /var/task

# Copy the application code into the container
COPY src/ .

# Install your dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the Lambda function handler
CMD ["app.threat_detection_prediction_handler"]
