
# 🚀 Streamlit Spiral Visualization App with Docker

## Access the application at
https://docknest-ypsrcfmkvjokuc2dnmpcm8.streamlit.app/
<img width="959" alt="image" src="https://github.com/user-attachments/assets/fe85095f-5468-4f6b-bfb9-ca26aec48a66" />
![image](https://github.com/user-attachments/assets/314de6a7-3ec1-4fdc-bbc5-c05d458743b8)



Welcome to the **Streamlit Spiral Visualization App!** This project is a simple and interactive Python application built with **Streamlit** to visualize a **dynamic spiral.** You can customize the spiral’s characteristics using sliders and see real-time changes.

The app is **Dockerized** for easy deployment and environment consistency.

---

## 🌟 Features

✅ **Interactive Controls** – Adjust the number of points and turns in the spiral.  
✅ **Real-time Visualization** – Watch the spiral dynamically change.  
✅ **Dockerized Application** – Run seamlessly across different environments.  
✅ **Lightweight & Easy to Use** – No extra dependencies, just Python & Streamlit.  

---

## 🚀 Technologies Used

- **Python 3** – Core programming language
- **Streamlit** – Web framework for interactive UI
- **Altair** – Data visualization library for the spiral graph
- **Pandas** – Data manipulation and handling
- **Docker** – Containerization for easy deployment

---

## ⚙ Prerequisites

Before running the application, make sure you have:

- **Docker** installed ([Install Docker](https://docs.docker.com/get-docker/))
- **Git** installed ([Install Git](https://git-scm.com/downloads))

---

## 🛠 Getting Started

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/ritu-pixel/DockNest.git
cd DockNest/streamlit-app
```

### **Step 2: Install Dependencies (Optional for Local Execution)**
If you’re running locally without Docker, install the required packages:
```bash
pip install -r requirements.txt
```

### **Step 3: Build the Docker Image**
```bash
docker build -t streamlit-app .
```
After building, verify the image with:
```bash
docker images
```

### **Step 4: Run the Docker Container**
```bash
docker run -p 8501:8501 streamlit-app
```

### **Step 5: Access the Application**
Once the container is running, open your browser and visit:
**[http://localhost:8501](http://localhost:8501)**

---

## 🌀 How the App Works

- **Sliders for Customization:**
  - **Number of Points in Spiral** – Controls the number of points that form the spiral.
  - **Number of Turns in Spiral** – Adjusts how many full turns the spiral makes.
- **Real-Time Visualization:**
  - The spiral updates instantly when you move the sliders.
- **Under the Hood:**
  - The app generates spiral points using **polar coordinates**.
  - The x and y positions are calculated using **cosine and sine functions**.
  - **Altair charts** visualize the spiral in Streamlit.

---

## 📜 Code Overview

### **Python Code (`app.py`)**
```python
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from collections import namedtuple

# Define a namedtuple for storing spiral points
Point = namedtuple('Point', ['x', 'y'])

# Function to generate spiral data
def generate_spiral(num_points, num_turns):
    data = []
    for i in range(num_points):
        angle = 2 * np.pi * num_turns * (i / num_points)
        radius = i / num_points
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        data.append(Point(x, y))
    return data

# Streamlit App Layout
st.title("🌀 Interactive Spiral Visualization")

# User input sliders
num_points = st.slider('Number of Points in Spiral', min_value=50, max_value=1000, value=500)
num_turns = st.slider('Number of Turns in Spiral', min_value=1, max_value=10, value=5)

# Generate and visualize spiral
spiral_data = generate_spiral(num_points, num_turns)
spiral_df = pd.DataFrame(spiral_data, columns=['x', 'y'])

# Create and display Altair chart
chart = alt.Chart(spiral_df).mark_circle(size=3).encode(x='x', y='y').properties(width=600, height=600)
st.altair_chart(chart, use_container_width=True)
```

---

## 🐳 Dockerfile

```dockerfile
# Use official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🛠 Troubleshooting

🛑 **Issue: "Streamlit command not found" inside Docker?**  
✔ Fix: Make sure dependencies are installed inside the container by rebuilding it:  
```bash
docker build --no-cache -t streamlit-app .
```

🛑 **Issue: Port 8501 is already in use?**  
✔ Fix: Run on a different port:  
```bash
docker run -p 8502:8501 streamlit-app
```
Then, visit **http://localhost:8502**

---

## 🤝 Contributing

🚀 Want to contribute? Here’s how:
1. **Fork** the repository
2. **Create a branch** (`git checkout -b feature-branch`)
3. **Commit your changes** (`git commit -m "Added feature XYZ"`)
4. **Push to the branch** (`git push origin feature-branch`)
5. **Submit a Pull Request**

---

## 📜 License
This project is open-source.**.

💡 **Happy Coding! 🚀🎉**

## Deploying it on Render
![Screenshot 2025-03-25 114157](https://github.com/user-attachments/assets/9ba561a9-c8f4-4acf-902b-a575cfaa6aac)
![Screenshot 2025-03-25 114209](https://github.com/user-attachments/assets/5198de96-0d52-4ad4-9283-751321d5fc33)
![Screenshot 2025-03-25 114222](https://github.com/user-attachments/assets/0c57de24-5602-4c30-9cea-aa47c0244ac2)
You can view your app at
https://docknest-1.onrender.com/
![image](https://github.com/user-attachments/assets/28593609-ddb7-4fd3-8af7-6a7e4620e0ec)




