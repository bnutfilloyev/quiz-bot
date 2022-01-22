from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.text import button_text

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=button_text['solve_test_text'])
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
