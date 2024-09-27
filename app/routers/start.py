from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from app.keyboards.global_clinic import global_clining_keyboard_bulder

start_router = Router()

@start_router.message(CommandStart())
async def start_hendler(message: Message, state: FSMContext):
    keybord = global_clining_keyboard_bulder()
    await message.answer(
        text=f"Вітаю у ветеринарній клініці '{message.from_user.full_name}'",
        reply_markup=keybord
        )
