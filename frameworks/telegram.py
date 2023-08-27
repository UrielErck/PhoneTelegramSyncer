def sendcommand(icon, text) -> bool:
    from pytgbot import Bot
    from frameworks.ConfigReaderFile import readconfig as rc
    data = rc().get('MVARIABLE')

    API_KEY = data.get('API')  # change this to the token you get from @BotFather
    CHAT = data.get('CLIENT')  # can be a @username or a id, change this to your own @username or id for example.

    bot = Bot(API_KEY)
    botname = bot.get_me()
    # sending messages:
    bot.send_message(CHAT, f'[(name:{botname.first_name}):(do:{text})]:(id:{botname.id})')
    if rc().get('VARIABLE').get('NOTIF') == 1:
        icon.notify(str(text))
    return True
