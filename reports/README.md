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

s183319, s194345, s185231, s184399, s194333

### Question 3
> **What framework did you choose to work with and did it help you complete the project?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the third-party framework ... in our projekkkkct. We used functionality ... and functionality ... from the*
> *package to do ... and ... in our project*.
>
> Answer:

In this project we utilized the [Transformers](https://github.com/huggingface/transformers) repository from the Huggingface group. This repository provides the [t5-small model](https://huggingface.co/t5-small), which is a natural language processing (NLP) model that can translate text from one language to another. In this project we have used the Trainer class in the pytorch lightning framework to train and test the t5-small model on a subset of the english/ german (en-de) subset of the [WMT19 dataset](https://huggingface.co/datasets/wmt19) (from the fourth conference on machine translation). We have used Weights and biases (`wandb`) to both handle the configuration file with the hyperparameters for the model and for logging the training and validation loss. 

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

Packages are mananged in conda environments. The packages required can be found in the requirements.txt file which is placed in the top folder in the cookiecutter structure. In this txt file we have a complete list of all used packages and relevant versions in this project. The requirement.txt file was auto-generated using the command pipreqs. To get a complete copy of our development enviroment, one would have to run the following commands (assuming they have git and Python 3.10 installed):
```
git clone https://github.com/MikkelGodsk/dtu_mlops_exam_project.git
cd dtu_mlops_exam_project
conda create -n myenv
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

The overall structure is initialized with the cookiecutter template. In general we tried to follow the cookiecutter structure as much as possible. Since the original WMT19 dataset took up too much memory in both cloud and drive, we processed the data locally and only included a subset in the proccessed folder in the data folder. Thus we deleted the data/external/, data/interim/ and data/raw/ folders. We also deleted the folders notebooks/, references/, src/features/, src/visualization/, since we did not use these. We filled out the src/data/ folder and the src/models/ folder in which we also included a file src/models/evaluate_model.py for evaluating the model and a folder src/models/config/, with the configuration files.
We also included the tests/ folder which holds scripts for conducting different pytests.


### Question 6

> **Did you implement any rules for code quality and format? Additionally, explain with your own words why these**
> **concepts matters in larger projects.**
>
> Answer length: 50-100 words.
>
> Answer:

In this project we have used typing and written comments when the code is not completly self explanatory, in addition to function docstrings. We tried to ensure that the code is pep8 compliant. To obtain this we have used black to format the code and flake8 to check. Lastly, we used isort to sort our imports. The code quality and format is tested in github actions, hence constantly ensuring the quality. Using these methods makes it much easier to share code and ensures the readability.

## Version control

> In the following section we are interested in how version control was used in your project during development to
> corporate and increase the quality of your code.

### Question 7

> **How many tests did you implement?**
>
> Answer: 

7

### Question 8

> **What is the total code coverage (in percentage) of your code? If you code had a code coverage of 100% (or close**
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
| Name                          | STMTS | Miss | Cover | Missing        |
|-------------------------------|-------|------|-------|----------------|
| ./src/\_\_init\_\_.py         | 0     | 0    | 100%  | -              |
| ./src/models/\_\_init\_\_.py  | 2     | 0    | 100%  | -              |
| ./src/models/model.py         | 48    | 4    | 92%   | 45, 47, 49, 51 |
| ./src/models/predict_model.py | 21    | 7    | 67%   | 21, 29-37      |
| ./tests/\_\_init\_\_.py       | 5     | 0    | 100%  | -              |
| ./tests/test_api.py           | 11    | 0    | 100%  | -              |
| ./tests/test_dataset.py       | 18    | 0    | 100%  | -              |
| ./tests/test_model.py         | 43    | 0    | 100%  | -              |
| TOTAL                         | 148   | 11   | 93%   | -              |

The reason for the code coverage less than 100% in the file `model.py` is that we deemed some of the checks in the constructor (`__init__`) too trivial to test. These are just checking for the data type and non-negativity of learning-rate and batch size.

In `predict_model.py`, the reason for the coverage being less than 100% is that we do not test with loading in a checkpoint. Unless we transfered this to GitHub, it would not be able to run in actions. Lastly, we have tested the code run in the `if __name__ == '__main__':`-block. In order to do so we had to open a pipe to another cmd using `os.popen` doing so, so the code is simply not counted here.

### Question 9

> **Did your workflow include using branches and pull requests? If yes, explain how. If not, explain how branches and**
> **pull request can help improve version control.**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of both branches and PRs in our project. In our group, each member had a branch that they worked on in*
> *addition to the main branch. To merge code we ...*
>
> Answer:

We added branch protection on the main branch. Hence we created a feature branch where changes were made. We then used pull requests to merge with the main branch quite often. A pull request typically only concerned a few changes in a limited amount of scripts. Hence we avoided having an unmanageable amount of branches as well as reduced the number of merge conflicts. Before merging a branch with the main branch the tests are conducted to ensure that the merge will result in a working code. Furthermore when making major changes we assured that pull request were created and reviewed immediately.

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

The wmt19 dataset originally contained around 9GB of data. Hence we decided to create a subset of the dataset. Data version control hereby contributed to an easy update of the data. We initially created a bucket in Google Cloud and used dvc to manage this. However s194333 did not have enough credit to sustain this service hence we had to create another bucket containing the same data with a different billing account. However we also stored the data on google drive, in case we potentially would use all credits on cloud again. Hence the dvc package proved to be very usefull for switching between different data storage options. In addition, dvc was an easy update to implement on all our devices since it only required some simple terminal commands. 

### Question 11

> **Discuss your continues integration setup. What kind of CI are you running (unittesting, linting, etc.)? Do you test**
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

We have organized our continues integration into three separate files: one for doing unittesting, one for running isort testing and one for running flake8. The isort test and the flake8 test are only run on the Ubuntu operating system and the python version 3.8. The unittesting is also run on the windows operating system and python version 3.10. Here we also make use of caching to speed up the process. Testing the dataset consists of loading the data and checking whether the format is correct. More precicely we check if the data (en-de) is given as a string and a label. When testing the model the following things must be satisfied
- The model is in torch
- The model outputs the translated sentence as a list containing a string
- In both training, validation and test the model outputs a torch tensor containing a float (not NaN)

Link to github actions:
https://github.com/MikkelGodsk/dtu_mlops_exam_project/actions/runs/3961726045/workflow


## Running code and tracking experiments

> In the following section we are interested in learning more about the experimental setup for running your code and
> especially the reproducibility of your experiments.

### Question 12

> **How did you configure experiments? Did you make use of config files? Explain with coding examples of how you would**
> **run an experiment.**
>
> Answer length: 50-100 words.
>
> Example:
> *We used a simple argparser, that worked in the following way: python my_script.py --lr 1e-3 --batch_size 25*
>
> Answer:

When training the model the hyperparameters are by default loaded from the configuration file src/models/config/default_params.yaml. It is also possible to pass a different path using the argparser. The configuration file contains the learning rate, number of epochs, the batch size of the model and a seed if reproducability is desired. The configuration file is passed to the wandb.init() function and the hyperparameters are loaded into the training script with the following code:

lr = wandb.config.lr
epochs = wandb.config.epochs
batch_size = wandb.config.batch_size

We utilized the *sweep* functionality of `wandb` in an attempt to optimize hyperparamters. Through `wandb` the hyperparameter configuration was logged. The hyperparameters for the different experiments are then set to the hyperparameters resulting in the best validation loss.

When using the src/models/predict_model.py we use a simple argparser to give the input string to be translated along with the checkpoint file containing the trained model weights.

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

 When we load the config file the hyperparameters of the model is set to the values provided in the file. Hence one can easily see which parameters are used to train. However, when conducting experiments it is important to track which parameters are used. By ensuring commits between changes in config file we make sure that experiments are logged in the git commit history. In order to reproduce the experiments we included a seed in the configuration file. Hereby we ensure that the exact same results are obtained when training a model with a specific set of hyperparameters. Furthermore we created docker images, which ensures that our models can be run on all computers. By running multiple experiments in W&B we ensure that hyperparameters are kept in W&B.

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

In W&B we track the training loss as seen on the figure below.

![Training loss](figures/train_loss.png)

We see a small descrease of the loss. This metric is essential for showing whether the model is learning from the data during the training. 

We also track the validation loss as seen on the figure below.

![Validation loss](figures/val_loss.png)

The validation loss is very important to monitor the models performance when presented to unknown data. 

We also perform a sweep in an attempt to optimize hyperparamters based on obtaining the lowest possible validation loss.

![Sweep hyperparameters](figures/hyperparams.png)

This did however show us that with the best hyperparameterse the validation loss remains constant.

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

In our project, reproducablity is very important, hence we utilize Docker in order to ensure that the application can be run on all devices. Hence we created docker images for training and deploying the model. Since building docker images are a time consuming task, we prefred google cloud for building the dockerimages in cloud using a dockerfile and triggers. After being build the docker images are run using google cloud Run.
A link to the training docker file is provided in the following:
https://github.com/MikkelGodsk/dtu_mlops_exam_project/blob/main/trainer.dockerfile


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

When locally executing code we used the build in debugger in visual studio code and when this was not enought we used simple print statements. The debugging mode in visual studio is in general quite informative and helpfull when erros occured. When for example building images in google cloud a lot of errors occured. Hence debugging needed to be performed locally before building in cloud.

We used the inbuild tool from pytorch lightning for profiling the training, but we did not really do anything to improve the code based on the profilling. However we are avare that the code might be edible for improvements. For example, we considered saving the tokenized dataset, which would probably speed up the training processes, such that the tokenization is not necessary every time the training function is called.

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

Buckets:
We used GCP buckets for initally storing the data. However we quickly ran out of credits and hence had to create a new bucket containg the same data but with a different billing account. Furthermore we also used buckets for storring checkpoints. 

Build:
Images are build using cloud build.

Triggers:
In order to automatically build images triggers are used to connect the github repository to google cloud

Containers:
Images are stored in containers 

Run:
Models are deployed using google Run

Vertex AI:
Training framework where we run the docker image


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

In this project we did not utilize the Compute engine and used Vertex AI instead. 

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

![GCP Registry](figures/gcp_registry.png)


### Question 21

> **Upload one image of your GCP cloud build history, so we can see the history of the images that have been build in**
> **your project. You can take inspiration from [this figure](figures/build.png).**
>
> Answer:

![Build history](figures/build_history_cloud.png)

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

Deploying the model locally was quite straight forward. Inputs to the model can easily be given through the terminal. However deploying in google cloud caused a lot more complication. For deployment we wrapped our model into an application using FastAPI and used cloud run. We were heavily challenged by the fact that after training the model the checkpoint could not be saved to a bucket on cloud without authentication, which we did not manage to implement. Hence we did not use the finetuned model for deployment directly trough cloud. 
We did however manage to finetune the model on the hypatia cluster at DTU and uploading a checkpoint to bucket, however we had issues with downloading he checkpoint from within the python code (again due to authentication issues). Given a little more time, it would have been easy to setup DVC such that the model weights would be store alongside the dataset, whence we should have been able to get the finetuned model to deploy.

In the training file, we used distributed data loading and multiple workers implemented through pytorch-lightning.

Link to our model: 
https://translation-gcp-app-jc4crsqeca-lz.a.run.app/translate/How are you doing?


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

We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could measure translation accuracy (based e.g on user rating) that would inform us about the performance and hence usefullness of our model. Provided we modelled the german and english language perfectly, our model would be quite prone to data-drifting. The only real issue would be words having new meanings or new words being adapted to the languages. However, this *perfect* modelling is rarely the case in real life as the dataset for a given translation task, will ultimately only be a subset of the distribution modelling the language. This means that our model will be context dependent. A weakness derived from this could e.g. be if the training dataset was exceedingly formal and we received an input which was very informal. As such, monitoring a user-based translation accuracy score could inform when our model becomes outdated.

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

s194333 did not use any credit for this project, since she managed to use all her credit on the project created for M21. In total on this project together we used around 5 dollars. Google cloud was not very transparent about billing account or money usage.  

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
> *Whenever we commit code and push to github, it auto triggers ... and ... . From there the diagram shows ...*
>
> Answer:

![Graphical reprsentation of architecture](figures/graphical_representation_of_architecture.png)
The starting point of the diagram is our local pytorch application, which we wrapped in the **pytorch lightning** framework. This served as the inital steps of creating the mlops pipeline. We version-controled our project using **git** via **Github**. A new environment can be initialized using either **Conda** or **pip**. We opted to use `pipreqs` for finding the package requirements of our project, which made for seamless instantiation of the projects *requirements.txt*. We utilized `wandb` in conjunction with **pytorch lightning** for logging the 'experiments'/ training of our *NLP* model. For training configuration `wandb` performed satisfactory, hence `hydra` was omited from this project. These are the essential parts which are contained into a **docker** container. Locally the project follows the codestructure of **Cookiecutter**. 

In order to utilize the **GPC** git and dvc both provides a link from the local machine. Git furthermore enabled **Github actions** for testing the code before uploading to a remote storage. Using a **trigger** connected to the github repository we created **docker images** in **docker containers** in the cloud. 

When training a dataset stored in a **GCP bucket** was utilized. Information sharing and version control of the dataset was handled by utilizing **dvc**. We interfaced with our application through **Cloud Run** by using the **Fast API** framework. Finally, we didn't utilize monitoring as we had plenty of work on our hands, trying to interface with and getting our model to run on cloud.

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

Our first time consuming task was to download the data. This was downloaded from huggingface which took a long time. We also spent an excessive amount of time trying to train our model on cloud. Some main factors contributing to this issue, was our funding running short and having to authenticate multiple frameworks within a docker container. s194333 created the project on GCP, however she quickly (within 48 hours) ran short on funding (complementary of the course) due to operations ineracting with the *bucket* storing our data. We aren't entirely certain as to what depleted the grants, however this greatly restricted our work. From docker we needed to authenticate dvc, GCP, in addition to `wandb`. This proved tremendously cumbersome as the authentication requires certfication, which we would preferably avoid storing in the docker image. During this process we spent a lot of time debugging. Due to long building times errors didn't occur immediatly, which resulted in a lot of reapeated idle time. 

In general most of the tools and frameworks were relativly new for us, which resulted in a lot of google searches and unknown errors. The exercises significantly prepared us for conducting the project, however we still had a lot to learn when making the project. This challenged us in many ways, however we ultimately managed to overcome these.

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


Student s184399 created github repository with the cookiecutter structure. Furthermore the student was in charge of testing the models using unittesting and other previously mentioned tests. Furthermore he also contributed to building the docker images in the cloud and deploying the model. 

Student s185231 was in charge of building the docker images in the cloud. Furthermore the student helped downloading the data and creating the scripts for training and testing the model.

Student s183319 heavily contributed to the report and was in charge of managing the dependencies and set up of version control as well as a lot of debugging.

Student 194333 was responsible for creating the scripts for training and prediction as well as afterwards training the model. Furthermore the student analysed the results and performed a sweep in W&B.

Student s194245 was in charge of handeling the data -all the way from downloading to utilizing. Furthermore the student was in charge of utilizing google cloud for training. 