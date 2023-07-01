import time
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

TOKEN = '5725307648:AAGx7QONU7ONM8CagfRIGvu9ecfraC0jCDA' 
CHAT_ID = '758457005'  

bot = Bot(token=TOKEN)
dispatcher=Dispatcher(bot=bot)
b1=KeyboardButton('/start')
kb=ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(b1)

@dispatcher.message_handler(commands=['start'])
async def start_handler(message:types.Message):
    
    user_fullname=message.from_user.full_name
    await message.reply(f'Hello {user_fullname}',reply_markup=kb)
    


if __name__ == '__main__':
    executor.start_polling(dispatcher)