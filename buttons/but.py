from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("📈Статистика")
b2 = KeyboardButton("🏆Уровень")

keybrd = ReplyKeyboardMarkup(resize_keyboard=True)

keybrd.add(b1).insert(b2)
