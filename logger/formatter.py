from datetime import datetime

from .levels import LogLevel


class MessageFormatter:
    def format(self, level: LogLevel, message: str) -> str:
        if not isinstance(level, LogLevel):
            raise ValueError(f"Недопустимый уровень журналирования: {level}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} [{level.value}] {message}"
