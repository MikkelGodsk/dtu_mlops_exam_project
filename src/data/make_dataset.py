# -*- coding: utf-8 -*-
import logging
import os
from pathlib import Path
from typing import Optional

import click
from datasets import Dataset, load_dataset
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('cache_dir', type=click.Path(exists=True))
@click.argument('k', type=int)
def main(cache_dir : str, k : Optional[int] = None) -> None:
    """
    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    
    Parameters
    ----------
    cache_dir : str, required
        A path to where the data is located.
    
    k : integer, optional
        The amount of datapoints to include from the the dataset.
    
    Raises
    ------
    TypeError
        If the cache_dir isn't a string.
    TypeError
        If k isn't an integer.
    ValueError
        If k is a negative integerr
    """
    
    if type(cache_dir) is not str:
        raise TypeError("cache_dir must be a string denoting the path to the data location.")
    if k is not None and type(k) is not int:
        raise TypeError("k must denote the amount (in an integer) of datapoints to include.")
    if k <= 0:
        raise ValueError("k must be a positive amount of datapoints.")
    
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")

    dataset = load_dataset('wmt19', 'de-en', cache_dir=cache_dir)
    
    if k is None:
        traindata = Dataset.from_dict(dataset["train"])
        valdata = Dataset.from_dict(dataset["validation"])
    else: 
        traindata = Dataset.from_dict(dataset["train"][:k])
        valdata = Dataset.from_dict(dataset["validation"][:k])
    
    traindata.save_to_disk(os.path.join(cache_dir, "processed", "train"))
    valdata.save_to_disk(os.path.join(cache_dir, "processed", "val"))


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
