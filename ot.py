import random
import time
import telebot
import requests
from telebot import types

#ДАННЫЕ, КОТОРЫЕ НУЖНО МЕНЯТЬ
bot = telebot.TeleBot('1674804600:AAHOMUH7S40k8d339xBEDXahvZDd8G7sLYE') #токен из @botfather

manager = 'https://t.me/MafiaBoss123'                           #телеграм менеджера
qiwi_numb = '+ххх'                         #номер киви
yandex_numb = 'ххх'                     #номер яндекс
card_numb = 'хххх хххх хххх хххх'                   #номер карты
btc_numb = 'ххх'     #btc кошелек

markdown = """
    *bold text*
    _italic text_
    [text](URL)
    """

#KEYBOARDS
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Доступ в приват')
keyboard1.row('Горячие архивы')
keyboard1.row('Тех. поддержка 👨🏻‍💻')

deliveryClub = telebot.types.ReplyKeyboardMarkup(True)
deliveryClub.row('🔄 Проверить оплату')
deliveryClub.row('❌Отменить действие❌')

yandexEat = telebot.types.ReplyKeyboardMarkup(True)
yandexEat.row('❤100 RUB(5 видео)❤', '💥150 RUB(8 видео)💥')
yandexEat.row('🔥200 RUB(13 видео)🔥', '👑300 RUB(20+ видео)👑')
yandexEat.row('❌Отменить действие❌')

keyboard_check = telebot.types.ReplyKeyboardMarkup(True)
keyboard_check.row('🔄 Проверить оплату', '❌ Отменить платеж')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '''📹 Продажа самых горячих запретных видео 📹
                                     \n😏 Сотни довольных пользователей 😏
                                     \n🗃  Архивы разбиты по категориям! 🗃
                                     \n🔥 Приватка и все архивы обновляются ежедневно!🔥
                                     \n💯На сегодня действуют скидки на большие архивы💯
                                     \n💯Успей ухватить!💯
                                     \n🕔 Тех. поддержка и бот работает 24/7 🕔
                                     \n🔥 Для тебя найдется все что угодно) 🔥''', reply_markup=keyboard1, parse_mode= "Markdown")
@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == 'Доступ в приват':
        bot.send_message(message.chat.id, '🔥🕔 Новые видео КАЖДЫЙ ЧАС! 🕔🔥\n🔥 Доступ навсегда! 🔥\nПеред оплатой сохраните 5-значный код\nВ случае ошибки тех.поддержке будет легче вам помочь\nВаша ссылка на оплату:\nhttps://oplata.qiwi.com/form?invoiceUid=67141e49-44c5-427d-a63a-fd2fdd64ec8d', reply_markup=deliveryClub)
    elif message.text == 'Горячие архивы':
        bot.send_message(message.chat.id, '📹 Выберите один из доступных архивов 📹\n💵 Сумма указана уже с учетом скидки 💵\n🔥 -50 RUB для каждого из архива! 🔥', reply_markup=yandexEat)
    elif message.text == '❤100 RUB(5 видео)❤':
        bot.send_message(message.chat.id, '📹 Вы выбрали архив на 5 видео 📹\nВаша ссылка на оплату:\nhttps://oplata.qiwi.com/form?invoiceUid=6d82965d-0477-4c19-8bfa-3006c7eca22d', reply_markup=keyboard_check)
    elif message.text == '💥150 RUB(8 видео)💥':
        bot.send_message(message.chat.id, '📹 Вы выбрали архив на 8 видео 📹\nВаша ссылка на оплату:\nhttps://oplata.qiwi.com/form?invoiceUid=7b8740ec-ae68-405f-ba29-402c0ddf09ea', reply_markup=keyboard_check)
    elif message.text == '🔥200 RUB(13 видео)🔥':
        bot.send_message(message.chat.id, '📹 Вы выбрали архив на 13 видео 📹\nВаша ссылка на оплату:\nhttps://oplata.qiwi.com/form?invoiceUid=fb5f5969-d538-46cf-a0ef-2169cedc013f', reply_markup=keyboard_check)
    elif message.text == '👑300 RUB(20+ видео)👑':
        bot.send_message(message.chat.id, '📹 Вы выбрали архив на 20+ видео 📹\nВаша ссылка на оплату:\nhttps://oplata.qiwi.com/form?invoiceUid=5d7257e2-22ea-4399-b398-dc5e5ef1113f', reply_markup=keyboard_check)
    elif message.text == '🔄 Проверить оплату':
        bot.send_message(message.chat.id, '🔎 Поиск платежа . . .', parse_mode= "Markdown")
        time.sleep(3)
        bot.send_message(message.chat.id, '🚫 *Платеж не был найден*', parse_mode= "Markdown")
        bot.delete_message(message.chat.id, message.message_id +1,)
    elif message.text == '❌ Отменить платеж':
        bot.send_message(message.chat.id, '❌ Платеж отменен', parse_mode='Markdown', reply_markup=keyboard1)
    elif message.text == 'Тех. поддержка 👨🏻‍💻':
        bot.send_message(message.chat.id, 'У Вас возникла проблема⁉️\nОбратитесь в телеграм канал тех. поддержки 👨🏻‍💻:\nhttps://t.me/MafiaBoss123', parse_mode='Markdown', reply_markup=keyboard1)
    elif message.text == '❌Отменить действие❌':
        bot.send_message(message.chat.id, '''📹 Продажа самых горячих запретных видео 📹
                                     \n😏 Сотни довольных пользователей 😏
                                     \n🗃  Архивы разбиты по категориям! 🗃
                                     \n🔥 Приватка и все архивы обновляются ежедневно!🔥
                                     \n💯На сегодня действуют скидки на большие архивы💯
                                     \n💯Успей ухватить!💯
                                     \n🕔 Тех. поддержка и бот работает 24/7 🕔
                                     \n🔥 Для тебя найдется все что угодно) 🔥''', reply_markup=keyboard1, parse_mode= "Markdown")
    else: bot.send_message(message.chat.id, 'Бот не отвечает на обычные сообщения', reply_markup=keyboard1)    

bot.polling()

