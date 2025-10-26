from aiogram import Router
from . import commands, checker


def get_router() -> Router:
    """Возвращает главный роутер со всеми обработчиками."""
    router = Router()
    
    router.include_router(commands.router)
    router.include_router(checker.router)
    
    return router

