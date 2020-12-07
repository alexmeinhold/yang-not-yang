# Yang-not-Yang Image Classifier
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-OEDTq5f968CaJBFfOMJJ-80YWs9C8ND?usp=sharing)

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
FLASK_APP=app/ flask run
```

## Deploy
```bash
docker build -t yangnotyang .
docker run -p 80:5000 -d --restart unless-stopped yangnotyang
```
