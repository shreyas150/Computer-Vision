import os
from yolov5 import train

def main():
    data_yaml = "data.yaml"
    model_config = "models/yolov5n.yaml"
    weights = "yolov5n.pt"
    img_size = 640
    batch_size = 8
    epochs = 50
    device = "cpu"
    
    train.run(
        data=data_yaml,
        cfg=model_config,
        weights=weights,
        imgsz=img_size,
        batch_size=batch_size,
        epochs=epochs,
        device=device,
        optimizer="AdamW"
    )

if __name__ == "__main__":
    main()