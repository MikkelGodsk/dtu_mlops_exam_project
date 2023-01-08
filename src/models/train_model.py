import wandb
from model import Model

wandb.init(project="mlops_exam_project", entity="chrillebon", config="config/dafault_params.yaml")

lr = wandb.config.lr
epochs = wandb.config.epochs
batch_size = wandb.config.batch_size

model = Model
wandb.watch(model, log_freq=100)

print("hello world")
