from abc import ABC, abstractmethod
from pathlib import Path


class OutputStrategy(ABC):
    @abstractmethod
    def write(self, message: str) -> None:
        pass


class ConsoleOutputStrategy(OutputStrategy):
    def write(self, message: str) -> None:
        print(message)


class FileOutputStrategy(OutputStrategy):
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def write(self, message: str) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as stream:
            stream.write(message + "\n")


class UppercaseFileOutputStrategy(FileOutputStrategy):
    def write(self, message: str) -> None:
        super().write(message.upper())
