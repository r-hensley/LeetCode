from __future__ import annotations
from dataclasses import dataclass
from typing import Union, Optional


test_input = """$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split('\n')

@dataclass
class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"file:{self.name}"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, target_file: File):
        if self.name == target_file.name and self.size == target_file.size:
            return True


@dataclass
class Directory:
    def __init__(self, name: str, contents: list[File, Directory] = None, parent: Optional[Directory] = None):
        if contents is None:
            contents = []

        self.name = name
        self.contents = contents
        self.parent = parent

    def append(self, addition: Union[File, Directory]):
        if addition not in self.contents:
            self.contents.append(addition)

    @property
    def size(self) -> int:
        """Returns recursively size of all files and directories inside current directory"""
        _size = 0
        for item in self.contents:
            item_size = item.size
            _size += item_size
        return _size

    def small_files(self, target_dir: Directory = None, total_size: int = 0) -> int:
        if not target_dir:
            target_dir = self

        for item in target_dir.contents:
            if type(item) == Directory:
                item: Directory
                if item.size <= 100000:
                    total_size += item.size
                total_size = self.small_files(item, total_size)

        return total_size

    def top(self) -> Directory:
        """Jumps to the top directory"""
        cwd = self
        while cwd.name != "\\":
            cwd = cwd.parent

        return cwd

    def __getitem__(self, desired_item: str):
        for item in self.contents:
            if item.name == desired_item:
                if type(item) == File:
                    raise TypeError(f"You cannot use cd to open a File "
                                    f"(tried to open {desired_item} in {self.name}: {self.contents})")
                else:
                    item: Directory
                    return item

        raise KeyError(f"Item with desired name ({desired_item}) not found in directory {self.name}: ({self.contents})")

    def __repr__(self):
        return f"dir:{self.name}"

    def __str__(self):
        return self.__repr__()

    def __contains__(self, desired_item):
        for item in self.contents:
            if type(item) == type(desired_item) and item.name == desired_item.name:
                return True

    def __eq__(self, target_dir: Directory):
        if self.name == target_dir.name and self.parent == target_dir.parent:
            return True


with open('input.txt', 'r') as f:
    real_input = f.read().splitlines()


def part_one(instructions: list[str]):
    listing = False  # True if user has called "ls" and terminal is listing dir contents
    cwd: Directory = Directory("\\", [])
    for instruction in instructions:
        if listing:
            if instruction.startswith("$ "):
                listing = False
            else:
                split_instruction = instruction.split()
                if split_instruction[0] == 'dir':
                    cwd.append(Directory(split_instruction[1], None, cwd))
                else:
                    cwd.append(File(split_instruction[1], int(split_instruction[0])))

        if not listing:
            if instruction.startswith("$ ls"):
                listing = True
            else:
                if instruction == '$ cd ..':
                    if not cwd.parent:
                        raise Exception(f"cwd.parent not defined for {cwd}")
                    cwd = cwd.parent
                else:
                    target_dir = instruction.split("$ cd ")[1]
                    cwd = cwd[target_dir]


    cwd = cwd.top()
    print("Part 1 answer:", cwd.small_files())

    total_size = cwd.size
    free_space = 70000000 - total_size
    needed_size = 30000000 - free_space
    all_dirs = []

    def add_dirs_to_list(target_dir: Directory):
        for item in target_dir.contents:
            if type(item) == Directory:
                item: Directory
                all_dirs.append(item)
                add_dirs_to_list(item)

    add_dirs_to_list(cwd)
    all_dirs.sort(key=lambda x: x.size)

    for d in all_dirs:
        if d.size > needed_size:
            print('part 2 sol:', d.size)  # 4443914
            break

    return cwd


cwd = part_one(real_input)


# testdir = Directory("test")
# file1 = File("file1", 3)
# file2 = File("file2", 5)
# print(testdir.contents, file1 in testdir, file2 in testdir)
# testdir.append(file1)
# print(testdir.contents, file1 in testdir, file2 in testdir)
# testdir.append(file2)
# print(testdir.contents, file1 in testdir, file2 in testdir)