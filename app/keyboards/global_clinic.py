from aiogram.utils.keyboard import ReplyKeyboardBuilder

def global_clining_keyboard_bulder():
    bulder = ReplyKeyboardBuilder()
    bulder.button(text="Показати тварин")
    bulder.button(text="Додати нову тварину на лікування")
    bulder.button(text="Вилікувати тварину")
    bulder.button(text="Видалити тварину")
    bulder.adjust(1)
    return bulder.as_markup()