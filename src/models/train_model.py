import pytorch_lightning as pl
import wandb
from torch.utils.data import DataLoader

from datasets import Dataset
from src.models import _DATA_PATH
from src.models.model import Model

if __name__ == "__main__":

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
    testset = Dataset.load_from_disk("data/processed/test")
    trainloader = DataLoader(trainset, batch_size=batch_size, num_workers=8)
    testloader = DataLoader(testset, batch_size=batch_size, num_workers=8)

    trainer = pl.Trainer(
        max_epochs=epochs, default_root_dir=""
    )  # , logger=pl.loggers.WandbLogger(project="mnist"), log_every_n_steps = 1

    trainer.fit(model=model, train_dataloaders=trainloader, val_dataloaders=testloader)

    print("Done!")
