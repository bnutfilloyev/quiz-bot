from aiogram import types

from loader import dp
from utils.Quiz import Quiz
from utils.db_api.mongo import quizzes_database, quizzes_owners


@dp.message_handler(content_types=["poll"])
async def msg_with_poll(message: types.Message):
    # # Если юзер раньше не присылал запросы, выделяем под него запись
    # if not quizzes_database.get(str(message.from_user.id)):
    #     quizzes_database[str(message.from_user.id)] = []

    # Если юзер решил вручную отправить не викторину, а опрос, откажем ему.
    if message.poll.type != "quiz":
        await message.reply("Извините, я принимаю только викторины (quiz)!")
        return

    # Сохраняем себе викторину в память
    quizzes_database.update_one({'telegram_id':str(message.from_user.id)}, {Quiz(
        quiz_id=message.poll.id,
        question=message.poll.question,
        options=[o.text for o in message.poll.options],
        correct_option_id=message.poll.correct_option_id,
        owner_id=message.from_user.id)}
    )
    # Сохраняем информацию о её владельце для быстрого поиска в дальнейшем
    quizzes_owners[message.poll.id] = str(message.from_user.id)

    await message.reply(
        f"Викторина сохранена. Общее число сохранённых викторин: {len(quizzes_database[str(message.from_user.id)])}")