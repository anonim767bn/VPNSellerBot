from aiogram.types import Message
import keyboards
import text


async def start(message: Message):
    await message.answer(
        text.get_start_message(
            user = message.from_user.full_name
        ),
        reply_markup = keyboards.get_start_keyboard()
    )
