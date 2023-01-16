import argparse

from src.models.model import Model

if __name__ == "__main__":
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--input', type=str, help = 'English string to be translated')
    #args = parser.parse_args()
    #input = args.input

    model = Model.load_from_checkpoint(
        checkpoint_path="models/epoch=1-step=3750.ckpt", 
        )
    input = "hello world"
    results = model(input)
    print(results)