# coding=utf-8
from application import bot
from telebot.types import Message

lista=[
    '@AnonymusRiv',
    '@albapj01',
    '@Xxema23',
    '@jes106',
    '@jdes01',
    '@MarcosRigal',
    '@Jimeninho',
    '@rafapeerez',
    '@Silvya292',
    '@Adoen',
    '@Davison27'
]

numero=0


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(commands=['test'])
def test(message):
    bot.reply_to(message, 'Prueba')

@bot.message_handler(func=lambda message: date.is_friday() , content_types=['text'] , commands=['post'])
def post(message):
    if(date.is_friday()):
        numero=numero+1
        if(numero==len(lista)):
            numero=0

        bot.send_message(CHAT_ID, "Esta semana le toca a {lista[numero]}")

    bot.reply_to(message, "Esta semana le toca a {lista[numero]}")

@bot.message_handler(commands=['post'])
def test(message):
    bot.reply_to(message, 'Esta semana le toca a {lista[numero]}')