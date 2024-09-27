from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import files_actions
from app.keyboards.animals import animals_keyboard_builder, animal_actions_keyboards

animal_router = Router()


@animal_router.message(F.text == "Показати тварин")
async def show_animals(message: Message, state: FSMContext):
    animals = files_actions.open_file()
    keyboard = animals_keyboard_builder(animals)
    await message.answer(
        text="Виберіть вагу тварину",
        reply_markup=keyboard
    )

@animal_router.callback_query(F.data.startswith("anim_"))
async def animal_actions(callbeck: CallbackQuery, state:FSMContext):
    animal = callbeck.data.split("_")[-1]
    keyboard = animal_actions_keyboards(animal)
    await callbeck.message.answer(
        text=animal,
        reply_markup=keyboard
        )

@animal_router.callback_query(F.data.startswith("sold_anim_"))    
async def animals_cured(callback: CallbackQuery, state: FSMContext):
    animal = callback.data.split("_")[-1]   
    msg = files_actions.animals_cured(animal)
    await callback.messege.answer(text=msg)


@animal_router.callback_query(F.data.startswith("del_anim_"))
async def del_animal(callback: CallbackQuery, state: FSMContext):
    animal = callback.data.split("_")[-1]
    msg = files_actions.del_animal(animal)
    await callback.message.answer(text=msg)
