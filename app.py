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
    elif event.message.text.casefold() == "mau gacha":
        message = TextSendMessage(text=gacha())
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text.casefold() == "minta top operator":
        message = TextSendMessage(text=gacha6())
        line_bot_api.reply_message(event.reply_token, message)

def gacha6():
	get = random.randint(1,10)
	if get == 10:
		numbr = random.randint(1,11)
		if numbr == 1:
			chara = 'Selamat, Anda mendapatkan Exusiai!'
		elif numbr == 2:
			chara = 'Selamat, Anda mendapatkan Siege!'
		elif numbr == 3:
			chara = 'Selamat, Anda mendapatkan Ifrit!'
		elif numbr == 4:
			chara = 'Selamat, Anda mendapatkan Eyjafjalla!'
		elif numbr == 5:
			chara = 'Selamat, Anda mendapatkan Angelina!'
		elif numbr == 6:
			chara = 'Selamat, Anda mendapatkan Shining!'
		elif numbr == 7:
			chara = 'Selamat, Anda mendapatkan Nightingale!'
		elif numbr == 8:
			chara = 'Selamat, Anda mendapatkan Hoshiguma!'
		elif numbr == 9:
			chara = 'Selamat, Anda mendapatkan Saria!'
		elif numbr == 10:
			chara = 'Selamat, Anda mendapatkan SilverAsh!'
		elif numbr == 11:
			chara = 'Selamat, Anda mendapatkan Skadi!'
	else:
		chara = 'Maaf sekali, Anda gagal mendapatkan Top Operator.'
		
	return chara
	
def gacha():
	
	rarity = random.randint(1,100)
	if rarity <= 2:
		numbr = random.randint(1,11)
		if numbr == 1:
			chara = 'Exusiai'
		elif numbr == 2:
			chara = 'Siege'
		elif numbr == 3:
			chara = 'Ifrit'
		elif numbr == 4:
			chara = 'Eyjafjalla'
		elif numbr == 5:
			chara = 'Angelina'
		elif numbr == 6:
			chara = 'Shining'
		elif numbr == 7:
			chara = 'Nightingale'
		elif numbr == 8:
			chara = 'Hoshiguma'
		elif numbr == 9:
			chara = 'Saria'
		elif numbr == 10:
			chara = 'SilverAsh'
		elif numbr == 11:
			chara = 'Skadi'
		
	elif rarity <= 10:
		numbr = random.randint(1,26)
		if numbr == 1:
			chara = 'Ptilopsis'
		elif numbr == 2:
			chara = 'Zima'
		elif numbr == 3:
			chara = 'Texas'
		elif numbr == 4:
			chara = 'Franka'
		elif numbr == 5:
			chara = 'Lappland'
		elif numbr == 6:
			chara = 'Specter'
		elif numbr == 7:
			chara = 'Blue Poison'
		elif numbr == 8:
			chara = 'Platinum'
		elif numbr == 9:
			chara = 'Meteorite'
		elif numbr == 10:
			chara = 'Skyfire'
		elif numbr == 11:
			chara = 'Mayer'
		elif numbr == 12:
			chara = 'Silence'
		elif numbr == 13:
			chara = 'Warfarin'
		elif numbr == 14: 
			chara = 'Nearl'
		elif numbr == 15: 
			chara = 'Projekt Red'
		elif numbr == 16: 
			chara = 'Liskarm'
		elif numbr == 17: 
			chara = 'Croissant'
		elif numbr == 18: 
			chara = 'Provence'
		elif numbr == 19: 
			chara = 'Firewatch'
		elif numbr == 20: 
			chara = 'Cliffheart'
		elif numbr == 21: 
			chara = 'Pramanix'
		elif numbr == 22: 
			chara = 'Istina'
		elif numbr == 23: 
			chara = 'Sora'
		elif numbr == 24: 
			chara = 'Manticore'
		elif numbr == 25: 
			chara = 'FEater'
		elif numbr == 26: 
			chara = 'Nightmare'
	elif rarity <= 60:
		numbr = random.randint(1,22)
		if numbr == 1: 
			chara = 'Haze'
		elif numbr == 2: 
			chara = 'Gitano'
		elif numbr == 3: 
			chara = 'Jessica'
		elif numbr == 4: 
			chara = 'Meteor'
		elif numbr == 5:
			chara = 'Shirayuki'
		elif numbr == 6: 
			chara = 'Scavenger'
		elif numbr == 7: 
			chara = 'Vigna'
		elif numbr == 8: 
			chara = 'Dobermann'
		elif numbr == 9: 
			chara = 'Matoimaru'
		elif numbr == 10: 
			chara = 'Frostleaf'
		elif numbr == 11: 
			chara = 'Mousse'
		elif numbr == 12: 
			chara = 'Gravel'
		elif numbr == 13: 
			chara = 'Rope'
		elif numbr == 14:
			chara = 'Myrrh'
		elif numbr == 15: 
			chara = 'Perfurmer'
		elif numbr == 16: 
			chara = 'Matterhorn'
		elif numbr == 17: 
			chara = 'Cuora'
		elif numbr == 18: 
			chara = 'Gummy'
		elif numbr == 19: 
			chara = 'Deepcolor'
		elif numbr == 20: 
			chara = 'Earthspirit'
		elif numbr == 21: 
			chara = 'Shaw'
		elif numbr == 22: 
			chara = 'Beehunter'
	else: 
		numbr = random.randint(1,14)
		if numbr == 1: 
			chara = 'Fang'
		elif numbr == 2: 
			chara = 'Vanilla'
		elif numbr == 3: 
			chara = 'Plume'
		elif numbr == 4: 
			chara = 'Melantha'
		elif numbr == 5: 
			chara = 'Cardigan'
		elif numbr == 6: 
			chara = 'Beagle'
		elif numbr == 7: 
			chara = 'Kroos'
		elif numbr == 8: 
			chara = 'Lava'
		elif numbr == 9: 
			chara = 'Hibiscus'
		elif numbr == 10: 
			chara = 'Ansel'
		elif numbr == 11: 
			chara = 'Steward'
		elif numbr == 12: 
			chara = 'Orchid'
		elif numbr == 13: 
			chara = 'Catapult'
		elif numbr == 14: 
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
