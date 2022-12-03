# part 1
print(max([sum(list(map(int, i.split('\n')))) for i in open('input.txt', 'r').read().split('\n\n')]))
# 71934

# part 2
print(sum(sorted([sum(list(map(int, i.split('\n')))) for i in open('input.txt', 'r').read().split('\n\n')], reverse=True)[:3]))
# 211447
