# 🐬 Containerized MySQL: Agile & Efficient 🚀

This project sets up a **MySQL database inside a Docker container**, ensuring an efficient and reusable development environment. The database is initialized with a predefined schema and sample data, making it easy to start development or testing.

## 📌 Prerequisites
Before proceeding, ensure you have the following installed:

✅ **Docker** - [Download & Install](https://docs.docker.com/get-docker/)
✅ **Basic SQL Knowledge**
✅ **Terminal or Command Prompt Access**

---

## 📂 Project Directory Structure

```
Containerized-sql/
│── Dockerfile
│── database_students.sql
│── README.md
```

---

## 🏗 Step 1: Create a Dockerfile

Create a `Dockerfile` in the `Containerized-sql` directory with the following content:

```dockerfile
# 🏗 Use the official MySQL image
FROM mysql:latest

# 📂 Copy initialization script to the container
COPY database_students.sql /docker-entrypoint-initdb.d/

# 🔥 Expose MySQL port
EXPOSE 3306
```

This Dockerfile:
- Uses the latest MySQL image.
- Copies the SQL initialization script into the container.
- Exposes MySQL's default port (3306).

---

## 📜 Step 2: Create an SQL Initialization Script

Create a file named `database_students.sql` with the following content:

```sql
CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

INSERT INTO students (name, age) VALUES ('Alice', 22), ('Bob', 24);
```

This script:
- Creates a `student_db` database.
- Defines a `students` table with sample records.

---

## 🛠 Step 3: Build the Docker Image
Run the following command in the `Containerized-sql` directory:

```sh
docker build -t mysql-custom .
```

This command:
- Builds a custom Docker image named `mysql-custom`.

---

## 🚀 Step 4: Run MySQL Container
Start a MySQL container using:

```sh
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -d mysql-custom
```

🔍 **Explanation:**
- `--name mysql-container` → Assigns a name to the container.
- `-e MYSQL_ROOT_PASSWORD=root` → Sets MySQL root password.
- `-d` → Runs in detached mode.
- `mysql-custom` → Uses the custom image built earlier.

---

## 🔍 Step 5: Access the Running Container
To enter the container’s shell:

```sh
docker exec -it mysql-container bash
```

Once inside, connect to MySQL:

```sh
mysql -u root -p
```

🔑 Enter `root` as the password.

---

## 📊 Step 6: Verify Database & Tables
Once inside MySQL, run:

```sql
SHOW DATABASES;
USE student_db;
SHOW TABLES;
SELECT * FROM students;
```

This will confirm that the database and tables were successfully created.

---
![Screenshot 2025-03-13 140348](https://github.com/user-attachments/assets/62d5e801-0a4a-41d8-8333-454127145523)
![Screenshot 2025-03-13 140358](https://github.com/user-attachments/assets/7dc859d8-3a26-44b7-89dc-88fbbb33f5de)



## 🎯 Cleanup & Stopping the Container
To stop the container:

```sh
docker stop mysql-container
```

To remove the container:

```sh
docker rm mysql-container
```

To remove the image:

```sh
docker rmi mysql-custom
```

---

## 🎉 Conclusion
🎯 You have successfully containerized MySQL using Docker! This setup ensures:
- ✅ A consistent development database environment.
- ✅ Easy database resets using the initialization script.
- ✅ Simplified deployment & testing.

🚀 **Happy Coding!** 💻

