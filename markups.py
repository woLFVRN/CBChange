from telebot import types

start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('Начать')
start_markup.add(start_markup_btn1)

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Обмен')
source_markup_btn2 = types.KeyboardButton('Помощь')
source_markup.add(source_markup_btn1, source_markup_btn2)

age_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
age_markup_btn1 =  types.KeyboardButton('Перевод')
age_markup_btn2 =  types.KeyboardButton('неделя')
age_markup_btn3 =  types.KeyboardButton('Месяц')
age_markup.add(age_markup_btn1, age_markup_btn2, age_markup_btn3)

transfer_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
transfer_markup_btn1 =  types.KeyboardButton('Готово')
transfer_markup_btn2 =  types.KeyboardButton('В начало')
transfer_markup.add(transfer_markup_btn1, transfer_markup_btn2)


rating_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
rating_markup_btn1 =  types.KeyboardButton('Продолжить')
rating_markup_btn2 =  types.KeyboardButton('Вернуться')
rating_markup.add(rating_markup_btn1, rating_markup_btn2)

amount_markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
amount_markup_btn1 =  types.KeyboardButton('Да')
amount_markup_btn2 =  types.KeyboardButton('Нет')
amount_markup_btn2 =  types.KeyboardButton('В начало')
amount_markup.add(amount_markup_btn1, amount_markup_btn2, amount_markup_btn3)
