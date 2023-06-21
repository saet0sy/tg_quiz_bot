import random
from aiogram import Dispatcher, types

# Вопросы для викторины
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin"],
        "correct_answer": "Paris"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"],
        "correct_answer": "Leonardo da Vinci"
    },
     {
        "question": "What is the capital of Japan?",
        "options": ["Tokyo", "Beijing", "Seoul"],
        "correct_answer": "Tokyo"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Jane Austen"],
        "correct_answer": "William Shakespeare"
    },
    {
        "question": "Which country is famous for the Great Wall?",
        "options": ["China", "India", "Brazil"],
        "correct_answer": "China"
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["Sahara Desert", "Gobi Desert", "Antarctic Desert"],
        "correct_answer": "Sahara Desert"
    },
    {
        "question": "Who discovered the theory of relativity?",
        "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei"],
        "correct_answer": "Albert Einstein"
    }
    # Остальные вопросы...
]

# Словарь для отслеживания количества правильных ответов
user_scores = {}


async def start_quiz(message: types.Message):
    # Выбираем случайный вопрос из списка
    question = random.choice(questions)

    # Формируем текст сообщения с вопросом и вариантами ответов
    question_text = question['question']
    options = question['options']
    buttons = [types.KeyboardButton(option) for option in options]
    random.shuffle(buttons)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    # Отправляем сообщение с вопросом и кнопками
    await message.answer(question_text, reply_markup=keyboard)


async def process_answer(message: types.Message):
    # Проверяем, является ли ответ правильным
    for question in questions:
        if message.text == question['correct_answer']:
            response = 'Правильный ответ!'
            # Увеличиваем счетчик правильных ответов для пользователя
            user_scores.setdefault(message.from_user.id, 0)
            user_scores[message.from_user.id] += 1
            break
    else:
        response = 'Неправильный ответ!'

    # Отправляем ответ пользователю
    await message.answer(response)

    # Проверяем количество ответов пользователя
    if user_scores.get(message.from_user.id, 0) == 5:
        # Пользователь ответил на 5 вопросов, завершаем викторину
        await message.answer("Викторина завершена! Ваш счет: {}".format(user_scores[message.from_user.id]))
    else:
        # Продолжаем викторину с новым вопросом
        await start_quiz(message)


def setup(dp: Dispatcher):
    dp.register_message_handler(start_quiz, commands=['quiz'])
    dp.register_message_handler(process_answer)
