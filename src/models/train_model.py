import wandb
from src.models.model import Model
from src.models import _DATA_PATH

wandb.init(project="mlops_exam_project", entity="chrillebon", config="src/models/config/default_params.yaml")

lr = wandb.config.lr
epochs = wandb.config.epochs
batch_size = wandb.config.batch_size

model = Model(lr)
wandb.watch(model, log_freq=100)
model.training_step()

trainer = pl.Trainer(max_epochs=epochs, default_root_dir = 'models', logger=pl.loggers.WandbLogger(project="mnist"), log_every_n_steps = 1)
trainer.fit(model=model, train_dataloaders=trainloader, val_dataloaders=testloader)
print("hello world")
