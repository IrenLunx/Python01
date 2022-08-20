from loader import dp, data_menger, bot
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards import commands_default_keyboard
from loader import data_menger
from states import ByerState
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands='start')
@dp.message_handler(text=['Привет', 'Начать'])
async def answer_start_command(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}!\nСписок команд представлен на клавиатуре",
                        reply_markup=commands_default_keyboard)

@dp.message_handler(text='Просмотр контактов')
async def look_contacts_text(message: types.Message):
    await message.answer(text=f'{data_menger.lookContacts()}')

@dp.message_handler(text='Поиск по имени')
async def get_item_name(message: types.Message):
    await message.answer(text='Введите имя:')
    await ByerState.wait_item_name.set()

@dp.message_handler(state=ByerState.wait_item_name)
async def get_item_name(message: types.Message, state: FSMContext):
    item_info = data_menger.lookForName(message.text)
    await message.answer(text=f'{item_info}')
    await state.reset_state()

@dp.message_handler(text='Удаление контакта')
async def dell_contact_text(message: types.Message):
    await message.answer(text='Введите имя или номер для удаления:')
    await ByerState.wait_item_name_dell.set()

@dp.message_handler(state=ByerState.wait_item_name_dell)
async def dell_contact_text(message: types.Message, state: FSMContext):
    trueFalse = data_menger.dellContact(message.text)
    if trueFalse:
        await message.answer(text=f'Контакт {message.text} удалён!')
    else: 
        await message.answer(text=f'Контакта {message.text} не существует!')
    await state.reset_state()

@dp.message_handler(text='Добавление контакта')
async def add_contact_text(message: types.Message):
    await message.answer(text='Введите фамилию, имя, номер и комментарий к нему:')
    await ByerState.wait_item_name_add.set()

@dp.message_handler(state=ByerState.wait_item_name_add)
async def add_contact_text(message: types.Message, state: FSMContext):
    data_menger.addContact(message.text)
    await message.answer(text=f'Контакт {message.text} добавлен!')
    await state.reset_state()