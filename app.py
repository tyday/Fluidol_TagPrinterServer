from flask import Flask, flash, jsonify, render_template, request, redirect, url_for
from celery import Celery
import random, time

from tag_printer_settings import TAG_DEFINITIONS, TAG_TYPES

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config['SECRET_KEY']

# Set up celery client
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')