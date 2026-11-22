from abc import ABC, abstractmethod
from pathlib import Path

from .logger import Logger
from .strategies import (
    ConsoleOutputStrategy,
    FileOutputStrategy,
    OutputStrategy,
    UppercaseFileOutputStrategy,
)


class LoggerCreator(ABC):
    @abstractmethod
    def create_strategy(self) -> OutputStrategy:
        pass

    def create_logger(self) -> Logger:
        return Logger(self.create_strategy())


class ConsoleLoggerCreator(LoggerCreator):
    def create_strategy(self) -> OutputStrategy:
        return ConsoleOutputStrategy()


class FileLoggerCreator(LoggerCreator):
    def __init__(self, path: str | Path) -> None:
        self.path = path

    def create_strategy(self) -> OutputStrategy:
        return FileOutputStrategy(self.path)


class UppercaseFileLoggerCreator(LoggerCreator):
    def __init__(self, path: str | Path) -> None:
        self.path = path

    def create_strategy(self) -> OutputStrategy:
        return UppercaseFileOutputStrategy(self.path)
