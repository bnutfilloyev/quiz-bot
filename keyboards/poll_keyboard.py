from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from data.text import button_text

poll_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
poll_keyboard.add(types.KeyboardButton(text=button_text['create_quiz'],
                                       request_poll=KeyboardButtonPollType(type=types.PollType.QUIZ)))

poll_keyboard.add(KeyboardButton(text=button_text['cancel_button']))

remove_keyboard = types.ReplyKeyboardRemove()
