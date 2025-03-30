FROM python:3.9-slim
WORKDIR /app
COPY api_gateway.py /app
RUN pip install flask requests
CMD ["python", "api_gateway.py"]
