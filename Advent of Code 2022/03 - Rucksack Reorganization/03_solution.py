test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split()

with open('input.txt', 'r') as f:
    real_input = f.read().splitlines()

priorities = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def sum_of_priorities(rucksacks: list[str]):
    priority_sum = 0

    for rucksack in rucksacks:
        comp_one = rucksack[0:int(len(rucksack)/2)]
        comp_two = rucksack[int(len(rucksack)/2):]
        for item in comp_one:
            if item in comp_two:
                priority_sum += priorities.index(item)
                break

    return priority_sum

print(sum_of_priorities(test_input))
print(sum_of_priorities(real_input))

# 157
# 7597 --> correct answer

def sum_of_elf_badges(rucksacks: list[str]):
    priority_sum = 0

    # create lists of three-elf groups
    # looks like [ ['...', '...', '...']  ,  ['...', '...', '...']  ,  ... ]
    groups = [rucksacks[3*i:3*(i+1)] for i in range(int(len(rucksacks)/3))]

    for group in groups:
        # each group has three elves in a list like ['...', '...', '...']
        for item in group[0]:
            if item in group[1] and item in group[2]:
                priority_sum += priorities.index(item)
                break

    return priority_sum

print(sum_of_elf_badges(test_input))
print(sum_of_elf_badges(real_input))

# 70
# 2607 --> correct answer
