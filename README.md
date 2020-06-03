# Yang-not-Yang Image Classifier
Image classifier to determine whether Andrew Yang is in a given image or not.\
Inspired by HBO Silicon Valley's hotdog/not-hotdog classifier.

## Installation
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Run locally
```bash
export FLASK_APP=main.py
export FLASK_DEBUG=true
flask run
```

## Train Model
```bash
python download_data.py
python split_data.py
python model.py
```

## Deploy
```bash
docker build -t yangnotyang .
docker run -p 80:5000 -d --restart unless-stopped yangnotyang
```

![](screenshot.png)
