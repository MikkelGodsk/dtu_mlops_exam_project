from datasets import load_dataset

dataset = load_dataset('wmt19', 'de-en', cache_dir="data/")

print(dataset)
print(dataset["train"][0])