import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile

# Загружаем переменные из спрятанного .env файла
load_dotenv()

# Безопасно достаем токен
TOKEN = os.getenv("BOT_TOKEN")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # Приветственный текст
    welcome_text = (
        "Привет! 🤍\n\n"
        "Рада видеть тебя. Как и обещала, отправляю полезные материалы.\n\n"
        "А чтобы не пропустить анонсы лекций и полезные подкасты, "
        "обязательно подписывайся на наш закрытый канал: [Ссылка на канал]"
    )
    
    # Путь к PDF файлу (положи файл guide.pdf в ту же папку, где скрипт)
    # На продакшене лучше отправлять по file_id, чтобы не грузить файл каждый раз
    document = FSInputFile("guide.pdf")
    
    # Отправляем сообщение и документ
    await message.answer(welcome_text, disable_web_page_preview=True)
    await bot.send_document(chat_id=message.chat.id, document=document)

async def main():
    # Запускаем поллинг
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())