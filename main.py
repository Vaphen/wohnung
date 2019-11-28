import schedule
import time
import os
from telegrambot import TelegramBot
from meine_stadt import MeineStadt, MeineStadtResult

lastVal = MeineStadtResult(None, None, None)
def notify_meine_stadt_news():
    global lastVal
    meineStadtResult = MeineStadt.receive_meine_stadt_result()
    if lastVal.plain == meineStadtResult.plain:
        print("Nothing new...")
        return

    telegram_secret = os.environ["TELEGRAM_SECRET"]
    channel_id = os.environ["CHANNEL_ID"]
    print("Secret: %s" % telegram_secret)
    print("Channel: %s" % channel_id)

    bot = TelegramBot("862350645:AAG9HcakMPX8MF6FWKjKcpFAnjyNRBTmdyo", "206250454")

    try:
        if meineStadtResult.image_url != None:
            bot.send_photo(meineStadtResult.image_url)
    except:
        print("Sending Image failed: %s" % meineStadtResult.image_url)

    try:
        if meineStadtResult.html_formatted != None:
            bot.send_message_html(meineStadtResult.html_formatted)
    except:
        print("Sending message failed: %s" % meineStadtResult.html_formatted)

    lastVal = meineStadtResult


if __name__ == "__main__":

    schedule.every(60).seconds.do(notify_meine_stadt_news)
    while True:
        #try:
        schedule.run_pending()
        #except:
       #$ print("An unknown error occured.")
