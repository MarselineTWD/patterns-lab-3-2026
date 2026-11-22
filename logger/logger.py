from .formatter import MessageFormatter
from .levels import LogLevel
from .strategies import OutputStrategy


class Logger:
    def __init__(
        self,
        strategy: OutputStrategy,
        formatter: MessageFormatter | None = None,
    ) -> None:
        self.strategy = strategy
        self.formatter = formatter or MessageFormatter()

    def log(self, level: LogLevel, message: str) -> str:
        formatted = self.formatter.format(level, message)
        self.strategy.write(formatted)
        return formatted
