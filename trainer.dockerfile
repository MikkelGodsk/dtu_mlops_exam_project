# Import a base image so we don't have to start from scratch
FROM python:3.10-slim

# Run a bunch of linux commands
RUN apt update && \         
    apt install --no-install-recommends -y build essential gcc & \
    apt clean & rm -rf /var/lib/apt/lists/*

# Copy the essential files from our folder to docker container.
COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY src/ src/
COPY data/ data/
ARG KEY_FILE
COPY $KEY_FILE $KEY_FILE

# get wandbkey
RUN apt-get -y update; apt-get -y install curl
RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-413.0.0-linux-x86_64.tar.gz
RUN tar -xf google-cloud-cli-413.0.0-linux-x86_64.tar.gz
RUN ./google-cloud-sdk/install.sh
RUN ./google-cloud-sdk/bin/gcloud auth activate-service-account 
# missing secret arguments in line above...^^^^
ARG WANDBKEY=$(exec ./google-cloud-sdk/bin/gcloud secrets versions access 1 --secret="wandbkey")

WORKDIR /

# Set working directory as / and install dependencies
RUN pip install -r requirements.txt --no-cache-dir
RUN mkdir models/
RUN mkdir models/checkpoints
COPY models/models--t5-small/ models/models--t5-small/

# Set entry point, i.e. which file we run with which argument when running the docker container.
# The -u flag makes it print to console rather than the docker log file.
ENTRYPOINT exec python -u src/models/train_model.py --wandbkey=$WANDBKEY --debug_mode