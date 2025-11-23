from aiogram import Router
from . import commands, checker


def get_router() -> Router:
    router = Router()
    
    router.include_router(commands.router)
    router.include_router(checker.router)
    
    return router

