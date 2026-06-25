import os
import numpy as np
from PIL import Image

# =========================
# PATH SETUP
# =========================
train_path = "data/Train"

# =========================
# GET CLASS FOLDERS
# =========================
folders = [
    folder
    for folder in os.listdir(train_path)
    if not folder.startswith(".")
]

folders = sorted(folders, key=int)

print("Number of classes:", len(folders))
print("First 5 classes:", folders[:5])


# =========================
# PREPROCESS FUNCTION
# =========================
def preprocess_image(image_path):

    image = Image.open(image_path)
    image = image.resize((30, 30))
    image = np.array(image)
    image = image / 255.0

    return image


# =========================
# BUILD DATASET
# =========================
X = []
y = []

for label in folders:

    class_path = os.path.join(train_path, label)

    # ensure it's a valid folder
    if not os.path.isdir(class_path):
        continue

    image_files = [
        img for img in os.listdir(class_path)
        if img.endswith(".png") or img.endswith(".jpg")
    ]

    for image_file in image_files:

        image_path = os.path.join(class_path, image_file)

        try:
            image = preprocess_image(image_path)

            X.append(image)
            y.append(int(label))

        except Exception as e:
            print("Skipping:", image_path, "Error:", e)


# =========================
# CONVERT TO NUMPY ARRAYS
# =========================
X = np.array(X)
y = np.array(y)

print("\nDATASET LOADED SUCCESSFULLY 🚀")
print("X shape:", X.shape)
print("y shape:", y.shape)