import telebot  # Основная библиотека для работы с Bot API

import logging

import bot_token  # Файл с объявлением токена спрятан с помощью .gitignore
import quotes  # Все фразы бота
import parsing  # Функции для работы с текстом и хранилищем
import database  # Функции для работы с базой данных
import exceptions  # Различные виды исключений

LOG_FILE = 'logs.txt'
logging.basicConfig(format='%(asctime)s %(filename)s:%(lineno)-3d' +
                    ' %(levelname)-8s %(message)s', level=logging.INFO,
                    filename=LOG_FILE)
logging._defaultFormatter = logging.Formatter(u'%(message)s')

bot = telebot.TeleBot(bot_token.token)
print(bot.get_me())


@bot.message_handler(commands=['start', 'help'])
def handle_text(message):
    bot.send_message(message.chat.id, quotes.HELP_TEXT, parse_mode='Markdown')


@bot.message_handler(commands=['add'])
def handle_text(message):
    try:
        arguments = parsing.find_arguments(message.text, last_is_string=True)
        cost = parsing.get_cost(arguments[0])
        date = parsing.get_date(arguments[1])
        description = parsing.get_description(arguments[2])
        database.add(message.chat.id, cost, date, description)
        bot.send_message(message.chat.id, quotes.ADD_OK)
    except exceptions.WrongNumberOfArgumentsException as exception:
        bot.send_message(message.chat.id, exception.value)
    except exceptions.InvalidArgumentFormatException as exception:
        bot.send_message(message.chat.id, exception.value)
    except OSError as exception:
        logging.critical(exception)
        bot.send_message(message.chat.id, quotes.BACKEND_ERROR)
        raise
    except Exception as exception:
        logging.error(exception)
        bot.send_message(message.chat.id, quotes.UNEXPECTED_ERROR)
        raise


@bot.message_handler(commands=['remove'])
def handle_text(message):
    try:
        arguments = parsing.find_arguments(message.text)
        record_id = parsing.get_id(arguments[0])
        database.remove(message.chat.id, record_id)
        bot.send_message(message.chat.id, quotes.REMOVE_OK)
    except exceptions.WrongNumberOfArgumentsException as exception:
        bot.send_message(message.chat.id, exception.value)
    except exceptions.NoSuchRecordException as exception:
        bot.send_message(message.chat.id, exception.value)
    except exceptions.InvalidArgumentFormatException as exception:
        bot.send_message(message.chat.id, exception.value)
    except OSError as exception:
        logging.critical(exception)
        bot.send_message(message.chat.id, quotes.BACKEND_ERROR)
        raise
    except Exception as exception:
        logging.error(exception)
        bot.send_message(message.chat.id, quotes.UNEXPECTED_ERROR)
        raise


@bot.message_handler(commands=['change'])
def handle_text(message):
    try:
        arguments = parsing.find_arguments(message.text, last_is_string=True)
        record_id = parsing.get_id(arguments[0])
        cost = parsing.get_cost(arguments[1])
        date = parsing.get_date(arguments[2])
        description = parsing.get_description(arguments[3])
        database.change(message.chat.id, record_id, cost, date, description)
        bot.send_message(message.chat.id, quotes.CHANGE_OK)
    except exceptions.WrongNumberOfArgumentsException as exception:
        bot.send_message(message.chat.id, exception.value)
    except exceptions.NoSuchRecordException as exception:
        bot.send_message(message.chat.id, exception.value)
    except exceptions.InvalidArgumentFormatException as exception:
        bot.send_message(message.chat.id, exception.value)
    except OSError as exception:
        logging.critical(exception)
        bot.send_message(message.chat.id, quotes.BACKEND_ERROR)
        raise
    except Exception as exception:
        logging.error(exception)
        bot.send_message(message.chat.id, quotes.UNEXPECTED_ERROR)
        raise


@bot.message_handler(commands=['show'])
def handle_text(message):
    try:
        bot.send_message(message.chat.id,
                         database.find_records(message.chat.id))
    except OSError as exception:
        logging.critical(exception)
        bot.send_message(message.chat.id, quotes.BACKEND_ERROR)
        raise
    except Exception as exception:
        logging.error(exception)
        bot.send_message(message.chat.id, quotes.UNEXPECTED_ERROR)
        raise


@bot.message_handler(commands=['total'])
def handle_text(message):
    try:
        bot.send_message(message.chat.id,
                         database.find_total_outcome(message.chat.id))
    except OSError as exception:
        logging.critical(exception)
        bot.send_message(message.chat.id, quotes.BACKEND_ERROR)
        raise
    except Exception as exception:
        logging.error(exception)
        bot.send_message(message.chat.id, quotes.UNEXPECTED_ERROR)
        raise


@bot.message_handler(commands=['last'])
def handle_text(message):
    try:
        arguments = parsing.find_arguments(message.text)
        number = parsing.get_number(arguments[0])
        unit = parsing.get_unit(arguments[1])
        bot.send_message(message.chat.id,
                         database.recently_outcome(message.chat.id, number,
                                                   unit))
    except exceptions.WrongNumberOfArgumentsException as exception:
        bot.send_message(message.chat.id, exception.value)
    except exceptions.InvalidArgumentFormatException as exception:
        bot.send_message(message.chat.id, exception.value)
    except OSError as exception:
        logging.critical(exception)
        bot.send_message(message.chat.id, quotes.BACKEND_ERROR)
        raise
    except Exception as exception:
        logging.error(exception)
        bot.send_message(message.chat.id, quotes.UNEXPECTED_ERROR)
        raise


@bot.message_handler(commands=['clear'])
def handle_text(message):
    try:
        arguments = parsing.find_arguments(message.text)
        date = parsing.get_date(arguments[0])
        database.clear_before_date(message.chat.id, date)
        bot.send_message(message.chat.id, quotes.CLEAR_OK)
    except exceptions.WrongNumberOfArgumentsException as exception:
        bot.send_message(message.chat.id, exception.value)
    except exceptions.InvalidArgumentFormatException as exception:
        bot.send_message(message.chat.id, exception.value)
        logging.critical(exception)
        bot.send_message(message.chat.id, quotes.BACKEND_ERROR)
        raise
    except OSError as exception:
        logging.critical(exception)
        bot.send_message(message.chat.id, quotes.BACKEND_ERROR)
        raise
    except Exception as exception:
        logging.error(exception)
        bot.send_message(message.chat.id, quotes.UNEXPECTED_ERROR)
        raise


try:
    bot.polling(none_stop=True, interval=0)
except GeneratorExit as exception:
    logging.info('GeneratorExit: {}'.format(exception))
except SystemExit as exception:
    logging.info('SystemExit: {}'.format(exception))
except KeyboardInterrupt as exception:
    logging.info('KeyboardInterrupt: {}'.format(exception))
except OSError:
    pass
except Exception:
    pass
