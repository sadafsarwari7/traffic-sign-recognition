import os

train_path = "data/Train"

folders = os.listdir(train_path)

# Remove hidden files
folders = [folder for folder in folders if not folder.startswith(".")]

print(f"Number of classes: {len(folders)}")

print("First 5 classes:")

for folder in folders[:5]:
    print(folder)