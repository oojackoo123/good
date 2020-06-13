# -*- coding: utf-8 -*-
from flask import Flask, request, abort
import schedule
import time

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel access token (long-lived)
line_bot_api = LineBotApi('')


# Channel secret 
handler = WebhookHandler('')

userID = ''


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

def get_time():
	from datetime import datetime 
	now_time = datetime.now().strftime('%Y-%m-%d %H:%M')
	message = TextSendMessage( now_time )
	line_bot_api.push_message(userID, message)

# write schedule here
```

```


# 無窮迴圈
while True: 
    schedule.run_pending()
    time.sleep(1)


#