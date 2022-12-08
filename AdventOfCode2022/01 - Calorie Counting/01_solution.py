# part 1
print(max([sum(list(map(int, i.split('\n')))) for i in open('input.txt', 'r').read().split('\n\n')]))
# 71934

# part 2
print(sum(sorted([sum(list(map(int, i.split('\n')))) for i in open('input.txt', 'r').read().split('\n\n')], reverse=True)[:3]))
# 211447

# expanded version
def expanded_part_one():
    groups = open('input.txt', 'r').read().split('\n\n')
    calorie_counts = []
    for i in groups:
        calories = i.split("\n") # a list of str
        calories = list(map(int, calories))  # convert all elements of list from str to int
        calorie_counts.append(sum(calories))
    
    return max(calorie_counts)