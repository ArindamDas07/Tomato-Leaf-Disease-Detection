import os
import shutil
import random

# ===============================
# CONFIG
# ===============================
SOURCE_DIR = "tomato_dataset"          # folder with 10 class subfolders merge dataset
DEST_DIR   = "split_dataset"    # output folder

TRAIN_RATIO = 0.8
VAL_RATIO   = 0.1
TEST_RATIO  = 0.1

assert TRAIN_RATIO + VAL_RATIO + TEST_RATIO == 1.0

random.seed(42)

# ===============================
# CREATE OUTPUT FOLDERS
# ===============================
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(DEST_DIR, split), exist_ok=True)

# ===============================
# SPLIT EACH CLASS
# ===============================
for class_name in os.listdir(SOURCE_DIR):
    class_path = os.path.join(SOURCE_DIR, class_name)
    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    images = [img for img in images if img.lower().endswith(('.jpg', '.png', '.jpeg'))]
    random.shuffle(images)

    total = len(images)
    train_end = int(total * TRAIN_RATIO)
    val_end   = train_end + int(total * VAL_RATIO)

    splits = {
        "train": images[:train_end],
        "val":   images[train_end:val_end],
        "test":  images[val_end:]
    }

    for split, files in splits.items():
        split_class_dir = os.path.join(DEST_DIR, split, class_name)
        os.makedirs(split_class_dir, exist_ok=True)

        for file in files:
            src = os.path.join(class_path, file)
            dst = os.path.join(split_class_dir, file)
            shutil.copy2(src, dst)

    print(f"✅ {class_name}: {total} images → "
          f"{len(splits['train'])} train, "
          f"{len(splits['val'])} val, "
          f"{len(splits['test'])} test")

print("\n🎉 Dataset split completed successfully!")
