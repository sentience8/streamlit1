# Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Install Streamlit (or other dependencies)
RUN pip install streamlit

# Copy the rest of your app code
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]