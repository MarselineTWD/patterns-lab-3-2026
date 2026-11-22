from logger import LogLevel, Logger, OutputStrategy


class RecordingStrategy(OutputStrategy):
    def __init__(self) -> None:
        self.message = ""

    def write(self, message: str) -> None:
        self.message = message


def test_logger_passes_formatted_message_to_strategy() -> None:
    strategy = RecordingStrategy()
    logger = Logger(strategy)

    result = logger.log(LogLevel.INFO, "Приложение запущено")

    assert "[INFO] Приложение запущено" in result
    assert strategy.message == result
