from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from config import settings
import handlers
import asyncio


async def main():
    print('Bot is running!')
    print(settings.BOT_TOKEN)
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
    print(bot)
    dp = Dispatcher()
    dp.message.register(handlers.start, Command('start'))
    await dp.start_polling(bot)  # Удалите 'bot=bot' здесь

if __name__ == '__main__':
    asyncio.run(main())