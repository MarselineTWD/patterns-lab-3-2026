from pathlib import Path

from logger import (
    ConsoleLoggerCreator,
    ConsoleOutputStrategy,
    FileLoggerCreator,
    FileOutputStrategy,
    Logger,
    UppercaseFileLoggerCreator,
    UppercaseFileOutputStrategy,
)


def test_console_creator_builds_logger() -> None:
    logger = ConsoleLoggerCreator().create_logger()

    assert isinstance(logger, Logger)
    assert isinstance(logger.strategy, ConsoleOutputStrategy)


def test_file_creator_builds_file_strategy(tmp_path: Path) -> None:
    log_file = tmp_path / "app.log"

    strategy = FileLoggerCreator(log_file).create_strategy()

    assert isinstance(strategy, FileOutputStrategy)
    assert strategy.path == log_file


def test_uppercase_creator_builds_uppercase_strategy(tmp_path: Path) -> None:
    strategy = UppercaseFileLoggerCreator(tmp_path / "app.log").create_strategy()

    assert isinstance(strategy, UppercaseFileOutputStrategy)
