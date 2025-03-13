# Use Python as base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY stream.py .

# Install dependencies
RUN pip install streamlit psycopg2

# Run Streamlit app
CMD ["streamlit", "run", "stream.py", "--server.port=8501", "--server.address=0.0.0.0"]
