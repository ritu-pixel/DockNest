# 🚀 PostgreSQL Docker Setup

## 📌 Overview
This project sets up a **PostgreSQL database** inside a Docker container, allowing for a fully containerized database environment. It includes **persistent storage**, **networking**, and **basic SQL setup**.

---

## 📁 Project Structure
```
sql-postgresql/
│── Dockerfile          # Defines the PostgreSQL container setup
│── init.sql            # SQL script to initialize the database and tables
│── db-data/            # Persistent volume for PostgreSQL data
└── README.md           # Documentation
```

---

## 🛠 Prerequisites
Ensure you have the following installed:
- **Docker** ([Download Here](https://www.docker.com/get-started))
- **Git** ([Download Here](https://git-scm.com/downloads))

---

## 🏗 Setting Up PostgreSQL in Docker

### **1️⃣ Create a Custom Docker Network**
To enable communication between containers, create a dedicated network:
```powershell
docker network create my_postgres_network
```

### **2️⃣ Run the PostgreSQL Container**
Execute the following command to start a PostgreSQL container:
```powershell
docker run --name my_postgres_container --network my_postgres_network `
    -e POSTGRES_USER=ritu -e POSTGRES_PASSWORD=secret `
    -e POSTGRES_DB=testdb -p 5432:5432 `
    -v ${PWD}/db-data:/var/lib/postgresql/data -d postgres
```

📌 **Explanation:**
- `--name my_postgres_container` → Assigns a name to the container.
- `--network my_postgres_network` → Connects the container to the custom network.
- `-e POSTGRES_USER=ritu` → Sets the PostgreSQL username.
- `-e POSTGRES_PASSWORD=secret` → Sets the PostgreSQL password.
- `-e POSTGRES_DB=testdb` → Creates a database named `testdb`.
- `-p 5432:5432` → Maps PostgreSQL’s default port to the host machine.
- `-v ${PWD}/db-data:/var/lib/postgresql/data` → Persists database data.
- `-d postgres` → Runs the container in detached mode.

### **3️⃣ Verify Running Container**
Check if the PostgreSQL container is running:
```powershell
docker ps
```

---

## 📊 Creating and Populating the Database

### **4️⃣ Access PostgreSQL CLI**
To interact with PostgreSQL inside the container:
```powershell
docker exec -it my_postgres_container psql -U ritu -d testdb
```

### **5️⃣ Create a Sample Table**
Run the following SQL command inside the PostgreSQL CLI:
```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
```

### **6️⃣ Insert Sample Data**
```sql
INSERT INTO students (name, age) VALUES
('Alice', 22),
('Bob', 24),
('Charlie', 23);
```

### **7️⃣ Verify Data**
```sql
SELECT * FROM students;
```

---

## 🐳 Dockerizing PostgreSQL with a Custom `Dockerfile`

### **8️⃣ Create a Dockerfile**
Inside `sql-postgresql/`, create a `Dockerfile`:
```Dockerfile
FROM postgres
ENV POSTGRES_USER=ritu
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_DB=testdb
COPY init.sql /docker-entrypoint-initdb.d/
```

### **9️⃣ Create an `init.sql` File**
Inside `sql-postgresql/`, create `init.sql`:
```sql
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
INSERT INTO students (name, age) VALUES ('Default User', 20);
```

### **🔟 Build and Run the Custom PostgreSQL Image**
```powershell
docker build -t custom-postgres .
docker run --name my_postgres_container --network my_postgres_network -p 5432:5432 -d custom-postgres
```

---

## 🔗 Connecting to PostgreSQL from an Application
To connect from a **Python** or **Node.js** app, use:
```
Database: testdb
User: ritu
Password: secret
Host: my_postgres_container
Port: 5432
```

Example connection string for **Python (psycopg2)**:
```python
import psycopg2
conn = psycopg2.connect(
    dbname="testdb",
    user="ritu",
    password="secret",
    host="my_postgres_container",
    port="5432"
)
print("Connected successfully!")
```

---

## 🚀 Deploying the Setup to GitHub
### **Push to `DockNest` Repository**
```powershell
git add sql-postgresql
git commit -m "Added PostgreSQL Docker setup"
git push origin main
```

---

## 🎯 Summary
✅ **PostgreSQL container stores student data.**  
✅ **Database and tables are automatically created.**  
✅ **Custom Dockerfile and SQL script initialize the database.**  
✅ **Data persists using a volume.**  
✅ **Easily deployable in any environment using Docker.**  

🚀 **Now your PostgreSQL setup is fully containerized and ready for development!** 🎉

