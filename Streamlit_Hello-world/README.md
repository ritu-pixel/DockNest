# Docker Basics: Hello World Project 

Welcome to the **Docker Hello World** project! This experiment walks you through the basics of Docker by creating and running a simple Python application inside a container.

---

##  Prerequisites
Before you begin, ensure you have the following installed on your system:

- **Docker**: A platform for developing, shipping, and running applications in containers.  
   Download: [Docker Desktop](https://www.docker.com/get-started/)
- **Python**: A programming language used to write the application.  
   Download: [Python](https://www.python.org/downloads/)

To verify installations, run the following commands:
```bash
# Check Docker version
docker --version

# Check Python version
python --version
```

---

## Step 1: Setting Up the Project
### 1.1 Create a Project Directory
```bash
mkdir Docker_Hello_World && cd Docker_Hello_World
```

### 1.2 Create a Python File (`app.py`)
Create a new file named `app.py` and add the following code:
```python
# app.py
print("Hello World! ")
```

---

##  Step 2: Creating a Dockerfile
A **Dockerfile** contains instructions to build and run a Docker image.

Create a file named `Dockerfile` (no extension) and add the following:
```dockerfile
# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the Python script
CMD ["python", "app.py"]
```

---

##  Step 3: Building the Docker Image
Now, build the Docker image using the following command:
```bash
docker build -t hello-world-app .
```
- `-t hello-world-app` → Tags the image with the name "hello-world-app".
- `.` → Specifies the current directory as the build context.
  ![Screenshot 2025-03-20 104648](https://github.com/user-attachments/assets/e9aba67b-763d-4e40-9c1f-d6beedc8077c)

  


Verify the image was created:
```bash
docker images
```
Expected output:
```
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
hello-world-app     latest    abc123def456   10 seconds ago   123MB
```

---

##  Step 4: Running the Docker Container
To execute the Python script inside a container, run:
```bash
docker run hello-world-app
```
Expected output:
```
Hello World! 
```
![Screenshot 2025-03-20 104725](https://github.com/user-attachments/assets/e0a4aa8e-f01f-4a73-a6e0-1e83ceb04414)

---

##  Step 5: Managing the Docker Container
### Check Running Containers
```bash
docker ps
```

### Stop the Container
```bash
docker stop <container_id>
```

### Remove the Container
```bash
docker rm <container_id>
```

### Remove the Docker Image
```bash
docker rmi hello-world-app
```

---

##  Conclusion
 Congratulations! You have successfully created and run your first Dockerized Python application. 🚀🐳  

This project covered:
Installing Docker & Python  
Writing a simple Python script  
Creating a Dockerfile  
Building and running a Docker container  
Managing Docker images & containers  

Next Steps:
- Try modifying the Python script to add user inputs.
- Build a simple **Flask** or **Streamlit** app and deploy it in Docker.
- Explore **Docker Compose** for multi-container applications.

Happy coding! 

