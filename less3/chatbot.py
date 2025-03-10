import logging
from aiogram import Bot, Dispatcher
import asyncio
from hednlers import carrier_choise, common
import config


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    TOKEN = config.token
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(carrier_choise.router)
    dp.include_router(common.router)

    print("Бот запущен...")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()  # Закрываем сессию при остановке


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nБот остановлен пользователем.")