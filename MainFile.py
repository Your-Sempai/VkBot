import vk_api
import requests
from RandomAnime import *
from other import *
from vk_api.longpoll import *
from vk_api import *


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "АР":
                RandomAnime()
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")
