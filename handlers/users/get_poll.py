from aiogram import types
from aiogram.dispatcher import FSMContext

from data.text import text
from loader import dp
from states.States import Form
from utils.db_api.mongo import quizzes_database

@dp.message_handler(content_types=types.ContentType.PHOTO, state=Form.addPoll)
async def get_image(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo_id'] = msg.photo[-1].file_id
        await Form.getPoll.set()


@dp.message_handler(content_types=types.ContentTypes.POLL, state=Form.getPoll)
async def save_poll(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.poll.type != "quiz":
            await message.reply(text['check_quiz'])
            return

        quizzes_database.insert_one({
            'quiz_id': message.poll.id,
            'question': message.poll.question,
            'options': [o.text for o in message.poll.options],
            'correct_option_id': message.poll.correct_option_id,
            'photo_id': data['photo_id'],
            'subject': data['subject'],
            'curriculum': data['curriculum'],
            'level': data['level'],
        })

        await message.reply(text['count_quiz'].format(quizzes_database.count_documents({})))
        await state.finish()


@dp.message_handler(content_types=types.ContentTypes.POLL, state=Form.addPoll)
async def msg_with_poll(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.poll.type != "quiz":
            await message.reply(text['check_quiz'])
            return

        quizzes_database.insert_one({
            'quiz_id': message.poll.id,
            'question': message.poll.question,
            'options': [o.text for o in message.poll.options],
            'correct_option_id': message.poll.correct_option_id,
            'photo_id': None,
            'subject': data['subject'],
            'curriculum': data['curriculum'],
            'level': data['level'],
        })

        await message.reply(text['count_quiz'].format(quizzes_database.count_documents({})))
