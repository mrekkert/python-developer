import unittest
from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from vk_api.bot_longpoll import VkBotMessageEvent

from bot import Bot


class MyTestCase(TestCase):
    RAW_EVENT = {
        'type': 'message new',
        'object': {
            'date': 1561873459, 'from_id': 576849345, 'id': 119, 'out': 0, 'peer_id': 576849345, 'text': 'hi',
            'conversation_message_id': 119, 'fwd_messages': [], 'important': False, 'random_id': 0, 'attachments': [],
            'is_hidden': False},
        'group_id': 194944763
    }

    def test_run(self):
        count = 5
        events = [{}] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock
        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call({})
                bot.on_event.call_count == count

    def test_on_event(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)

        send_mock = Mock()

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock

                bot.on_event(event)

        send_mock.assert_called_once_with(
            message=self.RAW_EVENT['object']['text'],
            random_id=ANY,
            peer_id=self.RAW_EVENT['object']['peer_id']
        )


if __name__ == '__main__':
    unittest.main()
