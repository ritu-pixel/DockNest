#  Python Logging Application with Docker

This project demonstrates how to create a Python application that logs data continuously to a file while running inside a Docker container. The logs are stored persistently in a Docker volume to ensure they remain available even if the container is stopped or removed.

---

##  Project Structure
```
.
├── app.py            # Python application that generates logs
├── Dockerfile        # Dockerfile to build the image
└── README.md         # Project documentation
```

---

## 📥 Prerequisites
Before starting, make sure you have Docker installed on your system.
- [Download Docker](https://www.docker.com/get-started)

---

##  Steps to Build and Run the Application

###  Step 1: Write the Python Application
Create a file named `app.py` with the following content:

```python
import os
import time

os.makedirs("/data", exist_ok=True)  # Ensure directory exists

with open("/data/app.log", "a") as log_file:
    while True:
        log_file.write(f"App is running at {time.ctime()}\n")
        log_file.flush()
        time.sleep(5)
```
This script writes a log entry every 5 seconds to `/data/app.log`.

###  Step 2: Create a Dockerfile
Create a file named `Dockerfile` with the following content:

```dockerfile
# Use a base Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY app.py /app/app.py

# Run the Python application
CMD ["python", "app.py"]
```

###  Step 3: Build the Docker Image
Run the following command to build the Docker image:

```bash
docker build -t python-log-app .
```

This will create an image named `python-log-app`.
![image](https://github.com/user-attachments/assets/fd350fb4-ec34-46be-b12a-f62abf35b900)


###  Step 4: Run the Docker Container with a Volume
To ensure logs are persisted, mount a Docker volume and run the container:

```bash
docker volume create my-app-data
docker run -d --name python-log-container -v my-app-data:/data python-log-app
```

**Explanation:**
- `-d`: Runs the container in detached mode.
- `-v my-app-data:/data`: Mounts the volume `my-app-data` to the `/data` directory inside the container.

###  Step 5: Verify Logs
1. **Check if the container is running:**
    ```bash
    docker ps
    ```
    ![image](https://github.com/user-attachments/assets/d69e5e36-2a43-4595-ab5b-79d1f7b97e76)

2. **View logs from the container:**
    ```bash
    docker logs <container_id/name>

    ```
    ![image](https://github.com/user-attachments/assets/73cdc884-b92e-4911-b7b5-17c6637cf4c9)

3. **Access the log file inside the container:**
    ```bash
    docker exec -it python-log-container sh
    cd /data
    cat app.log
    ```
    ![image](https://github.com/user-attachments/assets/8d404828-b218-4477-b207-8dd77207589e)

4. **Inspect the volume on the host system:**
    ```bash
    docker volume inspect my-app-data
    ```
![image](https://github.com/user-attachments/assets/87b41d72-1fb9-4f98-a40b-aec44744cd53)

###  Stopping and Cleaning Up
1. **Stop the container:**
    ```bash
    docker stop python-log-container
    ```
    ![image](https://github.com/user-attachments/assets/789a4efe-3cb9-4087-aac1-76b3653e3a2d)

2. **Remove the container:**
    ```bash
    docker rm python-log-container
    ```
    ![image](https://github.com/user-attachments/assets/2a6e178f-cc2f-4eac-99da-acc0bd681508)

3. **Remove the image (if needed):**
    ```bash
    docker rmi python-log-app
    ```
4. **Remove the volume (if needed):**
    ```bash
    docker volume rm my-app-data
    ```
![image](https://github.com/user-attachments/assets/c0b7f433-d2c1-4cd2-af19-1b459d4b483b)

---

##  Notes
- The logs are stored persistently in the Docker volume `my-app-data`.
- You can use `docker volume inspect my-app-data` to locate and analyze the logs on the host system.
 **Happy Logging with Docker!** 

