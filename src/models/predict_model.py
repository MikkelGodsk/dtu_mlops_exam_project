import argparse
import torch

from src.models.model import Model

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--checkpoint",
        type=str,
        default="models/epoch=1-step=3750.ckpt",
        help="Path to checkpoint",
    )
    parser.add_argument("--input", type=str, help="English string to be translated")
    args = parser.parse_args()
    input = args.input

    if torch.cuda.is_available():
        model = Model.load_from_checkpoint(checkpoint_path=args.checkpoint,)
    else:
        model = Model.load_from_checkpoint(
            checkpoint_path=args.checkpoint, map_location="cpu", strict=False
        )

    results = model(input)
    print(results)
