# Docker Bridge Networking Experiment

## 📌 Objective
The purpose of this experiment is to explore and demonstrate **network isolation** in Docker containers. We will examine how containers within the same **custom bridge network** can communicate, while those on different networks remain isolated. Understanding this is essential for securing **microservices and containerized applications**.

---
## 🌐 Introduction to Docker Networking
Docker networking enables communication between containers while maintaining security and isolation. Docker provides multiple networking options:

### 🔹 Types of Docker Networks:
- **Bridge Network (Default)** – Allows communication between containers using internal IPs unless restricted.
- **Custom Bridge Network** – Provides better control and supports name-based resolution.
- **Host Network** – Attaches containers directly to the host’s network stack.
- **Overlay Network** – Enables communication across multiple hosts (Docker Swarm).
- **Macvlan Network** – Assigns a MAC address to each container, making them appear as separate devices.
- **None Network** – Completely disables networking.

For this demonstration, we focus on the **custom bridge network**, which improves control and network isolation.

---
## ⚡ Why Use a Custom Bridge Network?
A **custom bridge network** offers several advantages:
✅ **Improved Security** – Containers on different networks are isolated by default.  
✅ **Better Performance** – Direct communication without host networking stack overhead.  
✅ **DNS-Based Resolution** – Containers communicate via names instead of IPs.  
✅ **Greater Control** – Define specific subnets, IP ranges, and gateways.  

To demonstrate, we create a **custom bridge network** and connect multiple containers.

---
## 🔧 1. Creating a Custom Bridge Network
Run the following command to create a custom bridge network:
```sh
docker network create --driver bridge --subnet 172.21.0.0/16 --ip-range 172.21.240.0/20 docknest-bridge
```
### 🔍 Explanation:
- `--driver bridge` → Uses the default bridge network mode.
- `--subnet 172.21.0.0/16` → Defines the network’s IP range.
- `--ip-range 172.21.240.0/20` → Allocates IPs dynamically.

---
## 🚀 2. Running Containers in the Custom Network
### Running a Database Container
```sh
docker run -itd --net=docknest-bridge --name=docknest-database redis
```
### Running an Application Container
```sh
docker run -itd --net=docknest-bridge --name=docknest-server-A busybox
```

---
## 📌 3. Check Container IPs
To inspect the network and retrieve container IP addresses, use:
```sh
docker network inspect docknest-bridge
```
✅ Expected Output Example:
```
docknest-database: 172.21.240.1
docknest-server-A: 172.21.240.2
```

---
## 📔 4. Testing Communication Between Containers
### Ping from `docknest-database` to `docknest-server-A`
```sh
docker exec -it docknest-database ping 172.21.240.2
```
### Ping from `docknest-server-A` to `docknest-database`
```sh
docker exec -it docknest-server-A ping 172.21.240.1
```
✅ Expected Outcome: Both containers should successfully ping each other.

---
## 🚧 5. Demonstrating Network Isolation with a Third Container
We now add another container (`docknest-server-B`) on the **default bridge network**.
```sh
docker run -itd --name=docknest-server-B busybox
```
### 📌 Get IP of `docknest-server-B`
```sh
docker inspect -format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' docknest-server-B
```
Example Output:
```
172.17.0.2
```

### ❌ 6. Testing Communication Between Different Networks
Attempting to ping `docknest-server-B` from `docknest-database`:
```sh
docker exec -it docknest-database ping 172.17.0.2
```
🚨 Expected Outcome: The ping should fail, as they are on different networks.

---
## 🔍 7. Confirming Network Isolation
To inspect the networks:
```sh
docker network inspect docknest-bridge
docker network inspect bridge
```
✅ `docknest-bridge` should contain `docknest-database` & `docknest-server-A`.  
✅ `bridge` should contain `docknest-server-B`.  

---
## 🏆 Conclusion
- Containers **within the same network** can communicate.
- Containers **on different networks** are **isolated by default**.
- Docker’s networking model ensures **security and separation** unless explicitly connected.

🚀 Now you have mastered Docker Bridge Networking! 🎯

---
## 📂 Project Structure
```
Docker-bridge-networking/
│-- Dockerfile
│-- README.md
│-- .gitignore
│-- src/
│   ├── app.py  (Sample Python app for testing)
│   ├── database.py (Database connectivity test script)
│-- requirements.txt
```

---
## 🚀 Pushing to GitHub
To push the project to GitHub, follow these steps:
```sh
git init
git add .
git commit -m "Initial commit - Docker Bridge Networking"
git branch -M main
git remote add origin https://github.com/ritu-pixel/DockNest.git
git push -u origin main
```

---
## 📜 License
This project is licensed under the **MIT License**.

Happy Coding! 🚀

