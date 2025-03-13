import streamlit as st
import psycopg2

# Database Connection
conn = psycopg2.connect(
    dbname="testdb",
    user="ritu",
    password="secret",
    host="my_postgres_container",
    port="5432"
)
cur = conn.cursor()

# Fetch Data
cur.execute("SELECT * FROM passengers;")
rows = cur.fetchall()

# Streamlit UI
st.title("🚆 Passenger Database")
st.table(rows)
