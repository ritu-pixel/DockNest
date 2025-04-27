# 🚀 Docker Volume Persistence: Bind Mounts on Linux Container 🐳

## 📌 Introduction  
This guide demonstrates **how to use Docker bind mounts** with a Linux container to persist data beyond a container’s lifecycle. Bind mounts allow a **host directory** to be mounted inside a container, ensuring that the data persists even when the container is removed.

---
## 🔧 **Setup Steps & Observations**  

### 🏗 **Step 1: Run a Container with a Bind Mount**
Run the following command to start an Alpine Linux container with a bind mount:
```sh
 docker run -dit --name alpine_with_bind_mount -v C:\Users\asus\docker_data:/data alpine:latest sh
```
### 🔍 **What Happens?**
- If `alpine:latest` is not available locally, Docker pulls it.
- A new container named `alpine_with_bind_mount` is created.
- The `-v` flag mounts the local folder `C:\Users\asus\docker_data` to `/data` inside the container.
- The container starts a shell (`sh`) in detached mode.

---
### 📄 **Step 2: Create a File Inside the Bind Mount**
Inside the container, create a file inside `/data`:
```sh
 docker exec -it alpine_with_bind_mount sh -c "echo 'Hello, Docker!' > /data/testfile.txt"
```
![image](https://github.com/user-attachments/assets/bbe88a31-28a8-46b0-afb5-c537aa6ac467)


### 🔍 **What Happens?**
- The command runs a shell inside the running container.
- A file `testfile.txt` is created inside `/data` and contains `Hello, Docker!`.
- Since `/data` is bind-mounted, the file actually exists in `C:\Users\asus\docker_data` on the host.

---
### ✅ **Step 3: Verify File Persistence**
To check if the file exists inside the container:
```sh
 docker exec -it alpine_with_bind_mount sh -c "cat /data/testfile.txt"
```
📌 **Expected Output:**
```
Hello, Docker!
```
To check the file from the **Windows host**:
```powershell
 type C:\Users\asus\docker_data\testfile.txt
```
---
### 🗑 **Step 4: Remove the Container**
Now, remove the container and check if the file persists:
```sh
 docker rm -f alpine_with_bind_mount
```
![image](https://github.com/user-attachments/assets/5867e94a-657e-4a2a-a905-03ec51e6ce6c)

### 🔍 **What Happens?**
- The container is **stopped and deleted**.
- Since `testfile.txt` is inside the **bind-mounted directory**, it **remains on the host**.

---
### 🔄 **Step 5: Create a New Container with the Same Bind Mount**
Start a new container and mount the same folder:
```sh
 docker run -dit --name new_alpine -v C:\Users\docker_data:/data alpine sh
```
### 🔍 **What Happens?**
- A new container named `new_alpine` is created.
- The **same** bind-mounted directory (`C:\Users\docker_data`) is mounted to `/data`.

---
### 🔎 **Step 6: Verify File Persistence in the New Container**
Check if `testfile.txt` still exists inside the **new** container:
```sh
 docker exec -it new_alpine sh -c "cat /data/testfile.txt"
```
📌 **Expected Output:**
```
Hello, Docker!
```
🚀 **The file persists even after the first container is deleted!** 🔥

---
## 🎯 **Key Takeaways**
✅ **Bind mounts persist data beyond a container’s lifecycle.**  
✅ **Deleting a container does NOT delete bind-mounted files.**  
✅ **New containers with the same mount can access previous container data.**  
✅ **Useful for sharing files between containers.**  

---
## 🚀 **Next Steps**
🔹 **Try Named Volumes (Instead of Bind Mounts)**  
```sh
 docker volume create my_data_volume
 docker run -dit --name alpine_with_volume -v my_data_volume:/data alpine sh
```
![image](https://github.com/user-attachments/assets/a4b073d1-6cb8-4c84-99b0-da6fae242a31)

🔹 **Experiment with Different Containers**  
Mount the same directory in **Ubuntu**:
```sh
 docker run -dit --name ubuntu_test -v C:\Users\asus\docker_data:/data ubuntu bash
```
🔹 **Explore File Permissions Across Containers**
```sh
 ls -l /data
```
🔹 **Mount Multiple Directories in One Container**
```sh
 docker run -dit --name multi_mount \
  -v C:\Users\asus\docker_data:/data \
  -v C:\Users\asus\logs:/logs \
  alpine sh
```

---
### 🎉 **Congratulations! You Now Understand Docker Bind Mounts!** 🚀🐳

