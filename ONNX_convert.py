import torch
from ultralytics import YOLO
pt_model_path = f"best.pt"

onnx_model_path = f"best.onnx"

model = YOLO(pt_model_path)
model.export(format="onnx", imgsz=640, opset=12)