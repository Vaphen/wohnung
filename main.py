import schedule
import time
import os
from telegrambot import TelegramBot
from meine_stadt import MeineStadt, MeineStadtResult
import socket
import sentry_sdk

bot = TelegramBot("862350645:AAG9HcakMPX8MF6FWKjKcpFAnjyNRBTmdyo", "206250454")s


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

lastVal = MeineStadtResult(None, None, None)
def notify_meine_stadt_news():
    global bot
    global lastVal
    meineStadtResult = MeineStadt.receive_meine_stadt_result()
    if lastVal.plain == meineStadtResult.plain:
        print("Nothing new...")
        return

    telegram_secret = os.environ["TELEGRAM_SECRET"]
    channel_id = os.environ["CHANNEL_ID"]
    print("Secret: %s" % telegram_secret)
    print("Channel: %s" % channel_id)

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
    hostname = socket.gethostname()
    bot.send_message_html("%s: %s" % (hostname, get_ip_address()))  # '192.168.0.110'))
    sentry_sdk.init("https://7451700f8a6847a4a79603c8f4044972@sentry.io/1849793")

    schedule.every(60).seconds.do(notify_meine_stadt_news)
    while True:
        #try:
        schedule.run_pending()
        #except:
       #$ print("An unknown error occured.")
