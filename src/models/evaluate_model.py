import pytorch_lightning as pl
import wandb
from torch.utils.data import DataLoader
from torchmetrics import BLEUScore

from datasets import Dataset
from src.models import _DATA_PATH
from src.models.model import Model

if _name_ == "_main_":

    #wandb.init(
    #    project="mlops_exam_project",
    #    entity="chrillebon",
    #    config="src/models/config/default_params.yaml",
    #)

    model = pl.load_from_checkpoint(
    checkpoint_path="/path/to/pytorch_checkpoint.ckpt", # to do...
    hparams_file="src/models/config/default_params.yaml",
    map_location=None,
)
    #wandb.watch(model, log_freq=100)

    testset = Dataset.load_from_disk("data/processed/validation")
    testloader = DataLoader(testset, num_workers=8)
    trainer = pl.Trainer()  # , logger=pl.loggers.WandbLogger(project="mnist"), log_every_n_steps = 1

    results = trainer.test(model=model, datamodule=testloader, verbose=True)
    print("Done!")

    metric = BLEUScore()
    metric(results, testset) # to be determined...