import asyncio
import random

from aiogram import types

from data.text import button_text, text
from loader import dp
from utils.db_api.mongo import quizzes_database


@dp.message_handler(text=button_text['solve_test_text'])
async def send_text(msg: types.Message):
    skip = random.randint(0, int(quizzes_database.count_documents({})))
    for i in quizzes_database.find().skip(skip).limit(6):
        await msg.answer_poll(
            question=i['question'],
            options=i['options'],
            is_anonymous=True,
            type='quiz',
            allows_multiple_answers=False,
            correct_option_id=i['correct_option_id'],
        )
        await asyncio.sleep(5)
    await msg.answer(text['invite_link'])

