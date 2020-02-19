from flask import Flask, request, abort, jsonify

import random
import json
import requests

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('jt2iNSpQg8C5pgQmQ6tHloSdJsfH7ivb+F1Kg2KVBhGFCRshYipt1YXJChz25QHUJhtuS+PYkp/zUmjm49EzVK1fTqWpj3b2r2HaD9QEr3vwvNp1sXKHIbzGdhHE2ZF62YNjMOQXUMOp9eW/lYf4/AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('312f45a27b528b4177855ce00573a699')

# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #message = TextSendMessage(text=event.message.text)
    #line_bot_api.reply_message(event.reply_token, message)
    if event.message.text.casefold() == "minta operator":
        line_bot_api.reply_message(event.reply_token, colong())

def colong():

    status = True

    while status:
        poin = random.randint(1,50000)
        link = "http://safebooru.org/index.php?page=dapi&s=post&q=index&pid=" + str(poin) + "&limit=1&json=1&tags=arknights"
        res = requests.get(link)


        if res.json()[0]['sample'] == False:
            ori = "https://safebooru.org/images/" + res.json()[0]['directory'] + "/" + res.json()[0]['image']
        else:
            ori = "https://safebooru.org/samples/" + res.json()[0]['directory'] + "/sample_" + res.json()[0]['image']


        pre = "https://safebooru.org/thumbnails/" + res.json()[0]['directory'] + "/thumbnail_" + res.json()[0]['image']

        orires = requests.get(ori)
        preres = requests.get(pre)

        if orires.status_code == 200:
            if preres.status_code == 200:
                status = False


    message = ImageSendMessage(original_content_url = ori ,preview_image_url = pre)
    print(message)
    print(poin)
    return message
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
