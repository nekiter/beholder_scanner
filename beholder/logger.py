#!/usr/bin/env python3
import logging


class Logger():
    logger = None

    formatter = None

    stream_handler = None

    def __init__(self, logger_name: str = "log", logger_level: str = "DEBUG"):
        self.logger = logging.getLogger(name=logger_name)
        self.logger.setLevel(logger_level)

        self.formatter = logging.Formatter(
            f"[Beholder] %(asctime)s %(lineno)s %(levelname)s %(message)s")

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(logger_level)
        self.stream_handler.setFormatter(self.formatter)

        self.logger.addHandler(self.stream_handler)

    def debug(self, message: str = "Empty message") -> None:
        self.logger.debug(message)
        return

    def info(self, message: str = "Empty message") -> None:
        self.logger.info(message)
        return

    def warning(self, message: str = "Empty message") -> None:
        self.logger.warning(message)
        return

    def error(self, message: str = "Empty message") -> None:
        self.logger.error(message)
        return


if __name__ == "__main__":
    pass
