from aiogram import types
from aiogram.dispatcher import Dispatcher
import controllers.quiz as quiz


# Функция-обработчик для команды /start
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('/quiz'))

    await message.reply("Привет! Выбери одну из игр:", reply_markup=keyboard)




# Функция для настройки обработчиков команды /start и /quiz
def setup(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz.start_quiz, commands=['quiz'])
    dp.register_message_handler(quiz.process_answer)
