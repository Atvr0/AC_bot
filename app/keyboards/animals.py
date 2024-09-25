from aiogram.utils.keyboard import InlineKeyboardBuilder


def animals_keyboard_builder(animals: list):
    builder = InlineKeyboardBuilder()

    for animal in animals:
        builder.button(text=animals,callback_data=f"anim_{animal}")

    builder.adjust(3)
    return builder.as_markup()    