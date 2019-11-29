import io
import os

import torch
import torch.nn as nn
from flask import Flask
from torchvision import models

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # max file size 16mb
app.config["ALLOWED_EXTENSIONS"] = set(["png", "jpg", "jpeg"])
app.config["CLASSES"] = ["not_yang", "yang"]

model = models.resnet18(pretrained=True)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)
model.load_state_dict(torch.load("models/model.pth"))
model.eval()

from app import routes
