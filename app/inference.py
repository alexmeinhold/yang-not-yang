from app import app, model
from app.utils import transform_image


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = y_hat.item()
    prediction = app.config["CLASSES"][predicted_idx]
    if prediction == "yang":
        return "Yang"
    else:
        return "Not Yang"
