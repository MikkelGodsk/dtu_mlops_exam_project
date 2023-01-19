# Import a base image so we don't have to start from scratch
#FROM python:3.10-slim
FROM huggingface/transformers-pytorch-cpu

# Run a bunch of linux commands
RUN apt update && \         
    apt install --no-install-recommends -y build essential gcc & \
    apt clean & rm -rf /var/lib/apt/lists/*

# Copy the essential files from our folder to docker container.
COPY src/ src/
COPY requirements_predict.txt requirements_predict.txt
COPY setup.py setup.py

#RUN export LC_ALL=C.UTF-8
#RUN export LANG=C.UTF-8

RUN pip install -r requirements_predict.txt --no-cache-dir

RUN dvc init --no-scm
RUN dvc remote add -d gcloud_storage gs://mlops-dataset-small
RUN dvc pull

# Set working directory as / and install dependencies
EXPOSE $PORT
WORKDIR /

RUN mkdir app

# Set entry point, i.e. which file we run with which argument when running the docker container.
# The -u flag makes it print to console rather than the docker log file.
#ENTRYPOINT ["python", "-u", "src/models/predict_model.py"]
CMD exec uvicorn src.models.predict_model:app --host 0.0.0.0 --workers 1 --port $PORT
#ENTRYPOINT ["uvicorn", "src.models.predict_model:app", "--host", "0.0.0.0", "--workers", "1", "--port", $PORT]
#  