import telebot
from telebot import types

dict = {'Готовые блюда': ['Оливье', 'Окрошка'], 'Овощи': ['Картошка', 'Броколи'], 'Фрукты': ['Яблоко', 'Банан'],
        'Мясо': ['Баранина', 'Свинина'], 'Рыба': ['Треска', 'Сёмга']}
dict_keys = list(dict.keys())
dict_values = list(dict.values())

CONTENT_TYPES = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"]

bot = telebot.TeleBot("5982546796:AAHGDn5cdQowW6v1OuFfYbZh-nrDeZUlKkI", parse_mode=None)

a = dict.get('Готовые блюда')
print(a)


# for i in dict_values:
#     for g in i:
#         print(g)

def choose_type(types_dish, message):
    global key_values
    if message.text == types_dish:
        bot.reply_to(message, text='Назовите продукт, которое нужно убрать'.format(message.from_user))
        key_values = dict.get(types_dish)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Задать вопрос")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}!\nЯ бот, который поможет хранить твои продукты правильно!\n ".format(
                         message.from_user), reply_markup=markup)


# commands=['помощь'],
@bot.message_handler(content_types=['text'])
def category(message):
    if message.text == 'Задать вопрос':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a = telebot.types.ReplyKeyboardRemove()
        btn = types.KeyboardButton(dict_keys[0])
        btn1 = types.KeyboardButton(dict_keys[1])
        btn2 = types.KeyboardButton(dict_keys[2])
        btn3 = types.KeyboardButton(dict_keys[3])
        btn4 = types.KeyboardButton(dict_keys[4])
        markup.add(btn, btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,
                         text='Скажи мне категорию продуктов и я помогу тебе убрать их'.format(message.from_user),
                         reply_markup=markup)
    elif message.text != 'Задать вопрос':
        asking_cur(message)


@bot.message_handler(content_types=['text'])
def asking_cur(message):
    choose_type('Готовые блюда', message)
    choose_type('Овощи', message)
    choose_type('Фрукты', message)
    choose_type('Мясо', message)
    choose_type('Рыба', message)

    if message.text == 'Готовые блюда' or message.text == 'Овощи' or message.text == 'Фрукты' or message.text == 'Мясо' or message.text == 'Рыба':
        checkdish(message)


@bot.message_handler(content_types=['text'])
def checkdish(message):
    msg = bot.send_message(message.chat.id, 'Напишите название с заглавной буквы')
    bot.register_next_step_handler(msg, next_step)


def next_step(message):
    if message.text in key_values:
        # if  ....:
        #     messages, description of message (food)

        bot.send_message(message.chat.id, text='OK')
    else:
        bot.reply_to(message, text='Такого продукта пока нет.\nНо скоро добавим!\nДля дальнейшенго использования нужно выбрать категорию ещё раз.'.format(message.from_user))
        asking_cur(message)


bot.infinity_polling()
