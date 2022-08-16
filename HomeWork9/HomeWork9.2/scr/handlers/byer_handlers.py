from loader import dp, data_menger, bot
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards import commands_default_keyboard
from loader import data_menger
from states import ByerState
from aiogram.dispatcher import FSMContext
from data_base import DataBase

@dp.message_handler(commands='start')
@dp.message_handler(text=['Привет', 'Начать'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}!\nСписок команд представлен на клавиатуре",
                        reply_markup=commands_default_keyboard)

@dp.message_handler(text='Просмотр контактов')
async def answer_start_text(message: types.Message):
    await message.answer(text=f'{data_menger.lookContacts()}')

@dp.message_handler(text='Поиск по имени')
async def get_item_name(message: types.Message):
    await message.answer(text='Введите имя:')
    await ByerState.wait_item_name.set()

@dp.message_handler(state=ByerState.wait_item_name)
async def get_item_name(message: types.Message, state: FSMContext):
    item_info = DataBase.lookForName(message.text)
    await message.answer(text=f'{item_info}')
    await state.reset_state()

# @dp.message_handler(text='Поиск по имени')
# async def answer_start_text(message: types.Message):
#     await message.answer(text=f'{data_menger.lookForName()}')

@dp.message_handler(text='Поиск по имени')
async def process_start_text(message: types.Message):
    temp = await message.reply("Введите имя: ")
    print(temp)
    await message.answer(text=f'{data_menger.lookForName(temp)}')
    

@dp.message_handler(text='Удаление контакта')
async def answer_start_text(message: types.Message):
    data_menger.dellContact()
    await message.answer(text='Контакт удален')

@dp.message_handler(text='Добавление контакта')
async def answer_start_text(message: types.Message):
    data_menger.addContact()
    await message.answer(text='Контакт добавлен')