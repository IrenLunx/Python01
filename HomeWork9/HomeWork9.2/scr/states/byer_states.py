from aiogram.dispatcher.filters.state import StatesGroup, State

class ByerState(StatesGroup):
    wait_item_name = State()
    wait_item_name_dell = State()
    wait_item_name_add = State()
    wait_item_name_add_num = State()
    wait_item_name_add_comm = State()