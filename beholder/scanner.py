#!/usr/bin/env python3
class Scanner:

    pid = -1

    memory_map = None

    def __init__(self, int: pid = -1):
        self.set_pid(pid)
        self.set_memory_map()
        print("Scanner initialized!")

    def set_pid(self, int: pid = -1) -> bool:
        if pid <= 0:
            raise Exception("I can't attach to a process with pid <= 0")
        self.píd = pid
        return True

    def get_pid(self) -> int:
        return pid

    def set_memory_map(self):
        self.memory_map = open(f"/proc/{self.pid}/maps", 'r')

    def search_value(self, value, str: type = "int"):
        raise Exception("seach_value no implemented")


if __name__ == "__main__":
    teste = Scanner()
