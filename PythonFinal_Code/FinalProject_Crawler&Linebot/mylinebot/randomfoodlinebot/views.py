from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from .randomcrawl import Randomcrawlrestaurant

import schedule

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

'''
# 未來可開發方向，依照傳入訊息回覆
# 可以讓使用者輸入所在地區、食物喜好種類等等

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                getfood = Randomcrawlrestaurant()
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text='仍在開發測試中...敬請期待^^' + \
                                    '\n' + getfood.crawlrestaurant())

                    # TextSendMessage(text=event.message.text)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
'''


def morningontimemessage():
    getfoodontime = Randomcrawlrestaurant()
    line_bot_api.broadcast(TextSendMessage(
        text="早安!起床囉!" + '\n' + "這是每日早上7:30定時播送, 現在正在測試中...敬請期待^^" +
             '\n' + getfoodontime.crawlrestaurant()))


def noonontimemessage():
    getfoodontime = Randomcrawlrestaurant()
    line_bot_api.broadcast(TextSendMessage(
        text="午安!今天過一半了喔!" + '\n' + "這是每日中午11:30定時播送, 現在正在測試中...敬請期待^^" +
        '\n' + getfoodontime.crawlrestaurant()))


def eveningontimemessage():
    getfoodontime = Randomcrawlrestaurant()
    line_bot_api.broadcast(TextSendMessage(
        text="該吃晚餐囉!" + '\n' + "這是每日晚上19:00定時播送, 現在正在測試中...敬請期待^^" +
        '\n' + getfoodontime.crawlrestaurant()))


schedule.every().day.at("07:30").do(morningontimemessage)
schedule.every().day.at("11:30").do(noonontimemessage)
schedule.every().day.at("19:00").do(eveningontimemessage)
# 測試用
# schedule.every(30).seconds.do(ontimemessage)

while True:
    schedule.run_pending()
