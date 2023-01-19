# Import a base image so we don't have to start from scratch
FROM python:3.10-slim

# Run a bunch of linux commands
RUN apt update && \         
    apt install --no-install-recommends -y build essential gcc & \
    apt clean & rm -rf /var/lib/apt/lists/*

# Copy the essential files from our folder to docker container.
COPY src/ src/
COPY data/ data/
COPY models/ models/

COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY data.dvc data.dvc

RUN pip install -r requirements.txt --no-cache-dir
RUN pip install pydantic
RUN pip install uvicorn

RUN dvc init --no-scm
RUN dvc pull


# Set working directory as / and install dependencies
WORKDIR /

RUN mkdir app

# Set entry point, i.e. which file we run with which argument when running the docker container.
# The -u flag makes it print to console rather than the docker log file.
#ENTRYPOINT ["python", "-u", "src/models/predict_model.py"]
CMD exec uvicorn src.models.predict_model:app --host 0.0.0.0 --workers 1 --port $PORT
#ENTRYPOINT ["uvicorn", "src.models.predict_model:app", "--host", "0.0.0.0", "--workers", "1", "--port", $PORT]
#  