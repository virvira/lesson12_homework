import json


def load_posts():
    '''Загружает данные из файла, возвращает список постов'''
    with open('posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_posts_by_word(word):
    '''Ищет посты, которые содержат переданное слово'''
    posts_list = load_posts()
    searched_posts = []
    for post in posts_list:
        if word in post['content']:
            searched_posts.append(post)
    return searched_posts


def add_post(post):
    '''Добавляет пост'''
    posts = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)

    return post