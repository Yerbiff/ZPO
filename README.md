# ZPO Project - Your Deepness Model
AT THE TOP OF THIS README ADD AN IMAGE/GIF WITH EXAMPLE MODEL PREICTION, AS A BANNER


## Dataset
- photos from Poznan 2023 aerial orthophoto high resolution
- 6382 annotations [376 free-standing-pool, 36 permanent-pool, 18 pond, 5953 none]
- how the data was prepared (e.g. preprocessed)
- dataset with annotations in [roboflow](https://app.roboflow.com/poolsearch2024/pool_searching/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)
- what format for data and
- how to load data
'''
!mkdir {HOME}/datasets
%cd {HOME}/datasets

from google.colab import userdata
from roboflow import Roboflow

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("poolsearch2024").project("pool_searching")
version = project.version(3)
dataset = version.download("yolov11")
'''

## Training
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
