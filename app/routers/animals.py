from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from app.data import files_actions
from app.keyboards.animals import animals_keyboard_builder, animal_actions_keyboards

animal_router = Router()


@animal_router.message(F.text == "Показати тварин")
async def show_animals(message: Message, state: FSMContext):
    animals = files_actions.open_file()
    keyboard = animals_keyboard_builder(animals)
    return message.answer(
        text="Виберіть вагу тварину",
        reply_markup=keyboard
    )

@animal_router.callback_query(F.data.startswith("anim_"))
async def animal_actions(callbeck: CallbackQuery, state:FSMContext):
    animal = callbeck.data.split("_")[-1]
    keybord = animal_actions_keyboards(animal)
    return callbeck.message.answer(
        text=animal,
        keyboard=keybord
        )
