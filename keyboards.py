from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import constants


def get_start_keyboard() -> ReplyKeyboardMarkup:
    Keyboard = [
        [
            KeyboardButton(text = constants.SUBSCRIBE_BUTTON_TEXT)
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard = Keyboard,
        resize_keyboard = True,
        one_time_keyboard = True
    )


def get_agreement_keyboard() -> InlineKeyboardMarkup:
    Keyboard = [
        [
            InlineKeyboardButton(text = constants.TERMS_INLINE_BUTTON_TEXT, callback_data = constants.TERMS_INLINE_BUTTON_CALLBACK),
            InlineKeyboardButton(text = constants.AGREE_INLINE_BUTTON_TEXT, callback_data = constants.AGREE_INLINE_BUTTON_CALLBACK),
            InlineKeyboardButton(text = constants.DISAGREE_INLINE_BUTTON_TEXT, callback_data = constants.DISAGREE_INLINE_BUTTON_CALLBACK)
        ]
    ]
    return InlineKeyboardMarkup(
        inline_keyboard = Keyboard
    )


def get_disagree_with_the_terms_keyboard() -> InlineKeyboardMarkup:
    Keyboard = [
        [
            InlineKeyboardButton(text = constants.LETS_START_AGAING_BUTTON_TEXT, callback_data = constants.LETS_START_AGAIN_CALLBACK)
        ]
    ]
    return InlineKeyboardMarkup(
        inline_keyboard = Keyboard
    )
