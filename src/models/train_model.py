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

print("hello world")
