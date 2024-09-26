from aiogram.utils.keyboard import InlineKeyboardBuilder


def animals_keyboard_builder(animals: list):
    builder = InlineKeyboardBuilder()

    for animal in animals:
        builder.button(text=animal,callback_data=f"anim_{animal}")

    builder.adjust(3)
    return builder.as_markup()  


    def animal_actions_keyboards(animal: str):
        builder = InlineKeyboardBuilder()  
        builder.button(text="Перенести в список вилікуваних", callback_data=f"cured_animals_{animal}")
        builder.button(text="Видалити", callback_data=f"del_animals_{animal}")
        return builder.as_markup()
        
