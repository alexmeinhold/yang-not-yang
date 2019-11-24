from pathlib import Path

from fastai.vision import download_images, verify_images


categories = ['yang','not_yang']
path = Path('data')

for category in categories:
    destination = path/category
    destination.mkdir(parents=True, exist_ok=True)
    csv_file = category + '.csv'
    download_images(csv_file, destination, max_pics=400)
    verify_images(destination, delete=True, max_size=500)
