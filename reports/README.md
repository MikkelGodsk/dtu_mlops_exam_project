---
layout: default
nav_exclude: true
---

# Exam template for 02476 Machine Learning Operations

This is the report template for the exam. Please only remove the text formatted as with three dashes in front and behind
like:

```--- question 1 fill here ---```

where you instead should add your answers. Any other changes may have unwanted consequences when your report is auto
generated in the end of the course. For questions where you are asked to include images, start by adding the image to
the `figures` subfolder (please only use `.png`, `.jpg` or `.jpeg`) and then add the following code in your answer:

```markdown
![my_image](figures/<image>.<extension>)
```

In addition to this markdown file, we also provide the `report.py` script that provides two utility functions:

Running:

```bash
python report.py html
```

will generate an `.html` page of your report. After deadline for answering this template, we will autoscrape
everything in this `reports` folder and then use this utility to generate an `.html` page that will be your serve
as your final handin.

Running

```bash
python report.py check
```

will check your answers in this template against the constrains listed for each question e.g. is your answer too
short, too long, have you included an image when asked to.

For both functions to work it is important that you do not rename anything. The script have two dependencies that can
be installed with `pip install click markdown`.

## Group information

### Question 1
> **Enter the group number you signed up on <learn.inside.dtu.dk>**
>
> Answer:

41

### Question 2
> **Enter the study number for each member in the group**
>
> Answer:

s183319, ss194345, s185231, s184399, s194333

### Question 3
> **What framework did you choose to work with and did it help you complete the project?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the third-party framework ... in our project. We used functionality ... and functionality ... from the*
> *package to do ... and ... in our project*.
>
> Answer:

In this project we utilized the <a target="_blank" href="https://github.com/huggingface/transformers">Transformers</a> repository from the Huggingface group. This repository provides the <a target="_blank" href="https://huggingface.co/t5-small">t5-small model</a>, which is a language model that can translate text from one language to another. In this project we have used the Trainer class in the pytorch lightening framework to train and test the t5-small model on a subset of the en-de subset of the <a target="_blank" href="https://huggingface.co/datasets/wmt19"> WMT19 dataset</a>. We have used Weights and biases to both handle the configuration file with the hyperparameters for the model and for logging the training.

## Coding environment

> In the following section we are interested in learning more about you local development environment.

### Question 4

> **Explain how you managed dependencies in your project? Explain the process a new team member would have to go**
> **through to get an exact copy of your environment.**
>
> Answer length: 100-200 words
>
> Example:
> *We used ... for managing our dependencies. The list of dependencies was auto-generated using ... . To get a*
> *complete copy of our development enviroment, one would have to run the following commands*
>
> Answer:
The new member would have to run the commands (assuming they have git and Python 3.10 installed):
```
git clone https://github.com/MikkelGodsk/dtu_mlops_exam_project.git
cd dtu_mlops_exam_project
pip install -r requirements.txt
dvc pull
python setup.py install
```

### Question 5

> **We expect that you initialized your project using the cookiecutter template. Explain the overall structure of your code. Did you fill out every folder or only a subset?**
>
> Answer length: 100-200 words
>
> Example:
> *From the cookiecutter template we have filled out the ... , ... and ... folder. We have removed the ... folder*
> *because we did not use any ... in our project. We have added an ... folder that contains ... for running our*
> *experiments.*
> Answer:

The overall structure is initialized with the cookiecutter template. In general we tried to as much as possible to follow the cookiecutter structure. Since the original WMT19 dataset took up to much memory in both cloud and drive, we processed the data locally and only included a subset in the proccessed folder in the data folder. Thus we deleted the data/external, data/interim and data/raw folders. We also deleted the folders notebooks, references, src/features, src/visualization, since we did not use these. We filled out the src/data folder and the src/models folder in which we also included a file for evaluating the model and a folder config, with the configuration files.
We also included the tests folder which holds scripts for conducting different pytests.


### Question 6

> **Did you implement any rules for code quality and format? Additionally, explain with your own words why these**
> **concepts matters in larger projects.**
>
> Answer length: 50-100 words.
>
> Answer:

In this project we have used typing and written comments when the code is not completly self explanatory. We tried to ensure that the code is pep8 compliant. To obtain this we have used black to format the code and flake8 to check that the code is pep8 compliant. Lastly, we used isort to sort our imports.

## Version control

> In the following section we are interested in how version control was used in your project during development to
> corporate and increase the quality of your code.

### Question 7

> **How many tests did you implement?**
>
> Answer: 

7

### Question 8

> **What is the total code coverage (in percentage) of your code? If you code had an code coverage of 100% (or close**
> **to), would you still trust it to be error free? Explain you reasoning.**
>
> **Answer length: 100-200 words.**
>
> Example:
> *The total code coverage of code is X%, which includes all our source code. We are far from 100% coverage of our **
> *code and even if we were then...*
>
> Answer: 

The total code coverage of code is 93%, which includes all our source code.

Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
src\__init__.py                   0      0   100%
src\models\__init__.py            2      0   100%
src\models\model.py              48      4    92%   45, 47, 49, 51
src\models\predict_model.py      21      7    67%   21, 29-37
tests\__init__.py                 5      0   100%
tests\test_api.py                11      0   100%
tests\test_dataset.py            18      0   100%
tests\test_model.py              43      0   100%
-----------------------------------------------------------
TOTAL                           148     11    93%


The reason for the code coverage less than 100% in the file `model.py` is that we deemed some of the checks in the constructor (`__init__`) too trivial to test. These are just checking for the data type and non-negativity of learning-rate and batch size.

In `predict_model.py`, the reason for the coverage being less than 100% is that we do not test with loading in a checkpoint. Unless we transfered this to GitHub, it would not be able to run in actions. Lastly, we have tested the code run in the `if __name__ == '__main__':`-block, however we had to open a pipe to another cmd using `os.popen` doing so, so the code is simply not counted here.



The tests are conducted upon pushes and pull-requests to the merge branch.
Testing the dataset consists of loading the data and checking whether the format is correct. More precicely we check if the data is given as a string and a label (en-de). When testing the model the following things must be satisfied
- The model is in torch
- The model outputs the translated sentence as a list containing a string
- In both training, validation and test the model outputs a torch tensor containing a float (not NaN)

### Question 9

> **Did you workflow include using branches and pull requests? If yes, explain how. If not, explain how branches and**
> **pull request can help improve version control.**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of both branches and PRs in our project. In our group, each member had an branch that they worked on in*
> *addition to the main branch. To merge code we ...*
>
> Answer:

Yes, we added branch protection on the main branch. Hence we created a personal branch where changes is made. We then used pull requests to merge with the main branch quite often. A pull request typically only concerned a few changes in a limited amount of scripts. Hence we avoided having an unmanageable amount of branches as well as reduced the number of merge conflicts. Before merging a branch with the main branch the tests are conducted to ensure that the merge will result in a working code. Furthermore when making major changes we assured that pull request were created and reviewed immidiatly.

### Question 10

> **Did you use DVC for managing data in your project? If yes, then how did it improve your project to have version**
> **control of your data. If no, explain a case where it would be beneficial to have version control of your data.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did make use of DVC in the following way: ... . In the end it helped us in ... for controlling ... part of our*
> *pipeline*
>
> Answer:

The wmt19 dataset originally contained around 9GB of data. Hence we decided to create a subset of the dataset. Data version control hereby contributed to an easy update of the data. We initially created a bucket in google cloud and used dvc to manage this. However we did not have enough credit to sustain this service hence we moved the data to google drive. Hereby data controll proved to be very usefull since this update on all our devices was easily made with a simple terminal commands.

### Question 11

> **Discuss you continues integration setup. What kind of CI are you running (unittesting, linting, etc.)? Do you test**
> **multiple operating systems, python version etc. Do you make use of caching? Feel free to insert a link to one of**
> **your github actions workflow.**
>
> Answer length: 200-300 words.
>
> Example:
> *We have organized our continues integration into 3 separate files: one for doing ..., one for running ... testing and one for running*
> *... . In particular for our ..., we used ... .An example of a triggered workflow can be seen here: <weblink>*
>
> Answer:

We have organized our CI into 3 separate files: one for doing unittesting, one for running isort testing and one for running flake8. The isort and flake8 test is only run on the Ubuntu operating system and the python version 3.8, the unittesting is also run on the windows operating system and python version 3.10. 

## Running code and tracking experiments

> In the following section we are interested in learning more about the experimental setup for running your code and
> especially the reproducibility of your experiments.

### Question 12

> **How did you configure experiments? Did you make use of config files? Explain with coding examples of how you would**
> **run a experiment.**
>
> Answer length: 50-100 words.
>
> Example:
> *We used a simple argparser, that worked in the following way: python my_script.py --lr 1e-3 --batch_size 25*
>
> Answer:

When training the model the hyperparameters are loaded from the configuration file src/models/config/default_params.yaml. When using the src/models/predict_model.py we use a simple argparser to give the input string to be translated along with the checkpoint file containing the trained model weights.

### Question 13

> **Reproducibility of experiments are important. Related to the last question, how did you secure that no information**
> **is lost when running experiments and that your experiments are reproducible?**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of config files. Whenever an experiment is run the following happens: ... . To reproduce an experiment*
> *one would have to do ...*
>
> Answer:

--- question 13 fill here ---

### Question 14

> **Upload 1 to 3 screenshots that show the experiments that you have done in W&B (or another experiment tracking**
> **service of your choice). This may include loss graphs, logged images, hyperparameter sweeps etc. You can take**
> **inspiration from [this figure](figures/wandb.png). Explain what metrics you are tracking and why they are**
> **important.**
>
> Answer length: 200-300 words + 1 to 3 screenshots.
>
> Example:
> *As seen in the first image when have tracked ... and ... which both inform us about ... in our experiments.*
> *As seen in the second image we are also tracking ... and ...*
>
> Answer:

--- question 14 fill here ---

### Question 15

> **Docker is an important tool for creating containerized applications. Explain how you used docker in your**
> **experiments? Include how you would run your docker images and include a link to one of your docker files.**
>
> Answer length: 100-200 words.
>
> Example:
> *For our project we developed several images: one for training, inference and deployment. For example to run the*
> *training docker image: `docker run trainer:latest lr=1e-3 batch_size=64`. Link to docker file: <weblink>*
>
> Answer:

--- question 15 fill here ---

### Question 16

> **When running into bugs while trying to run your experiments, how did you perform debugging? Additionally, did you**
> **try to profile your code or do you think it is already perfect?**
>
> Answer length: 100-200 words.
>
> Example:
> *Debugging method was dependent on group member. Some just used ... and others used ... . We did a single profiling*
> *run of our main code at some point that showed ...*
>
> Answer:

--- question 16 fill here ---

## Working in the cloud

> In the following section we would like to know more about your experience when developing in the cloud.

### Question 17

> **List all the GCP services that you made use of in your project and shortly explain what each service does?**
>
> Answer length: 50-200 words.
>
> Example:
> *We used the following two services: Engine and Bucket. Engine is used for... and Bucket is used for...*
>
> Answer:

We used GCP buckets for initally storring the data. However we quickly ran out of credits and hence decided to switch to google drive for data storage instead.

### Question 18

> **The backbone of GCP is the Compute engine. Explained how you made use of this service and what type of VMs**
> **you used?**
>
> Answer length: 50-100 words.
>
> Example:
> *We used the compute engine to run our ... . We used instances with the following hardware: ... and we started the*
> *using a custom container: ...*
>
> Answer:

--- question 18 fill here ---

### Question 19

> **Insert 1-2 images of your GCP bucket, such that we can see what data you have stored in it.**
> **You can take inspiration from [this figure](figures/bucket.png).**
>
> Answer:

The bucket can be seen in the following 
```markdown
![my_image](figures/cloud_bucket.png)
```
Here the bucket wmt19-de-en refers to the full dataset whereas 30k-dataset refers to the smaller dataset.

### Question 20

> **Upload one image of your GCP container registry, such that we can see the different images that you have stored.**
> **You can take inspiration from [this figure](figures/registry.png).**
>
> Answer:

--- question 20 fill here ---

### Question 21

> **Upload one image of your GCP cloud build history, so we can see the history of the images that have been build in**
> **your project. You can take inspiration from [this figure](figures/build.png).**
>
> Answer:

--- question 21 fill here ---

### Question 22

> **Did you manage to deploy your model, either in locally or cloud? If not, describe why. If yes, describe how and**
> **preferably how you invoke your deployed service?**
>
> Answer length: 100-200 words.
>
> Example:
> *For deployment we wrapped our model into application using ... . We first tried locally serving the model, which*
> *worked. Afterwards we deployed it in the cloud, using ... . To invoke the service an user would call*
> *`curl -X POST -F "file=@file.json"<weburl>`*
> 
> Answer:

For deployment we wrapped our model into application using FastAPI. 

### Question 23

> **Did you manage to implement monitoring of your deployed model? If yes, explain how it works. If not, explain how**
> **monitoring would help the longevity of your application.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could*
> *measure ... and ... that would inform us about this ... behaviour of our application.*
>
> Answer:

We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could measure ... and ... that would inform us about this ... behaviour of our application.

### Question 24

> **How many credits did you end up using during the project and what service was most expensive?**
>
> Answer length: 25-100 words.
>
> Example:
> *Group member 1 used ..., Group member 2 used ..., in total ... credits was spend during development. The service*
> *costing the most was ... due to ...*
>
> Answer:

s194333 did not use any credit for this project, since she managed to use all her credit on the project created for M21.

## Overall discussion of project

> In the following section we would like you to think about the general structure of your project.

### Question 25

> **Include a figure that describes the overall architecture of your system and what services that you make use of.**
> **You can take inspiration from [this figure](figures/overview.png). Additionally in your own words, explain the**
> **overall steps in figure.**
>
> Answer length: 200-400 words
>
> Example:
>
> *The starting point of the diagram is our local setup, where we integrated ... and ... and ... into our code.*
> *Whenever we commit code and puch to github, it auto triggers ... and ... . From there the diagram shows ...*
>
> Answer:

--- question 25 fill here ---

### Question 26

> **Discuss the overall struggles of the project. Where did you spend most time and what did you do to overcome these**
> **challenges?**
>
> Answer length: 200-400 words.
>
> Example:
> *The biggest challenges in the project was using ... tool to do ... . The reason for this was ...*
>
> Answer:

We especially spent a lot of time on trying to train the model on cloud.

### Question 27

> **State the individual contributions of each team member. This is required information from DTU, because we need to**
> **make sure all members contributed actively to the project**
>
> Answer length: 50-200 words.
>
> Example:
> *Student sXXXXXX was in charge of developing of setting up the initial cookie cutter project and developing of the*
> *docker containers for training our applications.*
> *Student sXXXXXX was in charge of training our models in the cloud and deploying them afterwards.*
> *All members contributed to code by...*
>
> Answer:

--- question 27 fill here ---
