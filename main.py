from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart, StateFilter
from config import settings
import handlers
import constants
import states
import asyncio



async def register_handlers(dp: Dispatcher):
    dp.message.register(handlers.start, CommandStart())
    dp.message.register(handlers.buy_subscription, F.text == constants.SUBSCRIBE_BUTTON_TEXT)
    dp.message.register(handlers.buy_subscription, StateFilter(states.Agreement.waiting_for_agreement))
    dp.callback_query.register(handlers.disagree_with_the_terms, F.data == constants.DISAGREE_INLINE_BUTTON_CALLBACK)
    dp.callback_query.register(handlers.lets_start_again, F.data == constants.LETS_START_AGAIN_CALLBACK)

    


async def main():
    print('Bot is running!')
    print(settings.BOT_TOKEN)
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    await register_handlers(dp)
    await dp.start_polling(bot)  

if __name__ == '__main__':
    asyncio.run(main())