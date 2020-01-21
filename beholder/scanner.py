#!/usr/bin/env python3
from logger import Logger


class Scanner:

    pid = -1
    logger = None
    memory_map = None

    def __init__(self, pid: int = -1):
        self.set_pid(pid)
        self.logger = Logger(logger_name=f"scanner({pid})",
                             logger_level="DEBUG")
        self.set_memory_map()
        print("Scanner initialized!")

    def set_pid(self, pid: int = -1) -> bool:
        if pid <= 0:
            raise Exception("I can't attach to a process with pid <= 0")
        self.pid = pid
        return True

    def get_pid(self) -> int:
        return self.pid

    def set_memory_map(self):
        self.memory_map = open(f"/proc/{self.pid}/maps", 'r')

    def get_memory_map(self) -> str:
        string_to_return = "addr\tperm\toffset\tdevice\tinode\tpath_name"
        for line in self.memory_map:
            splited_line = line.split(' ')
            addr = splited_line[0]
            perm = splited_line[1]
            offset = splited_line[2]
            device = splited_line[3]
            inode = splited_line[4]
            pathname = splited_line[-1][:-1]

            string_to_return += f"\n{addr}\t{perm}\t{offset}\t{device}\t{inode}\t{pathname}"
        return string_to_return

    def search_value(self, value, value_type: str = "int"):
        raise Exception("seach_value no implemented")


if __name__ == "__main__":
    teste = Scanner()
