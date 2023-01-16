from copy import deepcopy

import pytest
import torch
from pytorch_lightning import Trainer
import datasets
from tqdm import tqdm
import numpy as np

from src.models.model import Model


def test_model_is_torch():
    model = Model()
    assert isinstance(
        next(iter(model.t5_model.parameters())), torch.Tensor
    )  # To ensure that it runs in torch.


def test_model_output():
    input = ["The house is wonderful", "I am hungry"]
    model = Model()
    output = model(input)
    assert isinstance(output, list)
    assert output != []
    assert isinstance(output[0], str)


def test_steps():
    batch = {
        "translation": {
            "en": ["The house is wonderful", "I am hungry"],
            "de": ["Das Haus ist wunderbar.", "Ich habe hunger."],
        }
    }
    model = Model()
    loss = model.training_step(batch)
    assert isinstance(loss.item(), float) # loss is given as a float
    assert isinstance(loss, torch.Tensor) # loss is a torch tensor
    assert not torch.any(torch.isnan(loss)).item() # loss is not nan

    loss = model.validation_step(batch)
    assert isinstance(loss.item(), float)
    assert isinstance(loss, torch.Tensor)
    assert not torch.any(torch.isnan(loss)).item()

    loss = model.test_step(batch)
    assert isinstance(loss.item(), float)
    assert isinstance(loss, torch.Tensor)
    assert not torch.any(torch.isnan(loss)).item()


def test_training_loop():
    """
        Runs a training loop and checks if the weights change.
    """
    torch.manual_seed(42)
    batch = {
        "translation": {
            "en": ["The house is wonderful", "I am hungry"],
            "de": ["Das Haus ist wunderbar.", "Ich habe hunger."],
        }
    }
    ds = datasets.Dataset.from_list([batch])
    model = Model(lr=1e-3)
    old_params = deepcopy(model.state_dict())

    # Overfit model in Pytorch Lightning
    trainer = Trainer(
        enable_progress_bar=True, 
        enable_checkpointing=False, 
        max_epochs=40, 
        overfit_batches=1,
        log_every_n_steps=1,
    )
    trainer.fit(model, ds)
    print(trainer.logged_metrics['train loss'].item())
    assert trainer.logged_metrics['train loss'].item() < 0.1

    new_params = deepcopy(model.state_dict())
    for k in tqdm(old_params.keys()):
        assert torch.any(old_params[k] != new_params[k]).item()
