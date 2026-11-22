import re

import pytest

from logger import LogLevel, MessageFormatter


@pytest.mark.parametrize("level", list(LogLevel))
def test_message_format_contains_time_level_and_text(level: LogLevel) -> None:
    result = MessageFormatter().format(level, "Проверка")

    pattern = rf"^\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}}:\d{{2}} \[{level.value}\] Проверка$"
    assert re.match(pattern, result)


def test_unknown_log_level_is_rejected() -> None:
    with pytest.raises(ValueError, match="Недопустимый уровень"):
        MessageFormatter().format("DEBUG", "Проверка")  # type: ignore[arg-type]
