# подключение библиотек
import telethon
TOKEN = '7582577059:AAGllhSZSyezkoY3VInyI4WCTmuf4YvZrvM'


class NewsForwarderBot(telethon.Bot):
    def forward_news(self, @edo_diadoc, @KonturDiadocNewsBot, message):
        api = telethon.Client()
        api.send_message(chat_id=@edo_diadoc, message=message, chat_id=@KonturDiadocNewsBot)
