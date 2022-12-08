import re

real_start = """
[B]                     [N]     [H]
[V]         [P] [T]     [V]     [P]
[W]     [C] [T] [S]     [H]     [N]
[T]     [J] [Z] [M] [N] [F]     [L]
[Q]     [W] [N] [J] [T] [Q] [R] [B]
[N] [B] [Q] [R] [V] [F] [D] [F] [M]
[H] [W] [S] [J] [P] [W] [L] [P] [S]
[D] [D] [T] [F] [G] [B] [B] [H] [Z]
 1   2   3   4   5   6   7   8   9 """[1:].split('\n')[:-1]
# 1, 5, 9, 13, ..., every four

def solution(input_start, cratemover_version):

    start = input_start.copy()

    for row_idx in range(len(start)):
        row = start[row_idx]
        start[row_idx] = list(row[1:-1][::4])

    stacks = [[], [], [], [], [], [], [], [], []]
    for row in start:
        for object_id, object_letter in enumerate(row):
            if object_letter != " ":
                stacks[object_id] = [object_letter] + stacks[object_id]

    for i in start:
        pass
        # print(i)
        # ['B', ' ', ' ', ' ', ' ', ' ', 'N', ' ', 'H']
        # ['V', ' ', ' ', 'P', 'T', ' ', 'V', ' ', 'P']
        # ['W', ' ', 'C', 'T', 'S', ' ', 'H', ' ', 'N']
        # ['T', ' ', 'J', 'Z', 'M', 'N', 'F', ' ', 'L']
        # ['Q', ' ', 'W', 'N', 'J', 'T', 'Q', 'R', 'B']
        # ['N', 'B', 'Q', 'R', 'V', 'F', 'D', 'F', 'M']
        # ['H', 'W', 'S', 'J', 'P', 'W', 'L', 'P', 'S']
        # ['D', 'D', 'T', 'F', 'G', 'B', 'B', 'H', 'Z']

    for i in stacks:
        pass
        # print(i)
        # ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B']
        # ['D', 'W', 'B']
        # ['T', 'S', 'Q', 'W', 'J', 'C']
        # ['F', 'J', 'R', 'N', 'Z', 'T', 'P']
        # ['G', 'P', 'V', 'J', 'M', 'S', 'T']
        # ['B', 'W', 'F', 'T', 'N']
        # ['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N']
        # ['H', 'P', 'F', 'R']
        # ['Z', 'S', 'M', 'B', 'L', 'N', 'P', 'H']

    # I'll just stop and say here, there was definitely at least five ways this could've been done more efficiently
    # I imagine there's a nice numpy transpose that could've done it but I'm a noob

    with open('input.txt', 'r') as f:
        instructions = f.read().splitlines()

    for instruction in instructions:
        # example instruction: move 2 from 8 to 1
        instruction_list = list(map(int, re.split(r"move | from | to ", instruction)[1:]))
        number_of_crates = instruction_list[0]
        source_stack = instruction_list[1]
        destination_stack = instruction_list[2]

        if cratemover_version == 'CrateMover 9000':
            for _ in range(number_of_crates):
                stacks[destination_stack-1].append(stacks[source_stack-1].pop())
        elif cratemover_version == 'CrateMover 9001':
            stacks[destination_stack-1] += stacks[source_stack-1][-number_of_crates:]
            stacks[source_stack-1] = stacks[source_stack-1][:-number_of_crates]
        else:
            raise NotImplementedError("Sorry, this is not a supported CrateMover version")

    solution = ''
    for stack in stacks:
        solution += stack[-1]

    return solution


print(solution(real_start, 'CrateMover 9000'))  # PSNRGBTFT

# #############################
# ########## Part 2 ###########
# #############################

print(solution(real_start, 'CrateMover 9001'))  # BNTZFPMMW
