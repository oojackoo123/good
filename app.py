# -*- coding: utf-8 -*-
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('266985951cd059799eaadd1d9a8c79d9')
# Channel access token (long-lived)
handler = WebhookHandler('0SKGOAMS2iIokEnkEOoGd8l3gPSTqczICx77AckBV0aUS7SZFGa5NLifXwOmbrMLzR0jNYY2gD1R+t7qztDwyVw9QR1MwdycGtA505C69Jxt+Q1zcGPajNU/3eLJYPxUmcjfGFLO+CLX5wwDSebfCQdB04t89/1O/w1cDnyilFU=')
# Channel secret 



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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

if __name__ == '__main__':
    app.run(debug=True)