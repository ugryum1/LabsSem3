import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

with open("token.txt", "r") as f:
    TOKEN = f.read().strip()

# Создаём объект бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Клавиатура
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "Конвертировать валюту")],
        [KeyboardButton(text = "Список валют")],
        [KeyboardButton(text = "Помощь")]
    ],
    resize_keyboard = True
)

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Я бот-конвертер валют\nВыбери действие:",
        reply_markup = main_keyboard
    )

# Точка входа
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
