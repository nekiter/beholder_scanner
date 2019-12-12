# Beholder Scanner

## What is it?

Beholder scanner is a python 3 solution for memory scanning on Linux (test mainly on Ubuntu 18.10 and 18.02, but it should work on almost every linux distros). 

## Why this exists?

The main goal of this solution is scaning process memory for automatization. This process can be a browser, a game, or any software that doesn't has caraio API for automatization.

## Why implement a process scanner?

There is some motivations to implement this from zero:

- Learning, the process of developing this helps to understand how other softwares does memory scanning, how linux kernel does memory allocation, etc...

- Implement features that makes the scanning process easier.

- Create a python interface for easy automation and development of bots.

---
## TODO list


### Majors objectives

- [ ] Implement the memory map structure, so it'll be possible to say in which logical structure (heap, stack, etc) a specific address is.

- [ ] Implement the ptrace process, to read, scan, and save the memory of an process on a given moment.

- [ ] Develop the search_value of the class Scan.

- [ ] Create and develop the CLI interface.

- [ ] Build the solution for searching for structures more complex then just pure values.

  - [ ] Array  

  - [ ] List

  - [ ] Tree

  - [ ] Stack

  - [ ] Queue

- [ ] Build a structure to save and follow-up a given address content.

- [ ] Create some C code to test the scan process.
---

### Minor objectives

- [ ] Create the wiki for the project

- [ ] Modify logger class for more useful logs (sad with that).

- [ ] Add explanation about the scanning on the wiki.

- [ ] Add videos on wiki demonstrating the use of Beholder Scanner.

- [ ] Design diagrams explaining the process of scanning of each structure for the wiki.

- [ ] Keep the TODO list updated. xD

## Contributors

[Lucas Vale - Nekiter](https://stackoverflow.com/users/9380597/lucas-ara%c3%bajo)