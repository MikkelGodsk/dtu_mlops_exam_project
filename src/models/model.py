from typing import List, Optional, Dict

import pytorch_lightning as pl
import sentencepiece  # To ensure it is found by pipreqs
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

from src.models import _MODEL_PATH


class Model(pl.LightningModule):
    def __init__(self, lr=1e-3, batch_size=1, *args, **kwargs):
        """
            Models are obtained using the code from https://huggingface.co/docs/transformers/model_doc/t5
        """
        super().__init__(*args, **kwargs)
        self.tokenizer = T5Tokenizer.from_pretrained("t5-small", cache_dir=_MODEL_PATH)

        self.t5_model = T5ForConditionalGeneration.from_pretrained(
            "t5-small", cache_dir=_MODEL_PATH
        )
        self.add_module("t5",self.t5_model)
        self.lr = lr
        self.batch_size = batch_size

    def forward(self, x: List[str]) -> List[str]:
        """
            https://huggingface.co/docs/transformers/model_doc/t5#inference
        """

        input_ids = self.tokenizer(
            x, return_tensors="pt", padding=True, truncation=True, max_length=128
        ).input_ids.to(self.t5_model.device)

        # forward pass
        outputs = self.t5_model.generate(input_ids=input_ids)

        return [
            self.tokenizer.decode(output, skip_special_tokens=True)
            for output in outputs
        ]

    def _inference_training(
        self, batch: Dict[str, Dict[str, List[str]]], batch_idx: Optional[int] = None
    ) -> torch.Tensor:
        """
            From https://huggingface.co/docs/transformers/model_doc/t5#training
        """
        data = batch["translation"]["en"]
        labels = batch["translation"]["de"]
        encoding = self.tokenizer(
            data,
            return_tensors="pt",
            padding="longest",
            truncation=True,
            max_length=512,
        ).to(self.t5_model.device)
        target_encoding = self.tokenizer(
            labels, return_tensors="pt", padding=True, truncation=True, max_length=128
        ).input_ids.to(self.t5_model.device)
        input_ids = encoding["input_ids"]
        attention_mask = encoding["attention_mask"]
        loss = self.t5_model(
            input_ids=input_ids, attention_mask=attention_mask, labels=target_encoding,
        ).loss
        return loss

    def training_step(
        self, batch: List[str], batch_idx: Optional[int] = None
    ) -> torch.Tensor:
        loss = self._inference_training(batch, batch_idx)
        self.log("train loss", loss, batch_size=self.batch_size)
        # TODO: Add metrics
        return loss

    def validation_step(
        self, batch: List[str], batch_idx: Optional[int] = None
    ) -> torch.Tensor:
        loss = self._inference_training(batch, batch_idx)
        self.log("val loss", loss, batch_size=self.batch_size)
        # TODO: Add metrics
        return loss

    def test_step(
        self, batch: List[str], batch_idx: Optional[int] = None
    ) -> torch.Tensor:
        loss = self._inference_training(batch, batch_idx)
        self.log("test loss", loss, batch_size=self.batch_size)
        # TODO: Add metrics
        return loss

    def configure_optimizers(self) -> torch.optim.Optimizer:
        return torch.optim.Adam(self.t5_model.parameters(), lr=self.lr)
