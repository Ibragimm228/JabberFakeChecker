from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Обработчик команды /start."""
    await message.answer(
        "👋 <b>Jabber Fake Checker</b>\n\n"
        "Проверяю Jabber ID на наличие кириллических символов.\n\n"
        "<b>Как пользоваться:</b>\n"
        "• Отправь мне Jabber ID\n"
        "• Получи результат проверки\n\n"
        "Кидалы часто используют кириллицу вместо латиницы. "
        "Например, <code>usеr@jabber.ru</code> с русской <b>е</b> "
        "выглядит как <code>user@jabber.ru</code>, но это разные адреса.\n\n"
        "Попробуй: <code>/check user@jabber.ru</code>",
        parse_mode="HTML"
    )


@router.message(Command("check"))
async def cmd_check(message: Message) -> None:
    """Обработчик команды /check."""
    await message.answer(
        "Отправь мне Jabber ID для проверки.\n"
        "Например: <code>user@jabber.ru</code>",
        parse_mode="HTML"
    )

