# Yang-not-Yang Image Classifier
Image Classifier to determine whether Andrew Yang is in a given image

## Installation
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
export FLASK_APP=main.py
export FLASK_DEBUG=true
flask run
```

## Train Model
```bash
python download_data.py
python model.py
```

![](screenshot.png)
