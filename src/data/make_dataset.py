# -*- coding: utf-8 -*-
import logging
from pathlib import Path

import click
from datasets import load_dataset, Dataset
from dotenv import find_dotenv, load_dotenv
import os


@click.command()
@click.argument('cache_dir', type=click.Path(exists=True))
@click.argument('k', type=int)
def main(cache_dir, k):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")

    dataset = load_dataset('wmt19', 'de-en', cache_dir=cache_dir)

    traindata = Dataset.from_dict(dataset["train"][:k])
    valdata = Dataset.from_dict(dataset["validation"][:k])
    traindata.save_to_disk(os.path.join(cache_dir, "processed", "train"))
    valdata.save_to_disk(os.path.join(cache_dir, "processed", "train"))


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
