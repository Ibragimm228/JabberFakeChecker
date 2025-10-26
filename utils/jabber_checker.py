import re
from dataclasses import dataclass
from typing import List


@dataclass
class CyrillicChar:
    char: str
    position: int
    latin_lookalike: str = ""


class JabberChecker:
    """Проверяет Jabber ID на наличие кириллических символов."""
    
    CYRILLIC_PATTERN = re.compile(r'[а-яА-ЯёЁ]')
    
    LOOKALIKE_MAP = {
        'а': 'a', 'А': 'A',
        'е': 'e', 'Е': 'E',
        'о': 'o', 'О': 'O',
        'р': 'p', 'Р': 'P',
        'с': 'c', 'С': 'C',
        'у': 'y', 'У': 'Y',
        'х': 'x', 'Х': 'X',
        'В': 'B', 'К': 'K',
        'М': 'M', 'Н': 'H',
        'Т': 'T'
    }
    
    @classmethod
    def check(cls, jabber_id: str) -> tuple[bool, List[CyrillicChar]]:
        """
        Проверяет Jabber ID на кириллицу.
        
        Returns:
            tuple[bool, List[CyrillicChar]]: (есть_кириллица, список_символов)
        """
        cyrillic_chars = []
        
        for idx, char in enumerate(jabber_id):
            if cls.CYRILLIC_PATTERN.match(char):
                lookalike = cls.LOOKALIKE_MAP.get(char, "")
                cyrillic_chars.append(
                    CyrillicChar(char=char, position=idx, latin_lookalike=lookalike)
                )
        
        return len(cyrillic_chars) > 0, cyrillic_chars
    
    @classmethod
    def format_result(cls, jabber_id: str, has_cyrillic: bool, 
                     cyrillic_chars: List[CyrillicChar]) -> str:
        """Форматирует результат проверки для отображения."""
        
        if not has_cyrillic:
            return (
                f"✅ <b>Jabber чистый</b>\n\n"
                f"<code>{jabber_id}</code>\n\n"
                f"Кириллических символов не обнаружено. "
                f"Можно использовать безопасно."
            )
        
        highlighted = cls._highlight_cyrillic(jabber_id, cyrillic_chars)
        details = cls._format_details(cyrillic_chars)
        
        return (
            f"⚠️ <b>Внимание! Обнаружена кириллица</b>\n\n"
            f"{highlighted}\n\n"
            f"<b>Найдено символов:</b> {len(cyrillic_chars)}\n"
            f"{details}\n\n"
            f"🚨 Это может быть подделка! Будьте осторожны."
        )
    
    @classmethod
    def _highlight_cyrillic(cls, jabber_id: str, 
                           cyrillic_chars: List[CyrillicChar]) -> str:
        """Подсвечивает кириллические символы в строке."""
        result = []
        cyrillic_positions = {c.position for c in cyrillic_chars}
        
        for idx, char in enumerate(jabber_id):
            if idx in cyrillic_positions:
                result.append(f"<u><b>{char}</b></u>")
            else:
                result.append(char)
        
        return f"<code>{''.join(result)}</code>"
    
    @classmethod
    def _format_details(cls, cyrillic_chars: List[CyrillicChar]) -> str:
        """Форматирует детали найденных символов."""
        lines = []
        
        for char_info in cyrillic_chars[:5]:  # Показываем максимум 5
            line = f"  • <code>{char_info.char}</code> на позиции {char_info.position + 1}"
            
            if char_info.latin_lookalike:
                line += f" (похож на <code>{char_info.latin_lookalike}</code>)"
            
            lines.append(line)
        
        if len(cyrillic_chars) > 5:
            lines.append(f"  • ... и ещё {len(cyrillic_chars) - 5}")
        
        return "\n".join(lines)

