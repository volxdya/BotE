import time
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message

class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, time_limit: int = 1):
        self.limit = time_limit
        self.last_from_user: Dict[int, float] = {}

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        current_time = time.time()

        # Проверяем наличие пользователя в базе
        if user_id in self.last_from_user:
            last_time = self.last_from_user[user_id]
            if current_time - last_time < self.limit:
                # Если спамит — просто игнорируем или пишем сообщение
                return  # Бот просто промолчит
        
        # Записываем время текущего сообщения
        self.last_from_user[user_id] = current_time
        
        # Передаем управление дальше хендлерам
        return await handler(event, data)