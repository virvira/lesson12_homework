import logging

from flask import Blueprint
from flask import Flask, request, render_template, send_from_directory
from utils import add_post

# Cоздаем новый блюпринт, выбираем для него имя

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@loader_blueprint.route('/post')
def page_add_post():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    """ Эта вьюшка обрабатывает форму"""
    # Получаем объект картинки из формы
    picture = request.files.get("picture")
    post_text = request.form.get("content")

    if not picture or not post_text:
        return f"Не загружена картинка или текст"

    if picture.filename.split('.')[-1] not in ('jpeg', 'jpg', 'png'):
        logging.info('Некорректное расширение файла')
        return 'Некорректное расширение файла'

    try:
        # Получаем имя файла у загруженного файла
        filename = picture.filename
        path = f"./uploads/images/{filename}"
        # Сохраняем картинку под родным именем в папку uploads/images
        picture.save(path)
        picture_path = '/' + path
    except FileNotFoundError:
        logging.error('Ошибка при загрузке файла')
        return 'Файл не найден'

    post = add_post({'pic': picture_path, 'content': post_text})

    return render_template('post_uploaded.html', post=post)

