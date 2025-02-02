import os
from subprocess import run
from yolov5 import train

def run_lama(input_dir, output_dir, mask_dir):
    os.makedirs(output_dir, exist_ok=True)
    for file in os.listdir(input_dir):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, file)
            mask_path = os.path.join(mask_dir, file)
            output_path = os.path.join(output_dir, file)
            run([
                "python", "inference.py", 
                "--indir", img_path, 
                "--maskdir", mask_path, 
                "--outdir", output_path
            ], check=True)

def main():
    input_dir = "data/images"
    mask_dir = "data/masks"
    inpainted_dir = "data/inpainted_images"
    run_lama(input_dir, inpainted_dir, mask_dir)
    train.run(data="data.yaml", cfg="models/yolov5n.yaml", epochs=50, batch_size=8, optimizer="AdamW")

if __name__ == "__main__":
    main()
