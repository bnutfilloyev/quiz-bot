from aiogram import types

from data.text import button_text

poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
poll_keyboard.add(types.KeyboardButton(text=button_text['create_quiz'],
                                       request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))

poll_keyboard.add(types.KeyboardButton(text=button_text['cancel_button']))

remove_keyboard = types.ReplyKeyboardRemove()
