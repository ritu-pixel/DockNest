# Microservices Architecture with Docker Swarm

This project demonstrates how to deploy a microservices architecture using **Docker Swarm**. The architecture consists of an **API Gateway** and a **Backend Service**, both running as separate services in a Swarm cluster.

---

##  Project Structure
```
microservices-docker-swarm/
│── backend-service/
│   ├── backend.py
│   ├── Dockerfile
│
│── api-gateway/
│   ├── api_gateway.py
│   ├── Dockerfile
│
│── docker-compose.yml
│── README.md
```

---

##  Step 1: Install Docker & Initialize Docker Swarm

### 1.1 Install Docker
Ensure Docker is installed on your machine. Verify the installation:
```sh
docker --version
```
![image](https://github.com/user-attachments/assets/ed68b36a-7880-4ab0-b87c-15110e875221)

If not installed, download Docker from the [official website](https://www.docker.com/) and install it.

> **Note**: Docker Desktop must be running in the background for Docker Swarm to work properly.

### 1.2 Initialize Docker Swarm
Start Docker Swarm by running:
```sh
docker swarm init
```
![image](https://github.com/user-attachments/assets/b8f41e4e-90b9-48f3-ae9a-34e5ab44d036)

This will initialize your machine as a Swarm Manager.

---

##  Step 2: Create the Microservices

### Backend Service
Create `backend.py`:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "rajput_ritu"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```
Create `Dockerfile` for the backend service:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY backend.py /app
RUN pip install flask
CMD ["python", "backend.py"]
```

### API Gateway Service
Create `api_gateway.py`:
```python
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    backend_response = requests.get('http://backend-service:5000')
    return f"API Gateway: {backend_response.text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```
Create `Dockerfile` for the API Gateway:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY api_gateway.py /app
RUN pip install flask requests
CMD ["python", "api_gateway.py"]
```

---

##  Step 3: Build Docker Images

Build the Docker images for both services:
```sh
docker build -t backend-service ./backend-service
docker build -t api-gateway ./api-gateway
```
![image](https://github.com/user-attachments/assets/a0b2a50a-50ad-4d63-9253-be10e1e6c9fd)
![image](https://github.com/user-attachments/assets/8a75c69c-a156-4029-9010-ae1ee3c71306)

Verify the images:
```sh
docker images
```
![image](https://github.com/user-attachments/assets/980b321c-43b5-4245-895c-712bd1de9b04)

---

##  Step 4: Create Docker Compose File for Swarm

Create `docker-compose.yml`:
```yaml
version: '3.7'

services:
  backend-service:
    image: backend-service
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
    networks:
      - app-network
    ports:
      - "5000:5000"

  api-gateway:
    image: api-gateway
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
    networks:
      - app-network
    ports:
      - "8080:8080"
    depends_on:
      - backend-service

networks:
  app-network:
    driver: overlay
```

---

##  Step 5: Deploy the Microservices to Docker Swarm

Deploy the stack using Docker Swarm:
```sh
docker stack deploy -c docker-compose.yml my_microservices
```
![image](https://github.com/user-attachments/assets/913d490d-687d-4259-9811-dcfba409fc75)

---

##  Step 6: Verify the Deployment

Check the running services:
```sh
docker stack services my_microservices
```
![image](https://github.com/user-attachments/assets/1866b649-e8ba-4486-9a64-bc4f1fc9a1df)

List running containers:
```sh
docker ps
```

---

##  Step 7: Access the Microservices

Open your browser and visit:
```
http://localhost:8080
```
![Screenshot 2025-03-22 184836](https://github.com/user-attachments/assets/97045e89-358e-4204-9688-00bcac92c5a6)

Expected Output:
```
API Gateway: rajput_ritu
```

Alternatively, test using `curl`:
```sh
curl http://localhost:8080
```

---

##  Step 8: Scaling the Services

Scale the backend service to 5 replicas:
```sh
docker service scale my_microservices_backend-service=5

```
![image](https://github.com/user-attachments/assets/dc23a229-c15b-46e0-a5a0-9f9185e3baa8)

Verify scaling:
```sh
docker stack services my_microservices
```
![image](https://github.com/user-attachments/assets/646eb0dc-7b44-4155-84e5-a27f35790eee)

---

##  Step 9: Updating the Services

If you modify `backend.py`, rebuild and update the service:
```sh
docker build -t backend-service ./backend-service
docker service update --image backend-service:latest my_microservices_backend-service
```
![image](https://github.com/user-attachments/assets/9594c278-a1c5-490a-a93b-6599077b0f57)

If the update does not reflect, force the update:
```sh
docker service update --force --image backend-service:latest my_microservices_backend-service
```

---

##  Step 10: Remove the Stack

To stop and remove the microservices:
```sh
docker stack rm my_microservices
docker swarm leave --force
```
![image](https://github.com/user-attachments/assets/ed5ee84e-9c32-4e66-be80-0422f8f761fd)

---

##  Conclusion
This project demonstrates how to deploy a simple microservices architecture using **Docker Swarm**. You learned how to:
- Build and deploy microservices using Swarm.
- Use an API Gateway to route requests to a backend service.
- Scale services dynamically.
- Update services without downtime.

Now you can extend this setup by adding more microservices, databases, or load balancing strategies! 🚀

---

##  Author
**Ritu Rajput**

Happy coding! 


