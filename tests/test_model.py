import pytest
import torch
from pytorch_lightning import Trainer
from copy import deepcopy

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


def test_training_step():
    input = ["The house is wonderful", "I am hungry"]
    labels = ["Das Haus ist wunderbar.", "Ich habe hunger."]
    model = Model()
    loss = model.training_step((input, labels))
    assert isinstance(loss.item(), float)
    assert isinstance(loss, torch.Tensor)


def test_training_loop():
    raise NotImplemented
    input = ["The house is wonderful", "I am hungry"]
    labels = ["Das Haus ist wunderbar.", "Ich habe hunger."]
    model = Model()
    old_params = deepcopy(model.state_dict())
    ds = torch.utils.data.TensorDataset(input, labels)   # Needs to be torch tensor or a custom dataset
    trainer = Trainer()
    

    #train model one step in lightning
    new_params = deepcopy(model.state_dict())
    for k in old_params.keys():
        assert torch.any(old_params[k] != new_params[k])

