import asyncio
from aiogram import Bot, types, Dispatcher
from dotenv import dotenv_values
from aiogram.filters import Command
import random

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()


users = set()

@dp.message(Command('start'))
async def start(message: types.Message):
    name = message.from_user.first_name
    user_id = message.from_user.id

    users.add(user_id)

    user_count = len(users)

    commands = ('/myinfo\n'
                '/random\n')

    await message.answer(f'Hello, {name}!'
                         f' Our bot already serves {user_count} users.\n'
                         f'Available Commands:\n'
                         f' {commands}')

@dp.message(Command('myinfo'))
async def my_info(message: types.Message):
    info = message.from_user.first_name, message.from_user.username, message.from_user.id
    await message.answer(f'Information about you:\n'
                         f'First Name : {info[0]},\n'
                         f'Username : {info[1]},\n'
                         f'ID : {info[2]},\n')


@dp.message(Command('random'))
async def random_name(message: types.Message):
    random_list = ['Barry Allen', 'Bruce Wayne', 'Wade Wilson', 'Dura4ok','Peter Parker']
    await message.answer(f'Random name: {random.choice(random_list)}')

async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())