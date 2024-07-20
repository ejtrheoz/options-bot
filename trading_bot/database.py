import sqlite3




def set_FIO(user_id, FIO):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user_data
                    SET FIO = ?
                    WHERE user_id = ?
               """, (FIO, user_id))

    conn.commit()
    conn.close()


def set_email(user_id, email):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user_data
                    SET email = ?
                    WHERE user_id = ?
               """, (email, user_id))

    conn.commit()
    conn.close()


def set_number(user_id, number):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user_data
                    SET number = ?
                    WHERE user_id = ?
               """, (number, user_id))

    conn.commit()
    conn.close()


def set_card(user_id, card):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user_data
                    SET card = ?
                    WHERE user_id = ?
               """, (card, user_id))

    conn.commit()
    conn.close()


def set_country(user_id, country):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user_data
                    SET country = ?
                    WHERE user_id = ?
               """, (country, user_id))

    conn.commit()
    conn.close()


def change_balance(user_id, to_buy):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,))
    balance = float(cursor.fetchone()[6] + to_buy)

    cursor.execute("""UPDATE user_data
                    SET balance = ?
                    WHERE user_id = ?
               """, (balance, user_id))

    conn.commit()
    conn.close()

def change_balance_exact(user_id, balance):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user_data
                    SET balance = ?
                    WHERE user_id = ?
               """, (balance, user_id))


    conn.commit()
    conn.close()

def change_limit(user_id, limit):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user_data
                    SET withdraw_limit = ?
                    WHERE user_id = ?
               """, (limit, user_id))


    conn.commit()
    conn.close()

def change_currency(user_id, currency):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user_data
                    SET currency = ?
                    WHERE user_id = ?
               """, (currency, user_id))

    conn.commit()
    conn.close()


def block_withdraw(user_id):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,))
    data = cursor.fetchone()[8]
    to_block_unblock = "0" if data == '1' else '1'

    cursor.execute("""UPDATE user_data
                    SET block_withdraw = ?
                    WHERE user_id = ?
               """, (to_block_unblock, user_id))

    conn.commit()
    conn.close()
    return to_block_unblock

def change_min_deposit(min_deposit):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE user_data SET min_deposit = ?", (min_deposit,))

    conn.commit()
    conn.close()


def get_lucky(user_id):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,))
    data = cursor.fetchone()[11]

    conn.close()

    return data


def change_lucky(user_id, lucky):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE user_data
                    SET lucky = ?
                    WHERE user_id = ?
               """, (lucky, user_id))

    conn.commit()
    conn.close()
