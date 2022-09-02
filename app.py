import logging

from flask import Flask, request, render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
from utils import get_posts_by_word, load_posts


UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# Добавили файл, в который пишем логи
logging.basicConfig(filename="basic.log", level=logging.INFO)

app.run(port=5001)

