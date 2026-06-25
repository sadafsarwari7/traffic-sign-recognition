import os
import matplotlib.pyplot as plt
from PIL import Image

train_path = "data/Train"

# Ignore hidden files
folders = [f for f in os.listdir(train_path) if not f.startswith(".")]

# Sort folders
folders = sorted(folders, key=int)

# Select the first class
first_class = folders[0]

class_path = os.path.join(train_path, first_class)

# Get images
images = [img for img in os.listdir(class_path) if not img.startswith(".")]

# Display 6 images
plt.figure(figsize=(10, 6))

for i in range(6):

    image_path = os.path.join(class_path, images[i])

    image = Image.open(image_path)

    plt.subplot(2, 3, i + 1)
    plt.imshow(image)
    plt.axis("off")

plt.suptitle(f"Traffic Sign Class: {first_class}")

plt.show()