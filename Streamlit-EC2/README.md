# Streamlit Application Deployment on Amazon EC2

## 📌 Introduction
This project demonstrates how to deploy a **Streamlit** application on an **Amazon EC2** instance. Streamlit is a powerful Python framework for building interactive web applications with minimal effort. By hosting it on EC2, we make the application accessible over the internet with a public IP or domain name.

---
## 🚀 Features
- Deploy a **Streamlit** web application on an **AWS EC2 instance**
- Use **Ubuntu** as the OS for the EC2 instance
- Configure security groups to allow web traffic
- Run the app as a background service using **nohup** or **screen**
- Map a custom domain with **NGINX (optional)**

---
## 🛠 Prerequisites
Before proceeding, ensure you have the following:
- An **AWS** account
- A **Streamlit** application ready for deployment
- Basic knowledge of **Linux commands** and **SSH**

---
## 📦 Setup Guide
### 1️⃣ Launch an EC2 Instance
1. Log in to **AWS Console**.
2. Go to **EC2 Dashboard** → Click **Launch Instance**.
3. Choose an **Ubuntu** AMI (e.g., `Ubuntu 22.04 LTS`).
4. Select an instance type (e.g., `t2.micro` for free-tier usage).
5. Configure Security Group:
   - Allow **SSH (22)** from your IP.
   - Allow **HTTP (80)** and **HTTPS (443)** from anywhere.
6. Add a key pair for SSH access.
7. Launch the instance and note down its **public IP**.

### 2️⃣ Connect to the Instance via SSH
```sh
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

### 3️⃣ Install Required Packages
```sh
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip -y
```

### 4️⃣ Clone Your Streamlit App Repository
```sh
git clone https://github.com/your-username/your-streamlit-repo.git
cd your-streamlit-repo
```

### 5️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 6️⃣ Run Streamlit App
```sh
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```
The app will now be accessible at `http://your-ec2-public-ip:8501`.

---
## 🌍 Making It Publicly Accessible
### 1️⃣ Open Firewall for Streamlit (Port 8501)
```sh
sudo ufw allow 8501
```
### 2️⃣ Run Streamlit in the Background (Optional)
```sh
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &
```
This allows the app to keep running even after logging out.

---
## Use Render for deploying your application.
![Screenshot 2025-03-25 144037](https://github.com/user-attachments/assets/42b10b1b-f13b-4df2-99fc-2388a10b69d7)
![Screenshot 2025-03-25 144049](https://github.com/user-attachments/assets/8c786bee-2f4c-4fe1-8637-0ddc4691ed08)
Access it on
https://docknest-2.onrender.com/
![image](https://github.com/user-attachments/assets/fb15b66f-4d2e-438a-828b-55851572d8b5)



## 📜 License
This project is open-source under the **MIT License**.

---

## 📬 Contact
For any questions or issues, feel free to reach out:
- **GitHub**: [your-username](https://github.com/your-username)
- **Email**: your-email@example.com

