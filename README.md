# ZPO Project - Pool Detection Deepness Model
![image](https://github.com/user-attachments/assets/78630129-0269-4f6a-af0d-039404b6e59f)
![image](https://github.com/user-attachments/assets/9a5ae799-d37d-4b24-bfa5-5f5ffd384582)


## Dataset
- photos extracted from QGIS - Poznan 2023 aerial orthophoto high resolution
- 6382 annotations [420 free-standing-pool, 36 permanent-pool, 18 pond, 5908 none]
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
*YOUR_API_KEY - you can find it when register on roboflow.com

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
- notebook template - yolo11_pool_detection_on_dataset.ipynb

## Results

### Example Images from Dataset
Below are example images from the dataset:  

<div align="center">
  <img src="https://github.com/user-attachments/assets/50033680-8c85-47b1-9f17-6185144ef5bb" alt="Dataset Example 1" width="45%" />
  <img src="https://github.com/user-attachments/assets/003230dd-a28a-4e6c-a499-f5bbf5ce4875" alt="Dataset Example 2" width="45%" />
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/2b568263-d758-4c2d-a78d-8795c374565f" alt="Dataset Example 3" width="45%" />
  <img src="https://github.com/user-attachments/assets/b0830833-7049-488d-a1f1-683327e44ffe" alt="Dataset Example 4" width="45%" />
</div>

---

### Examples of Good and Bad Predictions
Here are examples of the model's good and bad predictions:  

<div align="center">
  <img src="https://github.com/user-attachments/assets/9175397c-b6ec-46e8-918f-e7225e8b1904" alt="Good Prediction 1" width="35%" />
  <img src="https://github.com/user-attachments/assets/4f6e04e9-7db2-4918-ad5c-7f6a64f88c69" alt="Good Prediction 2" width="45%" />
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/d1a58206-31b1-41e6-a7dd-6c5b2876136c" alt="Bad Prediction 1" width="45%" />
  <img src="https://github.com/user-attachments/assets/5311f593-27de-490c-abdc-9a799bb6de14" alt="Bad Prediction 2" width="45%" />
</div>

---

### Metrics on the Test and Train Dataset
The following charts summarize the model's performance on the test and train datasets:  

<div align="center">
  <img src="https://github.com/user-attachments/assets/ff725ac3-6da1-449e-ab38-c6e08397dac6" alt="Metrics Chart 1" width="45%" />
  <img src="https://github.com/user-attachments/assets/d7cd69ea-e5ff-4538-a12f-afd733379ace" alt="Metrics Chart 2" width="45%" />
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/856c8011-256c-4e15-9141-805cf4cc5df4" alt="Metrics Chart 3" width="90%" />
</div>

For the test dataset, the model detected:
- 36 out of 36 freestanding pools
- 0 out of 4 ponds
- 1 out of 2 permanent pools

## Trained model in ONNX ready for `Deepness` plugin
- model uploaded to [PUTCloud](https://chmura.student.put.poznan.pl/s/w30VPTu2DI8VWVD)
- script used to convert the model to ONNX - ONNX_convert.py
- script used to add the metadata to it - metadata.py

## Demo instructions and video
![xd2_QGIS_2025-01-24_15-39-06](https://github.com/user-attachments/assets/b2c32c1d-9191-49b4-bc18-8da398ff1974)

- ortophoto to load in QGIS: 'Poznan 2023 aerial orthophoto high resolution'
- place to zoom: 52.362475, 16.881612

![image](https://github.com/user-attachments/assets/8269b100-6371-4997-9322-10712e8e33e8)


## People

### Annotations & Training Scripts:
__Yerbiff__ - [Github](https://github.com/Yerbiff) (Jarosław Kuźma 147617)

__the_HaUBe__ - [Github](https://github.com/theHaUBe) (Hubert Górecki 147599)

### Annotations:
__JJayU__ - [Github](https://github.com/JJayU) (Jakub Junkiert 147550)

__MaksymilianKlemen__ - [Github](github.com/MaksymilianKlemen) (Maksymilian Klemenczak)
