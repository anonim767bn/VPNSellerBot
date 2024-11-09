from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.fsm.context import FSMContext
import states
import keyboards
import text


async def start(message: Message, state: FSMContext):
    await message.answer(
        text.get_start_message(
            user = message.from_user.full_name
        ),
        reply_markup = keyboards.get_start_keyboard()
    )


async def buy_subscription(message: Message, state: FSMContext):
    await state.set_state(states.Agreement.waiting_for_agreement)
    await message.answer(
        text.get_agreement_message(),
        reply_markup = keyboards.get_agreement_keyboard()
    )


async def disagree_with_the_terms(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer(
        text.get_disagree_with_the_terms_message(),
        reply_markup = keyboards.get_disagree_with_the_terms_keyboard()
    )
    await call.answer()

async def lets_start_again(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer(
        text.get_start_again_message(
            user = call.from_user.full_name
        ),
        reply_markup = keyboards.get_start_keyboard()
    )
    await call.answer()
        
    