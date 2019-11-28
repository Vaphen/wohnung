from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

class TelegramBot:
    updater = None
    chat_id = None

    def __init__(self, token, chat_id):
        self.updater = Updater(token, use_context=True)
        self.chat_id = chat_id
        self.updater.start_polling()

    def send_message_html(self, msg):
        self.updater.job_queue.run_once(lambda ctx: self._send_message(ctx, msg, ParseMode.HTML), 0)

    def repeat_message_html(self, msg_function, interval, first):
        self.updater.job_queue.run_repeating(lambda ctx: self._send_message(ctx, msg_function(), ParseMode.HTML), interval, first)

    def send_photo(self, url):
        self.updater.job_queue.run_once(lambda ctx: self._send_photo(ctx, url), 0)

    def repeat_photo(self, url_function, interval, first):
        self.updater.job_queue.run_repeating(lambda ctx: self._send_photo(ctx, url_function()), interval, first)

    #def repeat_functions(self, functions, interval, first):
    #    self.updater.job_queue.run_repeating(lambda ctx: func() [for func in functions])

    def _send_photo(self, ctx, url):
        if url == None:
            return

        ctx.bot.send_photo(chat_id=self.chat_id, photo=url)

    def _send_message(self, ctx, msg, parse_mode):
        if msg == None:
            return

        ctx.bot.send_message(chat_id=self.chat_id, text=msg, parse_mode=parse_mode)




'''
    def callback_minute(context):
        global latestResult
        global latestPrev
        if latestResult == latestPrev:
            return;

        latestPrev = latestResult;

        context.bot.send_photo(chat_id='206250454', photo=latestPrev[1])
        context.bot.send_message(chat_id='206250454', text=latestPrev[0], parse_mode=ParseMode.HTML)


    def getBotUpdater():
        """Start the bot."""
        # Create the Updater and pass it your bot's token.
        # Make sure to set use_context=True to use the new context based callbacks
        # Post version 12 this will no longer be necessary

        j = updater.job_queue
        j.run_repeating(callback_minute, interval=10, first=0)
        # Get the dispatcher to register handlers
        #dp = updater.dispatcher
        #dp.add_handler(CommandHandler("test", test))

        # on different commands - answer in Telegram
        #dp.add_handler(CommandHandler("start", start))

        return updater
        '''
