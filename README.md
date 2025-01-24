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

## Colab Environment Setup - Installation Steps
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

## Training Configuration

### Network
- Model: YOLO v11s (base model)
- Pretrained weights: `yolo11s.pt`

### Training Parameters
- Task: Object Detection
- Training Epochs: 100
- Image Size: 640x640 pixels
- Batch Size: 16
- Learning Rate: 0.001
- Optimizer: AdamW
- Warmup Epochs: 3

### Data Augmentation Techniques
- HSV Color Space Augmentation:
  - Hue Shift: ±0.015
  - Saturation Shift: 0.7
  - Value Shift: 0.4
- Geometric Transformations:
  - Rotation: ±10 degrees
  - Translation: 0.1
  - Scale: 0.5
- Flipping:
  - Horizontal Flip: 0.5 probability
  - Vertical Flip: 0.3 probability
- Advanced Augmentations:
  - Mosaic: 1.0
  - Mixup: 0.1
  - Copy-Paste: 0.1

## Training Script
```bash
yolo task=detect \
     mode=train \
     model=yolo11s.pt \
     data={dataset.location}/data.yaml \
     epochs=100 \
     imgsz=640 \
     batch=16 \
     lr0=0.001 \
     optimizer='AdamW' \
     warmup_epochs=3 \
     hsv_h=0.015 \
     hsv_s=0.7 \
     hsv_v=0.4 \
     degrees=10.0 \
     translate=0.1 \
     scale=0.5 \
     fliplr=0.5 \
     flipud=0.3 \
     mosaic=1.0 \
     mixup=0.1 \
     copy_paste=0.1 \
     plots=True
```

## Model Export
The best-performing model weights will be saved at:
`{HOME}/runs/detect/train/weights/best.pt`

### Google Colab Export
```python
from google.colab import drive
import os
import torch

# Mount Google Drive
drive.mount('/content/drive')

# Copy trained model to Google Drive
model_path = f"{HOME}/runs/detect/train/weights/best.pt"
drive.copy(model_path, '/content/drive/My Drive/trained_yolo_model.pt')
```

## Notes
- Ensure your `data.yaml` is properly configured with dataset paths and class information
- Adjust augmentation parameters based on your specific dataset characteristics
- Monitor training logs for performance metrics

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
