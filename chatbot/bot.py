# -*- coding: utf-8 -*-
from random import randint
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import vk_api
import logging

try:
    import settings
except ImportError:
    exit('copy settings.py.default into settings.py')

log = logging.getLogger('bot')


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
    stream_handler.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('bot.log', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s, %(levelname)s, %(message)s'))
    file_handler.setLevel(logging.DEBUG)

    log.addHandler(stream_handler)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)


class Bot:
    """
    Eco bot для vk.com
    Use python 3.8
    """
    def __init__(self, group_id, token):
        """

        :param group_id: group id  из группы vk
        :param token: секретнывй токен
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        """
        Запуск бота
        """
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('ошибка в обработке события')

    def on_event(self, event):
        """
        отправляет сообщение отправителю
        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.debug('отвечаем на сообщение')
            self.api.messages.send(message='зря вы сюда написали',
                                   random_id=randint(0, 2 ** 20),
                                   peer_id=event.message.peer_id
                                   )
        else:
            log.info('cant process event like this %s', event.type)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.VK_GROUP_ID, settings.ACCESS_TOKEN)
    bot.run()