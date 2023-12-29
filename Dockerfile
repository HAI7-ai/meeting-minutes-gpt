# -------------- BUILD STAGE ------------------
# Pull base image of python 3.11 slim version
FROM python:3.11-slim as base
# WorkDir 
WORKDIR /app
# Copy requirements.txt file
COPY requirements.txt .
# Install dependencies from requirements
RUN python -m venv .venv && .venv/bin/pip install --no-cache-dir -U pip setuptools
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt && find /app/.venv \( -type d -a -name test -o -name tests \) -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rf '{}' \+


# -------------- RUNNER STAGE -------------------
# Pull base image of python 3.11 slim version
FROM python:3.11-slim
# WorkDir 
WORKDIR /app
# Copy dependcies from base image
COPY --from=base /app /app
ENV PATH="$PATH:/app/.venv/bin"
# Copy App Files to app directory
COPY .streamlit/* /app/.streamlit/
COPY config /app/config/
COPY frontend/ /app/frontend/
COPY assets/ /app/assets/
COPY src/* /app/src/
# Expose default Streamlit UI port
EXPOSE 8501
# Run streamlit
CMD ["streamlit", "run", "frontend/main.py"]