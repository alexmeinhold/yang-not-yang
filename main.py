import io
import os

import torch
import torch.nn as nn
import torchvision.transforms as transforms
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from PIL import Image
from torchvision import models
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])
CLASSES = ["not_yang", "yang"]

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # max file size 16mb

model = models.resnet18(pretrained=True)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)
model.load_state_dict(torch.load("model.pth"))
model.eval()


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image_path = save_picture(file, filename)
            image_bytes = open(f"static/{filename}", "rb").read()
            prediction = get_prediction(image_bytes=image_bytes)
            return render_template(
                "index.html", image=image_path, prediction=prediction
            )
    else:
        return render_template("index.html", image=None, prediction=None)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def save_picture(file, filename):
    image_path = os.path.join("static", filename)
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


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = y_hat.item()
    prediction = CLASSES[predicted_idx]
    if prediction == "yang":
        return "Yang"
    else:
        return "Not Yang"
