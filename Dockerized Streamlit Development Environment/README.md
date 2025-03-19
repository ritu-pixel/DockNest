#  **Dockerized Streamlit Development Environment**  

This guide helps you set up a **Streamlit application** inside a **Docker container** for an efficient and portable development experience. 🚀  

---

##  **Prerequisites**  
Before setting up the environment, ensure you have the following installed on your machine:  

🔹 **Docker**  (Ensure the Docker daemon is running)  
🔹 **Python 3.9+**  (Check installation with `python --version`)  
🔹 **pip**  (Ensure it's up to date with `pip --version`)  
🔹 **Basic knowledge of Streamlit**   

---

##  **Directory Structure**  

```
project_root/
│── .streamlit/
│   └── config.toml
│── src/
│   └── main.py
│── Dockerfile
│── requirements.txt
│── README.md
```
![Screenshot 2025-03-19 143005](https://github.com/user-attachments/assets/168870ad-140a-4f93-85e8-9780bf8d905f)
![Screenshot 2025-03-19 143019](https://github.com/user-attachments/assets/7d8ba107-6d66-4b0b-bdc8-e750d7242fcb)
![Screenshot 2025-03-19 143032](https://github.com/user-attachments/assets/667f1ec5-e553-4335-bc45-da9b03c987d8)



---

##  **File Explanations**  

### **1️ `.streamlit/config.toml`**  
This file configures Streamlit settings for local development.  

```toml
[server]
headless = true
runOnSave = true
fileWatcherType = "poll"
```

---

### **2️ `src/main.py`**  
This file contains the **core logic** of the Streamlit application, including:  

🏠 **Home Page** → Introduction to the app.  
📊 **Data Explorer** → Allows users to upload and inspect CSV files.  
📈 **Visualization Page** → Generates interactive charts and graphs.  

---

### **3️ `Dockerfile`**  
Defines the containerized environment for Streamlit.  

```dockerfile
# Use a lightweight Python image
FROM python:3.9-slim  

# Set working directory
WORKDIR /app  

# Copy dependencies and install them
COPY requirements.txt /app/  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy all project files
COPY . /app/  

# Expose Streamlit’s default port
EXPOSE 8501  

# Run the Streamlit app
CMD ["streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

### **4️ `requirements.txt`**  
Contains necessary dependencies:  

```text
streamlit
pandas
numpy
matplotlib
plotly
```

---

## ⚡ **Steps to Run the Project**  

### **1️ Navigate to the project directory**  
```bash
cd path/to/project_root
```

### **2️ Build the Docker image**  
```bash
docker build -t streamlit-app .
```

### **3️ Run the container**  
```bash
docker run -p 8501:8501 streamlit-app
```
![Screenshot 2025-03-19 144424](https://github.com/user-attachments/assets/8c7b2586-5470-4617-b636-fc61a58b7a8d)

### **4️ Open in Browser**  
🌐 Go to → [http://localhost:8501](http://localhost:8501)  

---

##  **Conclusion**  
You now have a **fully functional Streamlit environment** running inside Docker! 🚀  

![Screenshot 2025-03-19 144538](https://github.com/user-attachments/assets/7268f73f-a874-4610-93f1-11411d60b026)
![Screenshot 2025-03-19 144550](https://github.com/user-attachments/assets/82c20b7d-cc51-4d6b-85a3-559cd03c5024)
![Screenshot 2025-03-19 144602](https://github.com/user-attachments/assets/2cc12418-6f89-4e1c-8349-caee4dc18295)






💡 **Next Steps:**  
🔹 Add more features to your Streamlit app.  
🔹 Deploy the containerized app on **AWS, GCP, or Azure**.  
🔹 Experiment with **Docker Compose** for multi-container applications.  

🚀 **Happy Coding!** 🐳💙
