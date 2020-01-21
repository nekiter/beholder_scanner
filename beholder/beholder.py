#!/usr/bin/env python3
from scanner import Scanner
from logger import Logger


class Beholder:

    scanners = None
    logger = None

    def __init__(self):
        self.logger = Logger(logger_name="beholder", logger_level="DEBUG")
        self.scanners = []
        self.logger.info("Beholder initialized!")

    def attach_to_process(self, pid: int = -1) -> bool:
        if pid <= -1:
            self.logger.error("Invalid PID!")
            return False

        for scanner in self.scanners:
            if scanner.get_pid() == pid:
                self.logger.warning("This process is already attached!")
                return False

        scanner = Scanner(pid=pid)
        self.scanners.append(scanner)
        return True

    def scan_value(self, value=None, value_type: str = "int") -> dict:
        if len(self.scanners) == 0:
            self.logger.warning("Can't scan without attach to a process.")
            return {}

        if value is None:
            self.logger.error("Can't scan None value.")
            return {}

        for scanner in self.scanners:
            scanner.search_value(value=value, value_type=value_type)

        return {}


if __name__ == "__main__":
    teste = Beholder()
    while True:
        print("="*100)
        print("Choose one option:")
        print("1- Attach to a process")
        print("2- Scan a value")
        print("="*100)
        option = int(input())

        if option < 0 or option > 2:
            print("Invalid option!")
            break

        if option == 1:
            print("\nWrite the PID of the process")
            pid = int(input())
            teste.attach_to_process(pid=pid)
        elif option == 2:
            print("\nWrite the value to search")
            value_to_scan = int(input())
            teste.scan_value(value=value_to_scan, value_type="int")
