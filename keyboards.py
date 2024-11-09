from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import constants


def get_start_keyboard() -> ReplyKeyboardMarkup:
    Keyboard = [
        [
            KeyboardButton(text='🔒 Купить VPN')
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=Keyboard,
        resize_keyboard=True
    )