from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_rating_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        KeyboardButton('Отлично'),
        KeyboardButton('Хорошо'),
        KeyboardButton('Удовлетворительно'),
        KeyboardButton('Плохо')
    ]
    keyboard.add(*buttons)
    return keyboard

async def process_food_rating(message: types.Message, state: FSMContext):
    rating_map = {'Отлично': 5, 'Хорошо': 4, ...}
    if message.text in rating_map:
        rating = rating_map[message.text]
    else:
        await message.answer("Некорректная оценка!")