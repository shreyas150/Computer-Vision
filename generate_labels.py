import os
from PIL import Image

def generate_annotations(images_dir, labels_dir, class_id):
    os.makedirs(labels_dir, exist_ok=True)
    
    for root, _, files in os.walk(images_dir):
        for file in files:
            if not file.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue
            class_folder = os.path.basename(root)
            unique_name = f"{class_folder}_{file}"
            txt_file = os.path.splitext(unique_name)[0] + ".txt"
            txt_path = os.path.join(labels_dir, txt_file)
            try:
                with Image.open(os.path.join(root, file)) as img:
                    width, height = img.size
            except Exception as e:
                print(f"Error processing {file}: {e}")
                continue
            with open(txt_path, "w") as f:
                f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")

if __name__ == "__main__":
    generate_annotations("/Users/shreyasmallesh/Wine-Beer-Detection/beer/data/train/beer_bottle", "/Users/shreyasmallesh/Wine-Beer-Detection/data/labels/train", 0)
    generate_annotations("/Users/shreyasmallesh/Wine-Beer-Detection/wine/data/train/wine_bottle", "/Users/shreyasmallesh/Wine-Beer-Detection/data/labels/train", 1)
    generate_annotations("/Users/shreyasmallesh/Wine-Beer-Detection/beer/data/val/beer_bottle", "/Users/shreyasmallesh/Wine-Beer-Detection/data/labels/val", 0)
    generate_annotations("/Users/shreyasmallesh/Wine-Beer-Detection/wine/data/val/wine_bottle", "/Users/shreyasmallesh/Wine-Beer-Detection/data/labels/val", 1)
