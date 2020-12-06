import os
import shutil

import requests
from PIL import Image


def download_images(urls_file, destination):
    os.makedirs(destination, exist_ok=True)
    with open(urls_file) as f:
        for index, url in enumerate(f):
            try:
                response = requests.get(url, stream=True)
                with open(f"{destination}/{index}.jpg", "wb") as out_file:
                    shutil.copyfileobj(response.raw, out_file)
            except Exception as e:
                print(str(e))


def verify_images(directory):
    for image in os.listdir(directory):
        img_path = os.path.join(directory, image)
        try:
            img = Image.open(img_path)
            img.verify()
        except (IOError, SyntaxError) as e:
            os.remove(img_path)


CATEGORIES = ["yang", "not_yang"]
PATH = "data"

for category in CATEGORIES:
    destination = os.path.join(PATH, category)
    download_images(category + ".txt", destination)
    verify_images(destination)
