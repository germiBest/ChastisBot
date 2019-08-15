import logging
import tgconfig as cfg
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import telegram
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def add_group(update, context):
    for member in update.message.new_chat_members:
        hello = telegram.Sticker('CAADAgADlwADkAABUCD95Ya3mn-HtgI', 512, 512, thumb=None)
        update.message.reply_sticker(hello)
#def stckr(update, context):
#    print(update.message.sticker)
#    hello = telegram.Sticker('CAADAgADlwADkAABUCD95Ya3mn-HtgI', 512, 512, thumb=None)
#    update.message.reply_sticker(hello)
def main():

    """Start the bot."""

    updater = Updater(cfg.api_token, use_context=True)

    dp = updater.dispatcher

    add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
    dp.add_handler(add_group_handle)
    #dp.add_handler(MessageHandler(Filters.sticker, stckr))
    #dp.add_handler(CommandHandler("start", start))
    #dp.add_handler(MessageHandler(Filters.photo, imga))
    #dp.add_handler(MessageHandler(Filters.text, urlparse))
    #dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
