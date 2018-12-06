import telebot
import bs4
import random
from Task import Task
import parser
import markups as m

#main variables
TOKEN = ''
bot = telebot.TeleBot(TOKEN)
task = Task()

#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    if not task.isRunning:
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, 'Доброго времени суток! Вас приветсвует автоматизированный обменник CBChange. До конца декабря мы работаем по фиксированному курсу 1 CBC = 20 руб.', reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, askSource)
        task.isRunning = True

def askSource(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[0]:
        task.mySource = 'Обмен'
        msg = bot.send_message(chat_id, 'В настоящий момент выводы происходят только на банковскую карту. Курс на сегодня 1 CBC = 20 руб. Введите номер вашей карты (без пробелов):')
        bot.register_next_step_handler(msg, askAge)
    elif text in task.names[1]:
        task.mySource = 'Помощь'
        msg = bot.send_message(chat_id, 'ТЕКСТ ПОМОЩИ', reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, askSource)    
    else:
        msg = bot.send_message(chat_id, 'Что-то пошло не так, попробуйте снова')
        bot.register_next_step_handler(msg, askSource)
        return

def askAge(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Номер карты должен состоять из чисел. Проверьте ввод и попробуйте снова.', reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, askAge)
        return
    else:
        msg = bot.send_message(chat_id, 'Внимательно проверьте номер введенной вами карты. Все верно?', reply_markup=m.amount_markup)
        bot.register_next_step_handler(msg, askAmount)

def askTransfer(message):
    chat_id = message.chat.id
    text = task.filters()
    if text in task.filters[1]:
        msg = bot.send_message(chat_id, 'Осуществите перевод указанной вами суммы на указанный ниже CBC кошелек. Обращаем ваше внимание, что срок осуществленния перевода от 15 минут и до нескольких суток (в зависимости от нагруженности сети)')
        msg = bot.send_message(chat_id, 'ZPK2QEV3aK6HwMgZaThm57zJhAjqJuxbpJ', reply_markup=m.transfer_markup) 
        bot.register_next_step_handler(msg, askAmount)
    else
        task.isRunning = False
        output = ''
        msg = bot.send_message(chat_id, output, reply_markup=m.start_markup)
    
def AskEnd(message):
    chat_id = message.chat.id
    text = task.filters()
    digits = set(range(10))
    first = random.randint(1, 9)
    last_4 = random.sample(digits - {first}, 4)
    if text in task.filters[1]:
        msg = bot.send_message(chat_id, 'Номер вашей транзакции: {0}'.format(str(first) + ''.join(map(str, last_3))))
        msg = bot.send_message(chat_id, 'Ожидайте зачисления средств на выбранную платежную систему. Это может занять некоторое время. Будем ждать вас снова!')
        task.isRunning = False
        output = ''
        msg = bot.send_message(chat_id, output, reply_markup=m.start_markup)
    else
        task.isRunning = False
        output = ''
        msg = bot.send_message(chat_id, output, reply_markup=m.start_markup)   
    
def askRating(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if not text.isdigit:
        msg = bot.send_message(chat_id, 'Введите корректное числовое значение (прим.: 10000). Повторим?', reply_markup=m.amount_markup)
        bot.register_next_step_handler(msg, askAmount)
    else
        msg = bot.reply_to(message, 'Вы получите (не включая возможную коммиссию вашего банка): {!s}'.format(message.text * 20), reply_markup=m.rating_markup)
        bot.register_next_step_handler(msg, askTransfer)

def askAmount(message):
    chat_id = message.chat.id
    text = task.filters_code_names()
    filterscn = task.filters_code_names
    if text in task.filters_code_names[1]:
        msg = bot.send_message(chat_id, 'Какое количество монет вы бы хотел вывести? (Минимальная сумма вывода 300 CBC)')
        bot.register_next_step_handler(msg, askRating)
    if text in task.filters_code_names[2]:
        msg = bot.send_message(chat_id, 'В настоящий момент выводы происходят только на банковскую карту. Курс на сегодня 1 CBC = 20 руб. Введите номер вашей карты (без пробелов):')
        bot.register_next_step_handler(msg, askAge)
    #if int(text) < 1 or int(text) > 5:
        #msg = bot.send_message(chat_id, 'Количество страниц должно быть >0 и <6. Введите корректно.')
        #bot.register_next_step_handler(msg, askAmount)
        #return
    else
        task.isRunning = False
        output = ''
        msg = bot.send_message(chat_id, output, reply_markup=m.start_markup)

bot.polling(none_stop=False, interval=0, timeout=20)
