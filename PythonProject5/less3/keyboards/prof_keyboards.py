from aiogram.types  import ReplyKeyboardMarkup, KeyboardButton

def make_row_keyboard(button: list[str])-> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=button) for button in buttons]
    return ReplyKeyboardMarkup(keyboard=[button], resize_keyboard=True)