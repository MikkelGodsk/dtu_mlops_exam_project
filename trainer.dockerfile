# Import a base image so we don't have to start from scratch
FROM huggingface/transformers-pytorch-cpu
# python:3.10-slim

# Run a bunch of linux commands
RUN apt update && \         
    apt install --no-install-recommends -y build essential gcc & \
    apt clean & rm -rf /var/lib/apt/lists/*

WORKDIR /
# Copy the essential files from our folder to docker container.
COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY src/ src/
COPY data/ data/

# Set working directory as / and install dependencies
RUN pip install -r requirements.txt --no-cache-dir
RUN mkdir models/
RUN mkdir models/checkpoints
COPY models/models--t5-small/ models/models--t5-small/

# Set entry point, i.e. which file we run with which argument when running the docker container.
# The -u flag makes it print to console rather than the docker log file.
# export to get wandb.init() to work
ENTRYPOINT export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 && exec python3 -u src/models/train_model.py --debug_mode