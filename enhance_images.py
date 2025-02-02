import os
from PIL import Image, ImageEnhance, ImageFilter
import shutil

def enhance_dataset(input_dir, output_dir, target_size=640):
    os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels'), exist_ok=True)

    for root, _, files in os.walk(os.path.join(input_dir, 'images')):
        for file in files:
            if not file.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue

            img_path = os.path.join(root, file)
            try:
                with Image.open(img_path) as img:
                    img = img.resize((target_size, target_size))
                    output_img_path = os.path.join(output_dir, 'images', file)
                    img.save(output_img_path)

                    enhanced_images = []
                    enhanced_images.append(("flipped_horizontal", img.transpose(Image.FLIP_LEFT_RIGHT)))
                    enhanced_images.append(("flipped_vertical", img.transpose(Image.FLIP_TOP_BOTTOM)))
                    enhanced_images.append(("sharpened", img.filter(ImageFilter.SHARPEN)))
                    enhanced_images.append(("contrasted", ImageEnhance.Contrast(img).enhance(1.5)))
                    enhanced_images.append(("brightened", ImageEnhance.Brightness(img).enhance(1.2)))
                    enhanced_images.append(("blurred", img.filter(ImageFilter.GaussianBlur(radius=1))))

                    for suffix, enhanced_img in enhanced_images:
                        enhanced_file = f"{os.path.splitext(file)[0]}_{suffix}{os.path.splitext(file)[1]}"
                        enhanced_img_path = os.path.join(output_dir, 'images', enhanced_file)
                        enhanced_img.save(enhanced_img_path)

            except Exception as e:
                print(f"Error processing {file}: {e}")
                continue

            label_file = os.path.splitext(file)[0] + ".txt"
            original_label_path = os.path.join(input_dir, 'labels', label_file)
            new_label_path = os.path.join(output_dir, 'labels', label_file)

            if os.path.exists(original_label_path):
                shutil.copy(original_label_path, new_label_path)

                for suffix, _ in enhanced_images:
                    enhanced_label_file = f"{os.path.splitext(label_file)[0]}_{suffix}.txt"
                    enhanced_label_path = os.path.join(output_dir, 'labels', enhanced_label_file)
                    shutil.copy(original_label_path, enhanced_label_path)
            else:
                print(f"Missing annotation for {file}")

if __name__ == "__main__":
    enhance_dataset(
        input_dir="data/train",
        output_dir="data/enhanced/train",
        target_size=640
    )

    enhance_dataset(
        input_dir="data/val",
        output_dir="data/enhanced/val",
        target_size=640
    )