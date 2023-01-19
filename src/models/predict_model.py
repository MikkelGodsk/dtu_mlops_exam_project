import argparse
import os
from typing import Optional

import torch
from fastapi import FastAPI
from google.cloud import storage
from src.models.model import Model

app = FastAPI()


def newest_blob(bucket):
    blobs = list(bucket.list_blobs())
    return sorted(
        blobs,
        key=lambda blob: str(blob.time_created),
        reverse=True
    )[0]


@app.get("/translate/{input}")
def translate(
    input: str = "Hello world",
    checkpoint: Optional[str] = None,  # "models/epoch=0-step=1875-v1.ckpt"
):
    """
        If a new model is uploaded to the bucket, the function downloads it when invoked.
    """
    DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
    # strict = True if torch.cuda.is_available() else False

    client = storage.Client()
    bucket = client.get_bucket("model-checkpoints-mlops-exam")
    if checkpoint is None:
        blob = newest_blob(bucket)
    else:
        blob = bucket.get_blob(checkpoint)
    filename = os.path.join('models', blob.name)
    if not os.path.isfile(filename):
        if not os.path.isdir('models'):
            os.mkdir('models')
        blob.download_to_filename(filename=filename)
    state_dict = torch.load(filename)  # pickle.loads(blob.download_as_string())
    model = Model().to(DEVICE)  # Model.load_from_checkpoint(
    # checkpoint_path=checkpoint, map_location=DEVICE,
    # )  # Model()
    model.load_state_dict(state_dict)

    return {"en": input, "de translation": model(input)[0]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="English string to be translated")
    parser.add_argument(
        "--checkpoint", default=None, type=str, help="Path to checkpoint"
    )
    args = parser.parse_args()
    input = args.input

    print(translate(args.input, args.checkpoint))
