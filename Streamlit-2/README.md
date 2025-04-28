Streamlit Interactive App.
# Streamlit-2: Interactive Data Explorer 🚀

Welcome to **Streamlit-2**, a simple yet powerful Streamlit application to **upload**, **explore**, and **visualize** your data!

![Streamlit Demo](https://raw.githubusercontent.com/ritu-pixel/Streamlit-2/main/your-screenshot-file.png)

## 📂 Features
- Upload your own CSV file (up to 200MB)
- Instantly preview the dataset
- Navigate between:
  - **Home**
  - **Data Explorer**
  - **Visualization**
- Clean dark-themed interface
- Easy to use and extend!

---

## 🛠️ Project Structure
```bash
├── Dockerfile
├── config.toml
├── main.py
├── requirements.txt
└── README.md
```
![image](https://github.com/user-attachments/assets/b46295b9-62be-4822-82ce-821bcaf7d293)

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/ritu-pixel/Streamlit-2.git
cd Streamlit-2
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
![image](https://github.com/user-attachments/assets/a4429c5b-38a2-443e-b701-e707849eaa11)

### 3. Run the Streamlit app
```bash
streamlit run main.py
```
![image](https://github.com/user-attachments/assets/318e6a1f-d714-4797-8e52-7285f85e8717)

---

## 🐳 Run with Docker

1. **Build the Docker image**
```bash
docker build -t streamlit2-app .
```

2. **Run the Docker container**
```bash
docker run -p 8501:8501 streamlit2-app
```
![Screenshot 2025-01-29 115120](https://github.com/user-attachments/assets/3c705bb4-49f5-4db6-b2e4-c7519ef21016)

Then, open your browser and visit:  
👉 **http://localhost:8501**
![image](https://github.com/user-attachments/assets/00dbdb36-9583-4966-bf12-ad7ae26e92ed)

---

## 📦 Requirements
- Python 3.8+
- Streamlit
- pandas

*(All listed in `requirements.txt`)*

---

## 📝 Notes
- File upload is limited to CSV format only.
- Make sure your CSV file is clean and properly formatted.
- You can extend this app easily to include charts, data cleaning, or machine learning!

---

## ✨ Acknowledgements
Built with ❤️ using [Streamlit](https://streamlit.io/).

---

## 🔗 Connect
- GitHub: [ritu-pixel](https://github.com/ritu-pixel)


![image](https://github.com/user-attachments/assets/6412aa24-a90d-4a73-bff2-8d625df79694)
