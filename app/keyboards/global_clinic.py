from aiogram.utils.keyboard import ReplyKeyboardBuilder

def global_clining_keyboard_bulder():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Показати тварин")
    builder.button(text="Додати новy Тварина")
    builder.button(text="Список вилікуваних тварин")
    builder.button(text="Показати всі відгуки")
    builder.button(text="Додати новий відгук")
    builder.adjust(1)
    return builder.as_markup()