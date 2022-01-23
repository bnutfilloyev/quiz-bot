import asyncio
import random

from aiogram import types

from data.text import button_text, text
from loader import dp
from utils.db_api.mongo import quizzes_database


@dp.message_handler(text=button_text['solve_test_text'])
async def send_text(msg: types.Message):
    data = []
    for i in quizzes_database.find():
        data.append(i['quiz_id'])
    for j in range(6):
        quiz_id = random.choice(data)
        data.remove(quiz_id)
        i = quizzes_database.find_one({'quiz_id': quiz_id})
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
