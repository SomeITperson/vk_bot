import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
import random
from difflib import SequenceMatcher
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = "460ebb6753f53e86f4a1a083a81cb3e99b43f4e48cb8e4b06ac7752f4c42a19a91a288e63fd977333b7cd"
vk_session = vk_api.VkApi(token=token)

"""
event.type-проверка событий на VkEventType.MESSAGE_NEW(новое сообщение)
event.to_me-проверка сообщения, адресовано ли оно боту
event.user_id-получение id пользователя из события
event.text-получение текста от пользователя
"""

phrazes = {
    "привет" : {"Привет!", "Здравствуй!", "Приветствую!"},
    "как дела?" : {"Отлично!", "Класс!", "Как вы пришли, стали лучше)"},
    "что делаешь?" : {"Чищу микросхемы)", "Заряжаюсь)", "Ловлю электрическую волну)"},
}

class Bot():
    def get_answer(self):
        word = []
        msg = event.text.lower()
        for i, j in phrazes.items():
            value = SequenceMatcher(None, msg, i).ratio()
            if value >= 0.6:
                for mean in j:
                    word.append(mean)
                random_answer = random.choice(word)
                return random_answer
        dictionary_error = "Я такого не знаю"
        return dictionary_error

    def get_user_id(self):
        user_id = event.user_id
        return user_id

    def send_msg(self, user_id, message):
        vk_session.method("messages.send", {
            "user_id" : user_id,
            "message" : message,
            "random_id" : 0,
        })

for event in VkLongPoll(vk_session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id_get = Bot().get_user_id()
        msg_answer = Bot().get_answer()
        send_msg = Bot().send_msg(user_id_get, msg_answer)