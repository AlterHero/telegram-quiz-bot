from aiogram import types
from questions import quiz_data
from aiogram.utils.keyboard import InlineKeyboardBuilder

def generate_options_keyboard(question_index):
    builder = InlineKeyboardBuilder()
    options = quiz_data[question_index]['options']
    correct_option = quiz_data[question_index]['correct_option']

    for i, option in enumerate(options):
        callback_data = "correct" if i == correct_option else "wrong"
        builder.add(types.InlineKeyboardButton(text=option, callback_data=callback_data))

    builder.adjust(1)
    return builder.as_markup()
