from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Solve Test')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
