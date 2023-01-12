import pytorch_lightning as pl
import wandb
from torch.utils.data import DataLoader

from src.data.download_dataset import dataset
from src.models import _DATA_PATH
from src.models.model import Model

# run using "python src/models/train_model.py"
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
    trainloader = DataLoader(dataset["train"], batch_size=batch_size)
    testloader = DataLoader(dataset["validation"], batch_size=batch_size)

    trainer = pl.Trainer(
        max_epochs=epochs, default_root_dir=""
    )  # , logger=pl.loggers.WandbLogger(project="mnist"), log_every_n_steps = 1

    trainer.fit(model=model, train_dataloaders=trainloader, val_dataloaders=testloader)

    print("Done!")
