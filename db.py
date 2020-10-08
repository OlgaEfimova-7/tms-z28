import sqlite3
__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('telegram_bot.db')
        return __connection


def init_db(force: bool = False):
    conn = get_connection()
    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS users')
        c.execute('DROP TABLE IF EXISTS stock_information')
        c.execute('DROP TABLE IF EXISTS sold_stocks_information')
    c.execute("\n"
              "    CREATE TABLE IF NOT EXISTS users(\n"
              "        id  INTEGER PRIMARY KEY,\n"
              "        str VARCHAR NOT NULL,\n"
              "        frequency INTEGER)")
    c.execute('\n'
              '    CREATE TABLE IF NOT EXISTS stock_information(\n'
              '        id  INTEGER PRIMARY KEY,\n'
              '        company VARCHAR NOT NULL,\n'
              '        amount_of_stocks VARCHAR NOT NULL,'
              '        sum_of_investments_in_stocks VARCHAR NOT NULL,'
              '        currency VARCHAR NOT NULL,'
              '        user_id INTEGER NOT NULL,'
              '        FOREIGN KEY(user_id) REFERENCES users (id))')
    c.execute('\n'
              '    CREATE TABLE IF NOT EXISTS sold_stocks_information(\n'
              '        id INTEGER PRIMARY KEY,\n'
              '        company VARCHAR NOT NULL,\n'
              '        amount_of_stocks VARCHAR NOT NULL,'
              '        cost_of_sold_stocks VARCHAR NOT NULL,'
              '        currency VARCHAR NOT NULL,'
              '        user_id INTEGER NOT NULL,'
              '        FOREIGN KEY(user_id) REFERENCES users (id))')
    conn.commit()
    global __connection
    __connection = None


def add_user(chat_id, frequency: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO users (str, frequency) VALUES (?, ?)',
              (chat_id, frequency))
    conn.commit()
    global __connection
    __connection = None


def add_stock_information(company: str, amount_of_stocks, sum_of_investments, currency: str, user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO stock_information (company, amount_of_stocks, sum_of_investments_in_stocks, currency, '
              'user_id)'
              'VALUES (?, ?, ?, ?, ?)',
              (company, amount_of_stocks, sum_of_investments, currency, user_id))
    conn.commit()
    global __connection
    __connection = None


def add_sold_stock_information(company: str, amount_of_stocks, cost_of_sold_stocks, currency: str, user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO sold_stocks_information (company, amount_of_stocks, cost_of_sold_stocks, currency, '
              'user_id)'
              'VALUES (?, ?, ?, ?, ?)',
              (company, amount_of_stocks, cost_of_sold_stocks, currency, user_id))
    conn.commit()
    global __connection
    __connection = None


def get_user(chat_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE str = ?', (chat_id, ))
    res = c.fetchall()
    global __connection
    __connection = None
    return res


def get_stock_information_from_db(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT company, amount_of_stocks, sum_of_investments_in_stocks, currency FROM '
              'stock_information WHERE user_id = ?', (user_id, ))
    res = c.fetchall()
    global __connection
    __connection = None
    return res


def get_sold_stock_information_from_db(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT company, amount_of_stocks, cost_of_sold_stocks, currency FROM '
              'sold_stocks_information WHERE user_id = ?', (user_id, ))
    res = c.fetchall()
    global __connection
    __connection = None
    return res


def change_frequency(frequency, user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET frequency = ? WHERE users.id = ?', (frequency, user_id))
    conn.commit()
    global __connection
    __connection = None


def get_frequency_and_chat_id():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT str, frequency FROM USERS')
    res = c.fetchall()
    global __connection
    __connection = None
    return res


def get_stock_information_about_specific_company(user_id, company):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT company, amount_of_stocks, sum_of_investments_in_stocks, currency FROM stock_information WHERE '
              'user_id = ? AND company = ?', (user_id, company))
    res = c.fetchall()
    global __connection
    __connection = None
    return res


def get_sold_stock_information_about_specific_company(user_id, company):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT company, amount_of_stocks, cost_of_sold_stocks, currency FROM sold_stocks_information WHERE '
              'user_id = ? AND company = ?', (user_id, company))
    res = c.fetchall()
    global __connection
    __connection = None
    return res


if __name__ == '__main__':
    init_db(True)

