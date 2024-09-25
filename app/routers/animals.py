from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.data import files_actions
from app.keyboards.animals import animals_keyboard_builder

animal_router = Router()


@animal_router.message(F.text == "Показати тварин")
async def show_animals(message: Message, state: FSMContext):
    animals = files_actions.open_file()
    keyboard = animals_keyboard_builder(animals)
    return message.answer(
        text="Виберіть вагу тварину",
        reply_parameters=keyboard

    )