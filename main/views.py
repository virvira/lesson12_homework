import logging
from json import JSONDecodeError
from flask import Blueprint
from flask import Flask, request, render_template
from utils import get_posts_by_word

# Cоздаем новый блюпринт, выбираем для него имя
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# Создаем вьюшки, используя в декораторе блюпринт вместо app
@main_blueprint.route('/')
def page_index():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_result():
    s = request.args.get('s', '')
    logging.info("Страница с результатами поиска")
    try:
        res = get_posts_by_word(s)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Не удалось преобразовать'
    return render_template('post_list.html', res=res, s=s)
