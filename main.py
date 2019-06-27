import os
import secrets
from PIL import Image
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from fastai.vision import load_learner, open_image

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # max file size 16mb

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image = save_picture(file)
            prediction = classify_image(image)
            return render_template('index.html', image=image, prediction=prediction)
    else:
        return render_template('index.html', image=None, prediction=None)

# register error routes

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

def save_picture(file):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(file.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join('static/', picture_filename)

    output_size = (500, 500)
    i = Image.open(file)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_path

def classify_image(filename):
    learn = load_learner('models')
    img = open_image(filename)
    pred_class, pred_idx, outputs = learn.predict(img)
    if str(pred_class) == 'yang':
        return 'Yang'
    else:
        return 'Not Yang'
