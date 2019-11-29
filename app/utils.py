import io
import os

import torchvision.transforms as transforms
from PIL import Image

from app import app


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


def save_picture(file, filename):
    upload_folder = os.path.join("app", app.config["UPLOAD_FOLDER"])
    os.makedirs(upload_folder, exist_ok=True)
    image_path = os.path.join(upload_folder, filename)
    output_size = (500, 500)
    image = Image.open(file)
    image.thumbnail(output_size)
    rgb_image = image.convert("RGB")
    rgb_image.save(image_path)
    return image_path


def transform_image(image_bytes):
    my_transforms = transforms.Compose(
        [
            transforms.Resize(255),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)
