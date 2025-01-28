import json
import onnx

model_path = 'best.onnx'
model = onnx.load(model_path)

class_definitions = {
    0: 'free_standing_pool',
    1: 'permanent_pool',
    2: 'pond'
}

def add_metadata(model, key, value):
    metadata_entry = model.metadata_props.add()
    metadata_entry.key = key
    metadata_entry.value = json.dumps(value)

add_metadata(model, 'model_type', 'Detector')
add_metadata(model, 'class_names', class_definitions)
add_metadata(model, 'resolution', 10)
add_metadata(model, 'det_conf', 0.5)
add_metadata(model, 'det_type', 'YOLO_Ultralytics')

output_path = 'model_with_metadata.onnx'
onnx.save(model, output_path)
