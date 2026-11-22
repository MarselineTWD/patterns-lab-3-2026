from logger import (
    ConsoleLoggerCreator,
    FileLoggerCreator,
    LogLevel,
    UppercaseFileLoggerCreator,
)


def main() -> None:
    console_logger = ConsoleLoggerCreator().create_logger()
    file_logger = FileLoggerCreator("logs/app.log").create_logger()
    uppercase_logger = UppercaseFileLoggerCreator("logs/app.log").create_logger()

    console_logger.log(LogLevel.INFO, "Application started")
    file_logger.log(LogLevel.WARN, "Low disk space")
    uppercase_logger.log(LogLevel.ERROR, "Example error")


if __name__ == "__main__":
    main()
