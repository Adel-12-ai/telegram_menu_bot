import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import config

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    button1 = types.InlineKeyboardButton(text = config.btn1_name, callback_data = "btn1")
    button2 = types.InlineKeyboardButton(text = config.btn2_name, callback_data = "btn2")
    button3 = types.InlineKeyboardButton(text = config.btn3_name, callback_data = "btn3")
    button4 = types.InlineKeyboardButton(text = config.btn4_name, callback_data = "btn4")
    builder.row(button1, button2)
    builder.row(button3, button4)
    await bot.send_photo(message.chat.id, photo = config.photo_url, caption = config.menu_text, reply_markup = builder.as_markup())

@dp.callback_query(F.data == "btn1")
async def cmd_price(callback: types.CallbackQuery):
    await callback.message.answer(config.btn1_response, parse_mode = 'HTML')

@dp.callback_query(F.data == "btn2")
async def cmd_price(callback: types.CallbackQuery):
    await callback.message.answer(config.btn2_response, parse_mode = 'HTML')

@dp.callback_query(F.data == "btn3")
async def cmd_price(callback: types.CallbackQuery):
    await callback.message.answer(config.btn3_response, parse_mode = 'HTML')

@dp.callback_query(F.data == "btn4")
async def cmd_price(callback: types.CallbackQuery):
    await callback.message.answer(config.btn4_response, parse_mode = 'HTML')

async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())