from aiogram import Router , types
# from aiogram.filters import Command
# from season_3_lesson_bot.main import bot

echo_router = Router()
@echo_router.message()
async def echo_handler(message: types.Message):
    txt = message.text
    await message.bot.send_message(chat_id=message.from_user.id, text=txt)
    # await message.answer(txt)