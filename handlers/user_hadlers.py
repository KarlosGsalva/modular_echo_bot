from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU


# инициализируем роутер модуля
router = Router()


# хендлер на команду /start
@router.message(CommandStart)
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# хендлер на команду /help
@router.message(Command(commands='help'))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
