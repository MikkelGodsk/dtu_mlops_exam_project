import argparse
from typing import Optional

import pytorch_lightning as pl
import torch
import wandb
from datasets import Dataset
from pytorch_lightning.callbacks import ModelCheckpoint
from src.models.model import Model
from torch.utils.data import DataLoader


def train(config: str, wandbkey: Optional[str] = None, debug_mode: bool = False):
    if not (wandbkey is None):
        wandb.login(key=wandbkey)  # input API key for wandb for docker
        project = "mlops_exam_project"
        entity = "chrillebon"
        anonymous = None
        mode = "online"
    else:
        project = None
        entity = None
        anonymous = "must"
        mode = "disabled"

    wandb.init(
        project=project,
        entity=entity,
        anonymous=anonymous,
        config=config,
        mode=mode,
    )

    lr = wandb.config.lr
    epochs = wandb.config.epochs
    batch_size = wandb.config.batch_size
    seed = wandb.config.batch_size

    if seed is not None:
        torch.manual_seed(seed)

    model = Model(lr=lr, batch_size=batch_size)

    if not (wandbkey is None):
        wandb.watch(model, log_freq=100)
        logger = pl.loggers.WandbLogger(
            project="mlops_exam_project", entity="chrillebon"
        )
    else:
        logger = True

    trainset = Dataset.load_from_disk("data/processed/train")
    testset = Dataset.load_from_disk("data/processed/validation")
    trainloader = DataLoader(trainset, batch_size=batch_size, num_workers=8)
    testloader = DataLoader(testset, batch_size=batch_size, num_workers=8)

    checkpoint_callback = ModelCheckpoint(dirpath="/models/checkpoints")

    if torch.cuda.is_available():
        accelerator = "gpu"
        devices = [6]
    else:
        accelerator = None
        devices = None

    if debug_mode:
        limit = 0.1
    else:
        limit = 1.0

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
        logger=logger,
    )

    trainer.fit(model=model, train_dataloaders=trainloader, val_dataloaders=testloader)

    torch.save(model.state_dict(), "/models/epoch=final.pt")
    print("Done!")

    # Mangler at uploade de gemte filer til drive. Gøres i docker


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        default="src/models/config/default_params.yaml",
        type=str,
        help="configuration file with hyperparameters",
    )
    parser.add_argument("--wandbkey", default=None, type=str, help="W&B API key")
    parser.add_argument(
        "--debug_mode", action="store_true", help="Run only 10 percent of data"
    )

    args = parser.parse_args()

    train(args.config, args.wandbkey, args.debug_mode)
