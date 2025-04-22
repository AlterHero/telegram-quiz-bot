import asyncio
import logging
import nest_asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from config import API_TOKEN
from database import create_table, get_quiz_index, update_quiz_index, update_score, get_score
from quiz import generate_options_keyboard
from questions import quiz_data

nest_asyncio.apply()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="Начать игру")]],
        resize_keyboard=True
    )
    await message.answer("Добро пожаловать в квиз!", reply_markup=keyboard)

@dp.message(F.text.casefold() == "начать игру")
async def start_quiz_button_handler(message: types.Message):
    await message.answer("Начинаем квиз!")
    user_id = message.from_user.id
    await update_quiz_index(user_id, 0)
    await update_score(user_id, 0)
    await send_question(message, index=0)

async def send_question(message, index=None):
    if index is None:
        index = await get_quiz_index(message.from_user.id)
    await message.answer(
        quiz_data[index]['question'],
        reply_markup=generate_options_keyboard(index)
    )

@dp.callback_query(lambda c: c.data and c.data in {"correct", "wrong"})
async def handle_answer(callback: types.CallbackQuery):
    question_index = await get_quiz_index(callback.from_user.id)
    await callback.message.edit_text(f"{quiz_data[question_index]['question']}")

    score = await get_score(callback.from_user.id) or 0

    if callback.data == "correct":
        await callback.message.answer("Верно!")
        await update_score(callback.from_user.id, score + 1)
    else:
        correct_answer = quiz_data[question_index]['options'][quiz_data[question_index]['correct_option']]
        await callback.message.answer(f"Неправильно! Правильный ответ: {correct_answer}")

    new_index = question_index + 1
    await update_quiz_index(callback.from_user.id, new_index)

    if new_index < len(quiz_data):
        await send_question(callback.message, index=new_index)
    else:
        final_score = await get_score(callback.from_user.id)
        await callback.message.answer(
            f"🎉 Квиз завершён, {callback.from_user.first_name}!\n"
            f"Вы набрали {final_score} из {len(quiz_data)} баллов!"
        )

async def main():
    await create_table()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    async def startup():
        await bot.delete_webhook(drop_pending_updates=True)
        await main()

    asyncio.run(startup())
