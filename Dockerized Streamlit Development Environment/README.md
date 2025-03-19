Dockerized Streamlit Development Environment
📌 Overview
This project sets up a Dockerized development environment for Streamlit, a powerful framework for building and deploying interactive web applications in Python. Using Docker, you can develop, test, and run your Streamlit applications in a consistent and isolated environment.

📁 Folder Structure
bash
Copy code
Dockerized-Streamlit-Development/
│── .streamlit/                  # Streamlit configuration folder
│   └── config.toml              # Configuration file for Streamlit UI settings
│── src/                         # Source code directory
│   └── main.py                  # Main Streamlit application file
│── Images/                      # Folder for storing images/screenshots
│── Dockerfile                   # Docker configuration file
│── requirements.txt              # Python dependencies
│── README.md                     # Documentation file
🛠️ Prerequisites
Before you begin, ensure you have:

Docker installed → Download Docker
Git installed → Download Git
🚀 Setup & Installation
✅ Step 1: Clone the Repository
Run the following command to clone this repository:

bash
Copy code
git clone https://github.com/ritu-pixel/DockNest.git
cd DockNest/Dockerized-Streamlit-Development
✅ Step 2: Build the Docker Image
To create a Docker image for your Streamlit application, run:

bash
Copy code
docker build -t streamlit-app .
✅ Step 3: Run the Streamlit App
Once the image is built, start a container using:

bash
Copy code
docker run -p 8501:8501 streamlit-app
Now, open http://localhost:8501/ in your browser to access the Streamlit app.

📝 Configuration
Inside the .streamlit/config.toml file, you can define custom settings for Streamlit, such as:

toml
Copy code
[server]
headless = true
enableCORS = false
port = 8501
🛑 Stopping & Removing Containers
To stop the running container, press CTRL + C.
To remove all stopped containers:

bash
Copy code
docker ps -a                # List all containers  
docker rm <container_id>     # Remove a specific container  
docker rmi streamlit-app     # Remove the Docker image  
📷 Screenshots
You can store screenshots of the running application inside the Images/ folder.

📤 Push to GitHub
To push your changes, including the Images/ folder, use:

bash
Copy code
git add .
git commit -m "Added Images folder and updated project"
git push origin main
🎯 Conclusion
This setup provides a fully containerized environment for Streamlit development, ensuring consistency and ease of deployment. 🚀

Let me know if you need any modifications! 😊
