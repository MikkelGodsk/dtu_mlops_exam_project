# Import a base image so we don't have to start from scratch
FROM python:3.12-rc-bullseye

# Run a bunch of linux commands
RUN apt update && \         
    apt install --no-install-recommends -y build essential gcc & \
    apt clean & rm -rf /var/lib/apt/lists/*

# Copy the essential files from our folder to docker container.
COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY src/ src/
COPY data/ data/

# Set working directory as / and install dependencies
WORKDIR /
RUN pip install -r requirements.txt --no-cache-dir

# Set entry point, i.e. which file we run with which argument when running the docker container.
# The -u flag makes it print to console rather than the docker log file.
ENTRYPOINT ["python", "-u", "src/models/predict_model.py"]