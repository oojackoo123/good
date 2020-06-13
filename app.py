# -*- coding: utf-8 -*-
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel access token (long-lived)
line_bot_api = LineBotApi('0SKGOAMS2iIokEnkEOoGd8l3gPSTqczICx77AckBV0aUS7SZFGa5NLifXwOmbrMLzR0jNYY2gD1R+t7qztDwyVw9QR1MwdycGtA505C69Jxt+Q1zcGPajNU/3eLJYPxUmcjfGFLO+CLX5wwDSebfCQdB04t89/1O/w1cDnyilFU=')

# Channel secret 
handler = WebhookHandler('266985951cd059799eaadd1d9a8c79d9')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def getNews():
    """
    建立一個抓最新消息的function
    """
    import requests
    import re
    from bs4 import BeautifulSoup

    url = 'https://www.ettoday.net/news/focus/3C%E5%AE%B6%E9%9B%BB/'
    r = requests.get(url)
    reponse = r.text

    url_list = re.findall(r'<h3><a href="/news/[\d]*/[\d]*.htm" .*>.*</a>',reponse)

    soup = BeautifulSoup(url_list[0])
    url = 'https://fashion.ettoday.net/' + soup.find('a')['href']
    title = soup.text


    tmp = title + ': ' +url
    return tmp

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 傳送文字
    if event.message.text == '傳送文字':
        message = TextSendMessage(getNews())
         elif event.message.text == '傳送圖片':
        message = ImageSendMessage(
            original_content_url='https://i.imgur.com/QPJ8A1b.png',
            preview_image_url='https://i.imgur.com/QPJ8A1b.png'
             elif event.message.text == '傳送貼圖':
        message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
    else:
        message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

    
if __name__ == '__main__':
    app.run(debug=True)