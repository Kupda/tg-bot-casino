import os
from dotenv import load_dotenv
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from random import randint


# Считываем токен из файла .env
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"""Привет, {message.from_user.full_name}, крутанем?\n
/roll - чтобы крутануть
/stats - чтобы узнать свою статистику""")

# Хэндлер на команду /roll
@dp.message(Command("roll"))
async def cmd_start(message: types.Message):
    slot1 = randint(1, 6)
    slot2 = randint(1, 6)
    slot3 = randint(1, 6)
    await message.answer(f"""Выпало: {slot1}|{slot2}|{slot3}""")
    if slot1 == slot2 and slot2 == slot3:
        await message.answer(f"""Поздравляю! Вы выиграли 5 монет!""")
    elif slot1 == slot2 and slot2 != slot3 or slot1 == slot3 and slot1 != slot2 or slot2 == slot3 and slot2 != slot1:
        await message.answer(f"""Поздравляю! Вы выиграли 3 монеты!""")
    else:
        await message.answer(f"""К сожалению, вы ничего не выиграли =(""")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
