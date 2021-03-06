FROM python:3.9-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
EXPOSE 5000
