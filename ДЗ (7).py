import requests
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = "8161962043:AAHycNP_lnYBKvKjrybfjugwXBZQXnlAolc"
bot = Bot(token='8161962043:AAHycNP_lnYBKvKjrybfjugwXBZQXnlAolc')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url).json()
    return {
        "USD_UZS": response["rates"]["UZS"],
        "EUR_USD": response["rates"]["EUR"],
        "EUR_UZS": response["rates"]["UZS"] / response["rates"]["EUR"],
    }

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Сум ➝ Евро"), KeyboardButton("Евро ➝ Доллар"))
keyboard.add(KeyboardButton("Доллар ➝ Сум"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я конвертер валют.\nВыбери нужное направление:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in ["Сум ➝ Евро", "Евро ➝ Доллар", "Доллар ➝ Сум"])
async def convert_currency(message: types.Message):
    rates = get_exchange_rates()
    conversion_type = message.text

    await message.reply("Введите сумму для конвертации:")

    @dp.message_handler()
    async def process_amount(msg: types.Message):
        try:
            amount = float(msg.text)
            if conversion_type == "Сум ➝ Евро":
                result = amount / rates["EUR_UZS"]
                await msg.reply(f"{amount} сум ≈ {result:.2f} евро")
            elif conversion_type == "Евро ➝ Доллар":
                result = amount * rates["EUR_USD"]
                await msg.reply(f"{amount} евро ≈ {result:.2f} долларов")
            elif conversion_type == "Доллар ➝ Сум":
                result = amount * rates["USD_UZS"]
                await msg.reply(f"{amount} долларов ≈ {result:.2f} сум")
        except ValueError:
            await msg.reply("Ошибка! Введите корректную сумму.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)