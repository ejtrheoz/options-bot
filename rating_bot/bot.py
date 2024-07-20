import telebot
import config
import database
import time

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['dkjfhasdkjvbdskjvnbsfvjkbfabjkvakjvbkjvfjbvfjvfj'])
def handle_command(message):
    if message.chat.id in [660343101, 975336105, 6990446751]:

        data = message.text.split('\n')
        try:
            database.new_record(data[1], int(data[2]), int(data[3]), data[4], data[5])
        except:
            bot.send_message(message.chat.id,  'Ошибка записи')
        else:
            bot.send_message(message.chat.id, "Успешная запись")

        
@bot.message_handler(commands=['top'])
def handle_command(message):
    text = "⚡️TOP TRADERS BY ALL TIME\n\n"
    data = database.get_global_top()

    text += f"🏆{data[0][0][1:]}\n\n"

    for i in data:
        if i[-1] == 1:
            text += f'🥇 {i[0][1:]} - '
        elif i[-1] == 2:
            text += f'🥈 {i[0][1:]} - '
        elif i[-1] == 3:
            text += f'🥉 {i[0][1:]} - '
        else:
            text += f'⚡️{i[-1]} {i[0][1:]} - '
        

        text += f'{i[2]} RUB - {i[1]} - профитов\n'
    
    photo = open("main.jpg", "rb")
    bot.send_photo(message.chat.id, photo, caption=text)
    photo.close()

    time.sleep(3)
    bot.delete_message(message.chat.id, message.message_id)

        
@bot.message_handler(commands=['mytop'])
def handle_command(message):
    data = database.get_stat_per_user('@' + message.from_user.username)

    print(data)
    if data == [] or data is None:
        bot.send_message(message.chat.id, "You haven't had any profits")
    else:
        text = f"""💸Number of Profits: {data[2]}
📶Rank: {data[-1]}
💰Profit for all time: {data[1]} USD
💰Profit for the month: {data[4]} USD
💰Profit for the week: {data[6]} USD
"""
        photo = open("main.jpg", "rb")
        bot.send_photo(message.chat.id, photo, caption=text)
        photo.close()

    time.sleep(3)
    bot.delete_message(message.chat.id, message.message_id)
    







if __name__ == "__main__":
    bot.infinity_polling()