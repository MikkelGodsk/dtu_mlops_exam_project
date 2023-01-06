from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import pytorch_lightning as pl
import sentencepiece # so it is put into requirements.txt


DEVICE = 'cpu' if not torch.cuda.is_available() else 'cuda'

class Model(pl.LightningModule):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tokenizer = T5Tokenizer.from_pretrained("t5-small")
        self.t5_model = T5ForConditionalGeneration.from_pretrained("t5-small")
        self.t5_model.to(DEVICE)   # https://huggingface.co/docs/transformers/model_doc/t5
        assert isinstance(next(iter(self.t5_model.parameters())), torch.Tensor)  # To ensure that it runs in torch.

    def forward(self, x):
        input_ids = self.tokenizer(
            x, 
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=128
        ).input_ids.to(DEVICE)  # Batch size 1
        
        # forward pass
        outputs = self.t5_model.generate(input_ids=input_ids)   # For training, see https://huggingface.co/docs/transformers/model_doc/t5#training

        return [self.tokenizer.decode(output, skip_special_tokens=True) for output in outputs]  # https://huggingface.co/docs/transformers/model_doc/t5#inference


if __name__ == '__main__':
    input = ['The house is wonderful', 'I am hungry']
    model = Model()
    print(model(input))

