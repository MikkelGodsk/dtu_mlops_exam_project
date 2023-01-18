import os

import pytest
from datasets import Dataset

from tests import _PATH_DATA


@pytest.mark.skipif(not os.path.exists(_PATH_DATA), reason="Data files not found")
def test_dataset_format():
    trainset = Dataset.load_from_disk("data/processed/train")
    testset = Dataset.load_from_disk("data/processed/validation")

    X_train = trainset[0]
    X_test = testset[0]

    assert list(X_train.keys()) == ["translation"]
    assert set(X_train["translation"].keys()) == {"en", "de"}
    assert isinstance(X_train["translation"]["en"], str)
    assert isinstance(X_train["translation"]["de"], str)

    assert list(X_test.keys()) == ["translation"]
    assert set(X_test["translation"].keys()) == {"en", "de"}
    assert isinstance(X_test["translation"]["en"][0], str)
    assert isinstance(X_test["translation"]["de"][0], str)
