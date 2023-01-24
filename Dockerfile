FROM python:3.7-slim

# Set environment variables
ENV PYTHONUNBUFFERED TRUE

COPY requirements.txt /purrfectCreations/requirements.txt

WORKDIR /purrfectCreations

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /purrfectCreations/
CMD ["/purrfectCreations/entrypoint.sh"]
