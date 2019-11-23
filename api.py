# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging
import random

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)

aneks = open('proved.txt').read().split('\n\n')
not_found = ['Друуузья, не очень вас понял, к сожалению...', 'Я глуховат, повторите...',  'Что?']


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])

def main():
# Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )

# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:

        res['response']['text'] = 'Добрый вечер!'
        return
    else:
        # Обрабатываем ответ пользователя.
        text = req['request']['original_utterance']
        if 'трави' in text or 'анек' in text:
            res['response']['text'] = random.choice(aneks)
            return
        if 'как сделать' in text:
            res['response']['text'] = "Посмотри на гикклассе"
            return
        if 'не работает' in text:
            res['response']['text'] = "Попробуй выключить и включить"
            return
        if 'свин' in text or 'поросенок' in text:
            res['response']['text'] = "Свинья - офигенная тема!"
            return
        if 'свин' in text or 'поросенок' in text:
            res['response']['text'] = "Свинья - офигенная тема!"
            return
        # Если нет, то убеждаем его купить слона!
        res['response']['text'] = random.choice(not_found)

app.run(debug=False, host='0.0.0.0', port=5000, ssl_context='adhoc')