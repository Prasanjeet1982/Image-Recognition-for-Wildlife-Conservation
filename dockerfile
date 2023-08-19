# Use the official TensorFlow Docker image as the base image
FROM tensorflow/tensorflow:2.6.0

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install project dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Expose the port that the FastAPI server will run on
EXPOSE 8000

# Command to start the FastAPI server using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
