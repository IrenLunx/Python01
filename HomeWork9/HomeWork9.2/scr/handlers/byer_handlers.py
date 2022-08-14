from loader import dp
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards import commands_default_keyboard
from loader import data_menger

@dp.message_handler(commands='start')
@dp.message_handler(text=['Привет', 'Начать'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}!\nСписок команд представлен на клавиатуре",
                        reply_markup=commands_default_keyboard)

@dp.message_handler(text='Просмотр контактов')
async def answer_start_text(message: types.Message):
    await message.answer(text=f'{data_menger.lookContacts()}')

@dp.message_handler(text='Поиск по имени')
async def answer_start_text(message: types.Message):
    await message.answer(text=f'{data_menger.lookForName()}')
    
@dp.message_handler(text='Удаление контакта')
async def answer_start_text(message: types.Message):
    data_menger.dellContact()
    await message.answer(text='Контакт удален')

@dp.message_handler(text='Добавление контакта')
async def answer_start_text(message: types.Message):
    data_menger.addContact()
    await message.answer(text='Контакт добавлен')