import pytorch_lightning as pl
import torch
from datasets import Dataset
from pytorch_lightning.callbacks import ModelCheckpoint
from src.models.model import Model
from torch.utils.data import DataLoader

if __name__ == "__main__":

    # wandb.init(
    #    project="mlops_exam_project",
    #    entity="chrillebon",
    #    config="src/models/config/default_params.yaml",
    # )

    model = Model.load_from_checkpoint(checkpoint_path="models/epoch=1-step=3750.ckpt",)

    testset = Dataset.load_from_disk("data/processed/validation")
    testloader = DataLoader(testset, num_workers=8)

    epochs = 1

    checkpoint_callback = ModelCheckpoint(dirpath="models/")

    if torch.cuda.is_available():
        trainer = pl.Trainer(
            max_epochs=epochs,
            default_root_dir="",
            callbacks=[checkpoint_callback],
            accelerator="gpu",
            devices=[6],
            strategy="ddp",
        )
    else:
        trainer = pl.Trainer(
            max_epochs=epochs, default_root_dir="", callbacks=[checkpoint_callback]
        )

    results = trainer.test(model=model, dataloaders=testloader, verbose=True)

    print(results)
