import numpy as np

test_input = """
30373
25512
65332
33549
35390"""[1:].split('\n')

test2 = """
99999
95519
95339
93549
99999"""[1:].split('\n')

with open('input.txt', 'r') as f:
    real_input = f.read().splitlines()

test_input = [list(map(int, list(i))) for i in test_input]
print(test_input)
print(test_input[0][0], test_input[0][1], test_input[1][0], test_input[1][1])
# 30
# 25
# [0][0]: 3     [0][1]: 0     [1][0]: 2     [1][1]: 5
print(np.array(test_input))
print(np.transpose(test_input))


def solution(tree_map):
    tree_map = [list(map(int, list(i))) for i in tree_map]
    invisible_count = 0
    tree_transpose = np.transpose(tree_map)
    width = len(tree_map[0])
    height = len(tree_map)
    total_number = width * height
    scenic_score = np.zeros((height, width))
    
    def calc_number_visible_trees(h: int, trees: list[int]):
        s = 0
        for t in trees:
            if h > t:
                s += 1
            else:
                s += 1
                break
        return s
    
    for row_number, tree_row in enumerate(tree_map):
        for column_number, tree_height in enumerate(tree_row):
            if row_number == 0 or row_number == height - 1 or column_number == 0 or column_number == width - 1:
                continue
            left_view = tree_row[:column_number][::-1]
            left_visibility = tree_height <= max(left_view)
            left_number = calc_number_visible_trees(tree_height, left_view)
            
            right_view = tree_row[column_number+1:]
            right_visibility = tree_height <= max(right_view)
            right_number = calc_number_visible_trees(tree_height, right_view)
            
            up_view = tree_transpose[column_number][:row_number][::-1]
            up_visibility = tree_height <= max(up_view)
            up_number = calc_number_visible_trees(tree_height, up_view)
            
            down_view = tree_transpose[column_number][row_number+1:]
            down_visibility = tree_height <= max(down_view)
            down_number = calc_number_visible_trees(tree_height, down_view)

            scenic_score[row_number][column_number] = left_number * right_number * up_number * down_number
            # print(tree_height, left_number, right_number, up_number, down_number)
            
            # print(tree_row[:column_number],
            #       tree_height,
            #       tree_row[column_number+1:],
            #       tree_transpose[column_number][:row_number],
            #       tree_height,
            #       tree_transpose[column_number][row_number+1:],
            #       left, right, up, down)
            
            if up_visibility and down_visibility and left_visibility and right_visibility:
                invisible_count += 1
    print('part one solution:', total_number - invisible_count)  # 1662
    print('part two solution:', scenic_score.max())  # 537600


solution(real_input)
