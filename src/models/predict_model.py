import argparse
import torch
from src.models.model import Model
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/translate/{input}")
def translate(
    input: str = "Hello world",
    checkpoint: str | None = None,  # "models/epoch=1-step=3750.ckpt"
):
    DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
    strict = True if torch.cuda.is_available() else False

    if checkpoint is None:
        model = Model()
    else:
        model = Model.load_from_checkpoint(
            checkpoint_path=checkpoint, map_location=DEVICE, strict=strict,
        )

    return {'en': input, 'de translation': model(input)[0]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--checkpoint", default=None, type=Union[str, None], help="Path to checkpoint"
    )  # "models/epoch=1-step=3750.ckpt"
    parser.add_argument("--input", type=str, help="English string to be translated")
    args = parser.parse_args()
    input = args.input

    print(translate(args.input, args.checkpoint))
