from aiogram import Router, F
from aiogram.types import Message

from utils import JabberChecker

router = Router()


@router.message(F.text)
async def check_jabber(message: Message) -> None:
    """Проверяет полученный текст на кириллицу."""
    
    if not message.text:
        return
    
    jabber_id = message.text.strip()
    
    if not jabber_id:
        await message.answer("Пожалуйста, отправь корректный Jabber ID.")
        return
    
    if len(jabber_id) > 500:
        await message.answer(
            "⚠️ Слишком длинная строка. "
            "Максимум 500 символов."
        )
        return
    
    has_cyrillic, cyrillic_chars = JabberChecker.check(jabber_id)
    result = JabberChecker.format_result(jabber_id, has_cyrillic, cyrillic_chars)
    
    await message.answer(result, parse_mode="HTML")

