# Use an official lightweight Python image.
FROM python:3.9-slim AS streamlit-build

# Set the working directory inside the container
WORKDIR /ARCD

# Copy the local code to the container
COPY ./ /ARCD/

# Install all required packages in one layer to keep the image clean and efficient
RUN pip install --no-cache-dir streamlit st-pages google-generativeai vertexai \
    google-cloud-bigquery python-dotenv google-ai-generativelanguage pillow db-dtypes

# Expose port 8501 for Streamlit applications
EXPOSE 8501

# The main command to run when the container starts.
CMD ["streamlit", "run", "main.py", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
