import vk_api
import random
from MainFile import *
from other import *
from vk_api import *

tanks = ['https://vk.com/album-169747041_270881984?z=photo-169747041_457239017%2Falbum-169747041_270881984',
         'https://vk.com/album-169747041_270881984?z=photo-169747041_457239018%2Falbum-169747041_270881984']
attachments = []
anime = ['Танки', 'Убийца Акаме']
Anime = ''


def Random():
    global Anime
    Anime = random.choice(anime)


def RandomAnime():
    global Anime
    Random()
    if Anime == 'Танки':
        upload = VkUpload(token)
        image_url = random.choice(tanks)
        image = token.get(image_url, stream=True)
        photo = upload.photo_messages(photos=image.raw)[0]
        attachments.append(
            'photo{}_{}'.format(photo['owner_id'], photo['id'])
        )
        vk.messages.send(
            user_id=event.user_id,
            attachment=','.join(attachments),
            message='Держи'
        )
    else:
        vk.messages.send(
            user_id=event.user_id,
            message='Нет фотки'
        )