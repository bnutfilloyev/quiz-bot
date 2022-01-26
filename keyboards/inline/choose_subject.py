from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.text import subject_text, curriculum_text, level_text
from keyboards.inline.callback_data import subject_callback, curriculum_callback, level_callback

Subject = InlineKeyboardMarkup(row_width=1)
for value, key in subject_text.items():
    Subject.insert(InlineKeyboardButton(text=key, callback_data=subject_callback.new(item_name=value)))

Curriculum = InlineKeyboardMarkup(row_width=1)
for value, key in curriculum_text.items():
    Curriculum.insert(InlineKeyboardButton(text=key, callback_data=curriculum_callback.new(item_name=value)))

Level = InlineKeyboardMarkup(row_width=1)
for value, key in level_text.items():
    Level.insert(InlineKeyboardButton(text=key, callback_data=level_callback.new(item_name=value)))