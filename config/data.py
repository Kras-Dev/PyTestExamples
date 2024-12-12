# config/data.py

import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env файла

class Data:
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")

    @classmethod
    def validate(cls):
        if cls.LOGIN is None or cls.PASSWORD is None:
            raise ValueError("LOGIN and PASSWORD must be set in the environment variables.")