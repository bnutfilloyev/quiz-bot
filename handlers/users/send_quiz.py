import asyncio
import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.config import ADMINS
from data.text import text
from loader import dp, bot
from utils.db_api.mongo import quizzes_database
from utils.misc.formatter import get_formatted_message


@dp.callback_query_handler(text_contains='level')
async def send_text(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        split_data = call.data.split(':')
        data[split_data[0]] = split_data[-1]

        await call.message.delete()
        sleep_time = 20
        quizes = []
        for i in quizzes_database.find():
            quizes.append(i['quiz_id'])

        for j in range(6):
            quiz_id = random.choice(quizes)
            quizes.remove(quiz_id)
            i = quizzes_database.find_one(
                {'quiz_id': quiz_id, 'subject': data['subject'], 'curriculum': data['curriculum'],
                 'level': data['level']})
            if i == None:
                await call.message.answer(text['over_text'])
                break
            if i['photo_id'] != None:
                await call.message.answer_photo(i['photo_id'])

            await call.message.answer_poll(
                question=i['question'],
                options=i['options'],
                is_anonymous=True,
                type='quiz',
                allows_multiple_answers=False,
                correct_option_id=i['correct_option_id'],
                open_period=sleep_time,
            )
            await asyncio.sleep(sleep_time)
        await call.message.answer(text['invite_link'])


@dp.poll_answer_handler()
async def test_poll_answer(poll: types.PollAnswer):
    print(poll)
    for admin in ADMINS:
        await bot.send_message(admin, str(poll))
