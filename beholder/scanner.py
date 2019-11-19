#!/usr/bin/env python3
class Scanner:

    pid = -1

    memory_map = None

    def __init__(self):
        print("Scanner initialized!")

    def set_pid(int: pid = -1) -> bool:
        if pid <= 0:
            raise Exception("I can't attach to a process with pid <= 0")
        self.píd = pid
        return True

    def get_pid() -> int:
        return pid

    def set_memory_map(self):
        self.memory_map = open(f"/proc/{self.pid}/maps", 'r')


if __name__ == "__main__":
    teste = Scanner()
