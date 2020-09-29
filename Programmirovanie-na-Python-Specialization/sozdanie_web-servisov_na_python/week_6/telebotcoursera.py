import telebot
import sqlite3


class DbConnector:
    @staticmethod
    def add_location_to_db(message):
        con = sqlite3.connect('db.sqlite3')
        cursor_obj = con.cursor()
        cursor_obj.execute(f"INSERT INTO Locations VALUES ({message.from_user.id}, {message.location.longitude}, "
                           f"{message.location.latitude}, {message.date})")
        con.commit()

    @staticmethod
    def show_locations_from_db(message):
        con = sqlite3.connect('db.sqlite3')
        cursor_obj = con.cursor()
        cursor_obj.execute(f"SELECT longitude, latitude, date from Locations as l "
                           f"WHERE l.user_id = {message.from_user.id} ORDER BY l.date DESC LIMIT 10")
        rows = cursor_obj.fetchall()
        if not rows:
            bot.send_message(chat_id=message.chat.id, text='You don\'t have any added location')
        else:
            bot.send_message(chat_id=message.chat.id, text='There is a list of last 10 locations')
            for row in rows:
                bot.send_location(chat_id=message.chat.id, longitude=row[0], latitude=row[1])

    @staticmethod
    def reset_locations_in_db(message):
        con = sqlite3.connect('db.sqlite3')
        cursor_obj = con.cursor()
        cursor_obj.execute(f"DELETE from Locations WHERE user_id = {message.from_user.id}")
        con.commit()
        bot.send_message(chat_id=message.chat.id, text='The locations list has been reset')


token = '1317313056:AAGBlhpSPxgkSQ4rWjVift3aP8ajYVmtgF4'
bot = telebot.TeleBot(token)
db = DbConnector()

keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
add_button = telebot.types.KeyboardButton(text='Add new location', request_location=True)
list_button = telebot.types.KeyboardButton(text='Show list of locations')
reset_button = telebot.types.KeyboardButton(text='Reset list of locations')
keyboard.add(add_button, list_button, reset_button)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello! I will help you add a location so that you can visit it later, '
                                      'if you want of course.\nChoose command on keyboard below', reply_markup=keyboard)


# @bot.message_handler(commands=['help'])
# def send_help_message(message):
#     bot.send_message(message.chat.id, f'What can I do for you, {message.from_user.first_name} '
#                                       f'{message.from_user.last_name}?')


@bot.message_handler(content_types='location')
def add_location(message):
    db.add_location_to_db(message)
    bot.send_message(chat_id=message.chat.id, text='Location has been added')
    print(message.from_user.id, message.location, message.date)
    # bot.send_message(chat_id=message.chat.id, text='Use /add to add name of location')


@bot.message_handler(regexp='^Show list of locations$')
def show_locations_list(message):
    db.show_locations_from_db(message)


@bot.message_handler(regexp='^Reset list of locations$')
def reset_locations_list(message):
    db.reset_locations_in_db(message)


bot.polling()
