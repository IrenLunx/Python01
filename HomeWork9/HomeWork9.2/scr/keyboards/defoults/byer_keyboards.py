from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Просмотр контактов'),
            KeyboardButton(text='Поиск по имени')
        ],
        [
            KeyboardButton(text='Удаление контакта'),
            KeyboardButton(text='Добавление контакта')
        ],
    ],
    resize_keyboard=True
)