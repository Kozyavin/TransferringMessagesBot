# подключение библиотек
import telebot
import telethon


import telethon

class TransmittingMessagesBot(telethon.Bot):
    def __init__(self, source_channel, destination_channel):
        self.source_channel = '@edo_diadocsource_channel'
        self.destination_channel = '@KonturDiadocNewsBot'

    def start_bot(self):
        bot = telethon.Bot(token='6969275970:AAFnV5gAzM4CUKjlR7wg2GqlpSh5JiFlQ10N')
        bot.send_message(chat_id=self.source_channel, message='/start', chat_id=self.destination_channel)

if __name__ == '__main__':
    TransmittingMessagesBot()