from application import bot, logger, CHAT_ID


@bot.message_handler(func=lambda message: message.chat.id != int(CHAT_ID))
def detect_valid_group(message):
    logger.info(f"Conexión no válida desde {message.from_user.id}")
    return None
