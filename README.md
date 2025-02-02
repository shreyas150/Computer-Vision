# Computer-Vision

# Wine and Beer Bottle Classification with YOLOv5n

This uses YOLOv5n to detect and classify wine and beer bottles in images. The dataset is enhanced with preprocessing, and the model is trained to recognize two classes: `beer` and `wine`.

---

## Dataset

- **Images**: JPG files of wine and beer bottles.
- **Labels**: TXT files in YOLO format (`<class_id> <x_center> <y_center> <width> <height>`).

Annotations were generated using `generate_labels.py`.

## Enhancements

**Image Enhancement**:
 - Resized images to 640x640 pixels using `enhance_images.py`.

 ## Training

- Trained the YOLOv5n model using `train.py` with 50 epochs and a batch size of 8.
- Used AdamW optimizer for improved training performance.

## Detection

- Detected wine and beer bottles in test images using `detect.py`.
- Visualized results with bounding boxes and class labels.