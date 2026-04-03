import numpy as np
from PIL import Image
import os
import json
from tqdm import tqdm

def generate_training_baseline(train_dir):
    stats = {
        "brightness": [],
        "contrast": [],
        "r_mean": [], "g_mean": [], "b_mean": []
    }
    
    # Check if directory exists
    if not os.path.exists(train_dir):
        print(f"❌ Error: The directory '{train_dir}' was not found.")
        return None

    print(f"Reading training data from: {train_dir}")
    
    # os.walk will automatically go into:
    # Root -> Subfolder -> 10 Class Folders
    for root, dirs, files in os.walk(train_dir):
        # Using tqdm on files so you see progress per folder
        for file in tqdm(files, desc=f"Processing {os.path.basename(root)}", leave=False):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                try:
                    img_path = os.path.join(root, file)
                    img = Image.open(img_path).convert("RGB")
                    arr = np.array(img)
                    
                    # Calculate metrics
                    stats["brightness"].append(np.mean(arr))
                    stats["contrast"].append(np.std(arr))
                    stats["r_mean"].append(np.mean(arr[:,:,0]))
                    stats["g_mean"].append(np.mean(arr[:,:,1]))
                    stats["b_mean"].append(np.mean(arr[:,:,2]))
                except Exception as e:
                    print(f"Skipping corrupt image {file}: {e}")

    # Calculate final averages
    if not stats["brightness"]:
        print("⚠️ No images found! Check your folder path.")
        return None

    baseline = {
        "mean_brightness": float(np.mean(stats["brightness"])),
        "mean_contrast": float(np.mean(stats["contrast"])),
        "mean_r": float(np.mean(stats["r_mean"])),
        "mean_g": float(np.mean(stats["g_mean"])),
        "mean_b": float(np.mean(stats["b_mean"])),
        "sample_count": len(stats["brightness"])
    }
    
    with open("training_baseline.json", "w") as f:
        json.dump(baseline, f, indent=4)
    
    print("\n✅ training_baseline.json created successfully!")
    return baseline

if __name__ == "__main__":
    # Update this path to your top-level folder
    # Example: "C:/Users/Name/Desktop/Project/Main_Folder"
    DATA_PATH = "split_dataset/train" 
    generate_training_baseline(DATA_PATH)