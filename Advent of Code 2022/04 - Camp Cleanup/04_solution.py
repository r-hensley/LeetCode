test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split('\n')

positive_tests = """2-38,2-2
4-90,5-5
66-86,66-77
59-81,60-80
11-11,10-94
9-39,9-40
9-9,9-98
9-9,9-9""".split('\n')  # 8

negative_tests = """5-10,3-5
3-5,5-10
5-7,3-5
3-5,5-7""".split('\n')  # 3


with open('input.txt', 'r') as f:
    real_input = f.read().splitlines()


def calc_overlaps(pairs_list: list):
    number_of_overlaps = 0
    # print(pairs_list)

    for elf_pair in pairs_list:  # looks like '2-4,6-8'
        # print(elf_pair)
        elves = elf_pair.split(',')  # ['2,4', '6-8']

        elf_one = elves[0]  # '2-4'
        a = int(elf_one.split('-')[0])  # 2
        b = int((elf_one.split('-')[1]))  # 4

        elf_two = elves[1]  # '6-8'
        x = int(elf_two.split('-')[0])  # 6
        y = int((elf_two.split('-')[1]))  # 8

        # good
        # 1-10,4-5    1-5,3-5    1-5,1-3    1-3,1-5    3-5,1-5    4-5,1-10    5-5,5-5
        # a < x       a < x      a == x     a == x     a > x      a > x       a == x
        # b > y       b == y     b > y      b < y      b == y     b < y       b == y
        # opp

        # bad
        # 3-5,5-7    5-10,3-5
        # a < x      a > x
        # b < y      b > y

        if (a < x and b < y) or (a > x and b > y):
            continue
        else:
            number_of_overlaps += 1
            continue

        # if a == x or b == y:
        #     number_of_overlaps += 1
        #     continue
        #
        # elif a < x and b >= y:
        #     number_of_overlaps += 1
        #     continue
        #
        # elif a > x and b <= y:
        #     number_of_overlaps += 1
        #     continue

    return number_of_overlaps

# print(calc_overlaps(positive_tests))
# print(calc_overlaps(negative_tests))
print(calc_overlaps(real_input))

# answer: 571

# #############################
# ########## Part 2 ###########
# #############################

def part_two_overlaps(pairs_list: list):
    number_of_overlaps = 0

    for elf_pair in pairs_list:  # looks like '2-4,6-8'
        elves = elf_pair.split(',')  # ['2,4', '6-8']

        elf_one = elves[0]  # '2-4'
        a = int(elf_one.split('-')[0])  # 2
        b = int((elf_one.split('-')[1]))  # 4

        elf_two = elves[1]  # '6-8'
        x = int(elf_two.split('-')[0])  # 6
        y = int((elf_two.split('-')[1]))  # 8

        # ....567..  5-7
        # ......789  7-9

        # ......789  7-9
        # ....567..  5-7
        if (b >= x and a < y) or (a <= y and b > x):
            number_of_overlaps += 1

    return number_of_overlaps

print(part_two_overlaps(test_input))
print(part_two_overlaps(real_input))