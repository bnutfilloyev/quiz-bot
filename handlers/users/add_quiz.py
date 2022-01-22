from aiogram import types

from loader import dp, bot


@dp.message_handler(commands=["add_quiz"])
async def cmd_start(message: types.Message):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="Создать викторину",
                                           request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    poll_keyboard.add(types.KeyboardButton(text="Отмена"))
    await message.answer("Нажмите на кнопку ниже и создайте викторину! "
                         "Внимание: в дальнейшем она будет публичной (неанонимной).", reply_markup=poll_keyboard)
