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
    else if event.message.text.casefold() == "mau gacha":
		line_bot_api.reply_message(event.reply_token, gacha())

def gacha():
	
	rarity = random.randint(1,100)
	if rarity <= 2:
		numbr = random.randint(1,11)
		if numbr == 1:
			chara = 'Exusiai'
		else if numbr == 2:
			chara = 'Siege'
		else if numbr == 3:
			chara = 'Ifrit'
		else if numbr == 4:
			chara = 'Eyjafjalla'
		else if numbr == 5:
			chara = 'Angelina'
		else if numbr == 6:
			chara = 'Shining'
		else if numbr == 7:
			chara = 'Nightingale'
		else if numbr == 8:
			chara = 'Hoshiguma'
		else if numbr == 9:
			chara = 'Saria'
		else if numbr == 10:
			chara = 'SilverAsh'
		else if numbr == 11:
			chara = 'Skadi'
		
	else if rarity <= 10:
		numbr = random.randint(1,26)
		if numbr == 1:
			chara = 'Ptilopsis'
		else if numbr == 2:
			chara = 'Zima'
		else if numbr == 3:
			chara = 'Texas'
		else if numbr == 4:
			chara = 'Franka'
		else if numbr == 5:
			chara = 'Lappland'
		else if numbr == 6:
			chara = 'Specter'
		else if numbr == 7:
			chara = 'Blue Poison'
		else if numbr == 8:
			chara = 'Platinum'
		else if numbr == 9:
			chara = 'Meteorite'
		else if numbr == 10:
			chara = 'Skyfire'
		else if numbr == 11:
			chara = 'Mayer'
		else if numbr == 12:
			chara = 'Silence'
		else if numbr == 13:
			chara = 'Warfarin'
		else if numbr == 14: 
			chara = 'Nearl'
		else if numbr == 15: 
			chara = 'Projekt Red'
		else if numbr == 16: 
			chara = 'Liskarm'
		else if numbr == 17: 
			chara = 'Croissant'
		else if numbr == 18: 
			chara = 'Provence'
		else if numbr == 19: 
			chara = 'Firewatch'
		else if numbr == 20: 
			chara = 'Cliffheart'
		else if numbr == 21: 
			chara = 'Pramanix'
		else if numbr == 22: 
			chara = 'Istina'
		else if numbr == 23: 
			chara = 'Sora'
		else if numbr == 24: 
			chara = 'Manticore'
		else if numbr == 25: 
			chara = 'FEater'
		else if numbr == 26: 
			chara = 'Nightmare'
	else if rarity <= 60:
		numbr = random.randint(1,22)
		if numbr == 1: 
			chara = 'Haze'
		else if numbr == 2: 
			chara = 'Gitano'
		else if numbr == 3: 
			chara = 'Jessica'
		else if numbr == 4: 
			chara = 'Meteor'
		else if numbr == 5:
			chara = 'Shirayuki'
		else if numbr == 6: 
			chara = 'Scavenger'
		else if numbr == 7: 
			chara = 'Vigna'
		else if numbr == 8: 
			chara = 'Dobermann'
		else if numbr == 9: 
			chara = 'Matoimaru'
		else if numbr == 10: 
			chara = 'Frostleaf'
		else if numbr == 11: 
			chara = 'Mousse'
		else if numbr == 12: 
			chara = 'Gravel'
		else if numbr == 13: 
			chara = 'Rope'
		else if numbr == 14:
			chara = 'Myrrh'
		else if numbr == 15: 
			chara = 'Perfurmer'
		else if numbr == 16: 
			chara = 'Matterhorn'
		else if numbr == 17: 
			chara = 'Cuora'
		else if numbr == 18: 
			chara = 'Gummy'
		else if numbr == 19: 
			chara = 'Deepcolor'
		else if numbr == 20: 
			chara = 'Earthspirit'
		else if numbr == 21: 
			chara = 'Shaw'
		else if numbr == 22: 
			chara = 'Beehunter'
	else: numbr = random.randint(1,14)
		if numbr == 1: 
			chara = 'Fang'
		else if numbr == 2: 
			chara = 'Vanilla'
		else if numbr == 3: 
			chara = 'Plume'
		else if numbr == 4: 
			chara = 'Melantha'
		else if numbr == 5: 
			chara = 'Cardigan'
		else if numbr == 6: 
			chara = 'Beagle'
		else if numbr == 7: 
			chara = 'Kroos'
		else if numbr == 8: 
			chara = 'Lava'
		else if numbr == 9: 
			chara = 'Hibiscus'
		else if numbr == 10: 
			chara = 'Ansel'
		else if numbr == 11: 
			chara = 'Steward'
		else if numbr == 12: 
			chara = 'Orchid'
		else if numbr == 13: 
			chara = 'Catapult'
		else if numbr == 14: 
			chara = 'Midnight'
		
	return chara
	
def colong():

    status = True

    while status:
        poin = random.randint(1,1800)
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
