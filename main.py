from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import settings
import asyncio


async def main():
    dp = Dispatcher()
    bot = Bot(token = settings.BOT_TOKEN, default = DefaultBotProperties(parse_mode = ParseMode.MARKDOWN_V2))
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())