import asyncio
import logging



from bot_config import dp,bot

from handlers.start import start_router
from handlers.picture import picture_router
from handlers.other_mess import echo_router


async def main():
    dp.include_routers(start_router,
                       picture_router,
                       echo_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


# @dp.message(Command("start"))
# async def start_handler(message: types.Message):
#     name = message.from_user.first_name
#     # await message.answer(f'Привет, {name}')
#     await message.reply (f"Hello {name}")


# @dp.message(Command("picture"))
# async def picture_handler(message: types.Message):
#     photo = types.FSInputFile('picture/maxresdefault.jpg')
#     await message.answer_photo(
#         photo=photo,
#         caption='Alphabet'
#     )




# @dp.message()
# async def echo_handler(message: types.Message):
#     txt = message.text
#     await bot.send_message(chat_id=message.from_user.id, text=txt)
#     # await message.answer(txt)

async def main():
    dp.include_routers(start_router,
                       picture_router,
                       echo_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

