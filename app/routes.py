import os

from flask import flash, redirect, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

from app import app, model
from app.inference import get_prediction
from app.utils import allowed_file, save_picture


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
            image_bytes = open(image_path, "rb").read()
            prediction = get_prediction(image_bytes=image_bytes)
            return render_template("index.html", image=filename, prediction=prediction)
    else:
        return render_template("index.html", image=None, prediction=None)


@app.route("/images/<filename>")
def get_image(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
