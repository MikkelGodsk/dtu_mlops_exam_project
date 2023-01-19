import argparse

import pytorch_lightning as pl
import torch
from datasets import Dataset
from torch.utils.data import DataLoader

import wandb
from src.models.model import Model


def train(config=None):
    with wandb.init(config=config):
        # If called by wandb.agent, as below,
        # this config will be set by Sweep Controller
        config = wandb.config

        lr = wandb.config.lr
        epochs = wandb.config.epochs
        batch_size = wandb.config.batch_size

        logger = pl.loggers.WandbLogger(
            project="mlops_exam_project", entity="chrillebon"
        )

        model = Model(lr=lr, batch_size=batch_size)

        trainset = Dataset.load_from_disk("data/processed/train")
        testset = Dataset.load_from_disk("data/processed/validation")
        trainloader = DataLoader(trainset, batch_size=batch_size, num_workers=8)
        testloader = DataLoader(testset, batch_size=batch_size, num_workers=8)

        if torch.cuda.is_available():
            accelerator = "gpu"
            devices = [7]
        else:
            accelerator = None
            devices = None

        trainer = pl.Trainer(
            max_epochs=epochs,
            default_root_dir="",
            accelerator=accelerator,
            devices=devices,
            strategy="ddp",
            logger=logger,
        )

        trainer.fit(
            model=model, train_dataloaders=trainloader, val_dataloaders=testloader
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--wandbkey",
        default="908b9732cead54d65140e987cb83ad9f78ba79bf",
        type=str,
        help="W&B API key",
    )
    args = parser.parse_args()
    wandbkey = args.wandbkey

    wandb.login(key=wandbkey)  # input API key for wandb for docker
    project = "mlops_exam_project"
    entity = "chrillebon"
    anonymous = None
    mode = "online"

    sweep_config = {
        "method": "random",
        "name": "sweep",
        "metric": {"goal": "minimize", "name": "val loss"},
        "parameters": {
            "batch_size": {"values": [16]},
            "epochs": {"values": [2]},
            "lr": {"max": 0.001, "min": 0.000001},
        },
    }
    sweep_id = wandb.sweep(
        sweep=sweep_config, project="mlops_exam_project", entity="chrillebon"
    )
    wandb.agent(sweep_id, train, count=5)
