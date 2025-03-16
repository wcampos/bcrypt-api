FROM amazonlinux:2023

# Install dependencies and create app user
RUN yum -y update && \
    yum -y install python3-pip python3-devel gcc libffi-devel openssl-devel shadow-utils curl-minimal && \
    yum clean all && \
    useradd -m -r appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

WORKDIR /app

# Install Python packages
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && \
    rm -f requirements.txt

# Copy application code
COPY app app/
RUN chown -R appuser:appuser /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=5000 \
    FLASK_DEBUG=false \
    BCRYPT_ROUNDS=12

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 5000

# Use gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.api:app"]

