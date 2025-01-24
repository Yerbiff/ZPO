# ZPO Project - Your Deepness Model
AT THE TOP OF THIS README ADD AN IMAGE/GIF WITH EXAMPLE MODEL PREICTION, AS A BANNER


## Dataset
- photos extracted from QGIS - Poznan 2023 aerial orthophoto high resolution
- 6382 annotations [376 free-standing-pool, 36 permanent-pool, 18 pond, 5953 none]
- resolution: 10 cm/pixel
- input window size: 512x512 pixels
- dataset with annotations in [roboflow](https://app.roboflow.com/poolsearch2024/pool_searching/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)

How to load data:
```
!mkdir {HOME}/datasets
%cd {HOME}/datasets

from google.colab import userdata
from roboflow import Roboflow

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_API_KEY*")
project = rf.workspace("poolsearch2024").project("pool_searching")
version = project.version(3)
dataset = version.download("yolov11")
```
*YOUR_API_KEY - znajdziesz go w ustawieniach po założeniu konta na roboflow.com 

## Training
- Colab Environment Setup - Installation Steps:
```
!nvidia-smi
```
Let's make sure that we have access to GPU. We can use nvidia-smi command to do that. In case of any problems navigate to Edit -> Notebook settings -> Hardware accelerator, set it to GPU, and then click Save.
```
import os
HOME = os.getcwd()
print(HOME)
```
NOTE: To make it easier for us to manage datasets, images and models we create a HOME constant.
```
%pip install "ultralytics<=8.3.40" supervision roboflow
import ultralytics
ultralytics.checks()
```
Install YOLO11 via Ultralytics

- what network, how trained, what parameters
- what augmentation methods used
- what script to run the training
- remember to have a fully specified Python environemnt (Python version, requirements list with versions)
- other instructions to reproduce the training process

## Results
- Example images from dataset (diverse), at least 4 images
- Examples of good and bad predictions, at least 4 images
- Metrics on the test and train dataset

## Trained model in ONNX ready for `Deepness` plugin
- model uploaded to XXX and a LINK_HERE
- model have to be in the ONNX format, including metadata required by `Deepness` plugin (spatial resolution, thresholds, ...)
- name of the script used to convert the model to ONNX and add the metadata to it

## Demo instructions and video
- a short video of running the model in Deepness (no need for audio), preferably converted to GIF
- what ortophoto to load in QGIS and what physical place to zoom-in. E.g. Poznan 2022 zoomed-in at PUT campus
- showing the results of running the model

## People
__Yerbiff__ - [Github](https://github.com/Yerbiff) (Jarosław Kuźma 147617)

__the_HaUBe__ - [Github](https://github.com/theHaUBe) (Hubert Górecki 147599)

## Other information
Feel free to add other information here.
