import argparse
import torch
from src.models.model import Model
from typing import Union, Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/translate/{input}")
def translate(
    input: str = "Hello world",
    checkpoint: Optional[str] = None #"models/epoch=0-step=1875-v1.ckpt"
):
    DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
    strict = True if torch.cuda.is_available() else False

    if checkpoint is None:
        model = Model()
    else:
        model = Model.load_from_checkpoint(
            checkpoint_path=checkpoint, map_location=DEVICE,
        )

    return {'en': input, 'de translation': model(input)[0]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="English string to be translated")
    parser.add_argument(
        "--checkpoint", default=None, type=str, help="Path to checkpoint"
    )
    args = parser.parse_args()
    input = args.input

    print(translate(args.input, args.checkpoint))
