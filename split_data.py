import os
import random

CATEGORIES = ["yang", "not_yang"]
DATA_DIR = "data"
VAL_PCT = 0.1

val_path = os.path.join(DATA_DIR, "val")
train_path = os.path.join(DATA_DIR, "train")
os.makedirs(val_path, exist_ok=True)
os.makedirs(train_path, exist_ok=True)

for category in CATEGORIES:
    category_path = os.path.join(DATA_DIR, category)
    images = os.listdir(category_path)
    image_count = len(images)
    val_amount = int(image_count * VAL_PCT)
    random.shuffle(images)
    val_images = images[:val_amount]
    train_images = images[val_amount:]
    os.makedirs(os.path.join(val_path, category))
    os.makedirs(os.path.join(train_path, category))

    for image in val_images:
        source_path = os.path.join(category_path, image)
        target_path = os.path.join(val_path, category, image)
        os.rename(source_path, target_path)

    for image in train_images:
        source_path = os.path.join(category_path, image)
        target_path = os.path.join(train_path, category, image)
        os.rename(source_path, target_path)

    os.rmdir(category_path)
