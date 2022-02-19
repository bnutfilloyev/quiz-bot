import asyncio
import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.text import text, curriculum_text, level_text, subject_text
from loader import dp, bot
from utils.db_api.mongo import quizzes_database, user_db, polls_database


@dp.callback_query_handler(text_contains='level')
async def send_text(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        split_data = call.data.split(':')
        data[split_data[0]] = split_data[-1]

        # User message delete
        await call.message.delete()

        # quiz message sleep time
        sleep_time = 5
        quizes = []
        for i in quizzes_database.find({'subject': data['subject'],
                                        'curriculum': data['curriculum'],
                                        'level': data['level']}):
            quizes.append(i['quiz_id'])

        if len(quizes) == 0:
            await call.message.answer(text['over_text'])
            await call.message.answer(text['invite_link'])
            return

        # quiz message send random
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

            poll = await call.message.answer_poll(
                question=i['question'],
                options=i['options'],
                is_anonymous=False,
                type='quiz',
                allows_multiple_answers=False,
                correct_option_id=i['correct_option_id'],
                open_period=sleep_time,
            )
            polls_database.insert_one({'user_id': poll.chat.id, 'poll_id': poll.poll.id, 'correct_option_id': poll.poll.correct_option_id})
            await asyncio.sleep(sleep_time)
            # break
        correct_answer = 0
        total_quiz = 0
        for poll in polls_database.find({'user_id': call.from_user.id}):
            total_quiz += 1
            correct_option_id = poll['correct_option_id']
            poll_id = poll['poll_id']
            try:
                answer_polls = user_db.find_one_and_delete({'poll_id': poll_id})['option_ids']
                if answer_polls == correct_option_id:
                    correct_answer += 1
            except:
                pass
            polls_database.delete_one({'poll_id': poll_id})

        await call.message.answer(text['invite_link'].format(
            subject_text[data['subject']], curriculum_text[data['curriculum']], level_text[data['level']],
            correct_answer,
            total_quiz - correct_answer,
            correct_answer * 100 // total_quiz,
        ))


@dp.poll_answer_handler()
async def poll(poll: types.Poll):
    user_db.update_one({'poll_id': poll["poll_id"]}, {
        '$set': {
            'user_id': str(poll["user"]["id"]),
            "option_ids": poll["option_ids"][0],
        }}, upsert=True)
