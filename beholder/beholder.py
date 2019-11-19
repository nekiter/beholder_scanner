#!/usr/bin/env python3
from scanner import Scanner
from logger import Logger


class Beholder:

    scanner = None

    logger = None

    def __init__(self):
        self.logger = Logger(logger_name="beholder", logger_level="DEBUG")

        self.scanner = Scanner()

        self.logger.info("Beholder initialized!")

    def attach_to_process(self, pid: int = -1) -> bool:
        self.scanner.set_pid(pid)
        return True


if __name__ == "__main__":
    teste = Beholder()
