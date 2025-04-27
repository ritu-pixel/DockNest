# Streamlit Application Deployment on Amazon EC2

## Access the Streamlit application at:
https://docknest-fazewmfro2peqhq3bahmrc.streamlit.app/
<img width="959" alt="image" src="https://github.com/user-attachments/assets/220930d5-5204-43a0-ac57-364707672f71" />


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
   ![Screenshot 2025-03-23 224048](https://github.com/user-attachments/assets/8ee109b6-961b-4369-80e8-71a3362017cb)
   ![Screenshot 2025-03-23 224150](https://github.com/user-attachments/assets/505de16c-3b9b-428e-b94d-c50aa8957390)
   ![Screenshot 2025-03-23 224158](https://github.com/user-attachments/assets/79db428e-cc09-4989-a943-f0f74d3c98e8)
   ![Screenshot 2025-03-23 224338](https://github.com/user-attachments/assets/8d2e6f7d-72d1-4766-ab56-f7d3e106f514)
   ![Screenshot 2025-03-23 224534](https://github.com/user-attachments/assets/ff4ac4f3-ef42-440f-baf7-ecd642d4ce68)
   ![Screenshot 2025-03-23 224545](https://github.com/user-attachments/assets/94832f83-b7ed-4923-a2dc-53b7093afbcb)
   ![Screenshot 2025-03-23 225121](https://github.com/user-attachments/assets/8ed0e950-cf87-412e-b7c9-5f47da1a386b)
   ![Screenshot 2025-03-23 225259](https://github.com/user-attachments/assets/0138762f-c514-4df2-8e3a-d9c2d6d7dbdc)
   ![Screenshot 2025-03-23 225346](https://github.com/user-attachments/assets/e772a537-ac31-4410-9550-bb611fbcd241)
   ![Screenshot 2025-03-23 225414](https://github.com/user-attachments/assets/996c6811-d332-4b5f-95d7-5c674144b6a6)


2. Go to **EC2 Dashboard** → Click **Launch Instance**.
   ![Screenshot 2025-03-23 230009](https://github.com/user-attachments/assets/36ede19d-63cf-42c1-ab82-3d7dbeefe4d6)

5. Choose an **Ubuntu** AMI (e.g., `Ubuntu 22.04 LTS`).
6. Select an instance type (e.g., `t2.micro` for free-tier usage).
7. Configure Security Group:
   - Allow **SSH (22)** from your IP.
   - Allow **HTTP (80)** and **HTTPS (443)** from anywhere.
     ![Screenshot 2025-03-23 230447](https://github.com/user-attachments/assets/f8a533c4-bba4-4410-8951-f34e7b2cdcae)

8. Add a key pair for SSH access.
9. Launch the instance and note down its **public IP**.

### 2️⃣ Connect to the Instance via SSH
```sh
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```
![Screenshot 2025-03-23 234653](https://github.com/user-attachments/assets/54c9dcbd-d40c-453f-aad0-b147f3d8e665)

![Screenshot 2025-03-23 234618](https://github.com/user-attachments/assets/742767e1-004f-4d0a-a360-c2de5ea875b0)

### 3️⃣ Install Required Packages
```sh
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip -y
```
![Screenshot 2025-03-23 234627](https://github.com/user-attachments/assets/38550f49-6254-4a3e-b407-1c639c6d22fc)

### 4️⃣ Clone Your Streamlit App Repository
```sh
git clone https://github.com/your-username/your-streamlit-repo.git
cd your-streamlit-repo
```

### 5️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
![Screenshot 2025-03-23 234734](https://github.com/user-attachments/assets/a4f9e23c-0b5d-4b64-bc1e-3074c92db500)

### 6️⃣ Run Streamlit App
```sh
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```
The app will now be accessible at `http://your-ec2-public-ip:8501`.
![Screenshot 2025-03-23 234848](https://github.com/user-attachments/assets/5059fc31-c900-4dcc-8c6e-3f3f1ae0d4be)

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

