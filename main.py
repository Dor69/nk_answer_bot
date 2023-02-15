from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN, admin_id

storage = MemoryStorage()
bot = Bot(token= BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
state = None

#data =[]

#Method /Start

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Здравствуйте! Вы можете задать интересующие вопросы, прислать новость, фото и видео. На связи с вами редактор интернет-сайта <<Наш край>>")

#Method send message to Admin

@dp.message_handler()   
async def message_handler1(message):
    await bot.forward_message(admin_id, message_id = message.message_id, from_chat_id= message.chat.id )
    await bot.send_message(text="Вопрос от @{}".format(message.from_user["username"]), chat_id=admin_id)
    await message.reply("Ваше сообщение было отправлено")

if __name__ == '__main__':
    executor.start_polling(dp)