from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

from config import BOT_TOKEN, admin_id

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Словарь для хранения выбора типа сообщения пользователем
user_message_type = {}

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    markup = types.ReplyKeyboardRemove()
    await message.reply("Привет! Опишите вашу проблему или предложение:", reply_markup=markup)

# Обработчик для получения текстового сообщения от пользователя
@dp.message_handler(lambda message: message.text)
async def handle_text_message(message: types.Message):
    # Проверяем, выбрал ли пользователь тип сообщения
    if message.chat.id in user_message_type:
        message_type = user_message_type[message.chat.id]
        
        # Отправляем сообщение администратору с указанием типа и текста сообщения
        await bot.send_message(admin_id, f"Сообщение типа '{message_type}' от @{message.from_user.username}: {message.text}")
        await message.reply(f"Ваше сообщение типа '{message_type}' отправлено администратору.")
        # Удаляем выбор типа сообщения
        del user_message_type[message.chat.id]
        markup = types.ReplyKeyboardRemove()
    else:
        # Если пользователь еще не выбрал тип сообщения, предлагаем это сделать
        markup = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("Проблема")
        item2 = types.KeyboardButton("Предложение")
        markup.add(item1, item2)
        await message.reply("Выберите тип вашего сообщения:", reply_markup=markup)
        # Добавляем выбор типа сообщения в словарь
        user_message_type[message.chat.id] = message.text

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
