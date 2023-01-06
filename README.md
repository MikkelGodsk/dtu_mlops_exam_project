dtu_mlops_exam_project
==============================

Exam project for course 02476 MLOps at DTU

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------


In this project we wish to obtain a translater from English to German. We finetune the <a target="_blank" href="https://huggingface.co/t5-small">t5-small model</a> using the <a target="_blank" href="https://huggingface.co/datasets/wmt19"> WMT19 dataset</a>. This dataset contains translation pairs in multiple languages and is part of the conference <a target="_blank" href="https://machinetranslate.org/wmt">(WMT)</a> on machine learning translation.
    
T5 is a text-to-text model and the model from Huggingface is already able to translate multiple languages as well as perform other tasks within NLP. However, we seek to finetune it for translation of english to german. In order to train the model we utilize the <a target="_blank" href="https://github.com/huggingface/transformers">Transformer framework</a>. This framework provides a large variery of tools for working with transformers in Python, where we will utilize relevant functions for finetuning as well as pytorch lightening. 
    
In this project we highly focus on obtaining a good model pipeline. In order to obtain this goal we will utilize many different tools such as cookiecutter for document structure, docker to containerising our code as dvc for handeling data.

Furthermore Weights and Biases will provide usefull insight in the performance of the model.

    


