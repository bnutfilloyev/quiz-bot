from aiogram import types

from data import text

poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
poll_keyboard.add(types.KeyboardButton(text=text['create_quiz'],
                                       request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))

poll_keyboard.add(types.KeyboardButton(text=text['cancel_button']))