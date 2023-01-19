import argparse
import pytorch_lightning as pl
import wandb
from datasets import Dataset
from torch.utils.data import DataLoader
import torch
from pytorch_lightning.callbacks import ModelCheckpoint
import os

from src.models.model import Model

def train(wandbkey, debug_mode=False):
    print(wandbkey)
    wandb.login(key=wandbkey) # input API key for wandb for docker
    wandb.init(
        project="mlops_exam_project",
        entity="chrillebon",
        config="src/models/config/default_params.yaml",
    )

    lr = wandb.config.lr
    epochs = wandb.config.epochs
    batch_size = wandb.config.batch_size

    model = Model(lr=lr, batch_size=batch_size)
    wandb.watch(model, log_freq=100)

    trainset = Dataset.load_from_disk("data/processed/train")
    testset = Dataset.load_from_disk("data/processed/validation")
    trainloader = DataLoader(trainset, batch_size=batch_size, num_workers=8)
    testloader = DataLoader(testset, batch_size=batch_size, num_workers=8)

    checkpoint_callback = ModelCheckpoint(dirpath=os.path.join("models","checkpoints"))

    if torch.cuda.is_available():
        accelerator = "gpu"
        devices = [6]
    else:
        accelerator = None
        devices = None

    if debug_mode:
        limit = 0.1
    else:
        limit = 1

    trainer = pl.Trainer(
        max_epochs=epochs,
        default_root_dir="",
        callbacks=[checkpoint_callback],
        accelerator=accelerator,
        devices=devices,
        strategy="ddp",
        limit_train_batches=limit,
        limit_val_batches=limit,
        profiler="simple",
        logger=pl.loggers.WandbLogger(project="mlops_exam_project",entity="chrillebon")
    )

    trainer.fit(model=model, train_dataloaders=trainloader, val_dataloaders=testloader)

    torch.save(model.state_dict(), os.path.join("models","checkpoints","epoch=final.ckpt"))
    print("Done!")

    # Mangler at uploade de gemte filer til drive.


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--wandbkey", type=str, help="W&B API key"
    )
    parser.add_argument(
        "--debug_mode", action='store_true', help="Run only 10 percent of data"
    )

    args = parser.parse_args()
    
    train(args.wandbkey, args.debug_mode)