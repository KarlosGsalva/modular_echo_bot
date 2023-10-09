import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_hadlers


# функция кофигурирования и запуска бота
async def main() -> None:

    # загружаем конфиг в переменную config
    config: Config = load_config()

    # инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # регистрируем роутеры в диспетчере
    dp.include_router(user_hadlers.router)
    dp.include_router(other_handlers.router)

    # пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

