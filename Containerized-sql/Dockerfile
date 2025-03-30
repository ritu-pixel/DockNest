# 🏗 Use the official MySQL image
FROM mysql:latest

# 📂 Copy initialization script to the container
COPY database_students.sql /docker-entrypoint-initdb.d/

# 🔥 Expose MySQL port
EXPOSE 3306
