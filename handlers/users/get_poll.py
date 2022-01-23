from aiogram import types
from aiogram.dispatcher import FSMContext

from data.text import text
from loader import dp
from utils.db_api.mongo import quizzes_database


@dp.message_handler(content_types=types.ContentTypes.POLL)
async def msg_with_poll(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.poll.type != "quiz":
            await message.reply(text['check_quiz'])
            return

        quizzes_database.insert_one({
            'question': message.poll.question,
            'options': [o.text for o in message.poll.options],
            'correct_option_id': message.poll.correct_option_id,
        })

        await message.reply(text['count_quiz'].format(quizzes_database.count_documents({})))
