from slackbot.bot import respond_to
from slackbot.bot import default_reply
import datetime

w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']

@respond_to('曜日を教えて')
def show_day(message):
    message.reply("今日は" + w_list[datetime.date.today().weekday()] + "だよ。")

@respond_to('時間を教えて')
def show_date(message):
    message.reply("今日は" + str(datetime.date.today()) + "だよ。")
