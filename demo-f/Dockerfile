# Set base image (host OS)
FROM python:3.9-slim-bullseye

RUN apt-get -y update && \
   apt-get install -y --no-install-recommends build-essential  \
   curl wget nginx ca-certificates npm \
   && npm install pm2 -g \
   && pip install --upgrade pip setuptools \
   && rm -rf /var/lib/apt/lists/*

# By default, listen on port 5000
EXPOSE 8000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Copy the content of the local src directory to the working directory
COPY main.py .
COPY server/ ./server
COPY dist/ ./dist
COPY __init__.py .

RUN pip install --upgrade pip && \
     pip install --no-cache-dir -r requirements.txt

RUN pip install -U scikit-learn

# Specify the command to run on container start
CMD [ "python", "./main.py" ]