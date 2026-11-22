from pathlib import Path

import pytest

from logger import (
    ConsoleOutputStrategy,
    FileOutputStrategy,
    UppercaseFileOutputStrategy,
)


def test_console_strategy_prints_message(
    capsys: pytest.CaptureFixture[str],
) -> None:
    ConsoleOutputStrategy().write("Сообщение")

    assert capsys.readouterr().out == "Сообщение\n"


def test_file_strategy_writes_message(tmp_path: Path) -> None:
    log_file = tmp_path / "app.log"

    FileOutputStrategy(log_file).write("Сообщение")

    assert log_file.read_text(encoding="utf-8") == "Сообщение\n"


def test_uppercase_file_strategy_changes_message_to_uppercase(
    tmp_path: Path,
) -> None:
    log_file = tmp_path / "app.log"

    UppercaseFileOutputStrategy(log_file).write("Важное сообщение")

    assert log_file.read_text(encoding="utf-8") == "ВАЖНОЕ СООБЩЕНИЕ\n"
