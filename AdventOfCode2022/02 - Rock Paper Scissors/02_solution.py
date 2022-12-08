test_input = """A Y
B X
C Z""".split('\n')

with open('input.txt', 'r') as f:
    real_input = f.read().splitlines()

def determine_outcome(opponent, you):
    # A/X: Rock
    # B/Y: Paper
    # C/Z: Scissors

    # Rock
    if opponent == 'A':
        if you == 'X':
            return 3
        elif you == 'Y':
            return 6
        elif you == 'Z':
            return 0
        else:
            raise ValueError

    # Paper
    elif opponent == 'B':
        if you == 'X':
            return 0
        elif you == 'Y':
            return 3
        elif you == 'Z':
            return 6
        else:
            raise ValueError

    # Scissors
    elif opponent == 'C':
        if you == 'X':
            return 6
        elif you == 'Y':
            return 0
        elif you == 'Z':
            return 3
        else:
            raise ValueError

    else:
        raise ValueError


def calculate_score(game_txt):
    total_score = 0
    hand_scores = {'X': 1, 'Y': 2, 'Z': 3}

    for game in game_txt:
        opponent = game.split()[0]
        you = game.split()[1]
        score = determine_outcome(opponent, you)
        total_score += score + hand_scores[you]

    return total_score

print(calculate_score(test_input))
print(calculate_score(real_input))
# 15
# 10595 --> correct answer

# ---------------------------------------------------
# ----------------- Part 2 --------------------------
# ---------------------------------------------------


def determine_hand(opponent: str, desired_result: str) -> str:
    # A: Rock
    # B: Paper
    # C: Scissors
    # X: Lose
    # Y: Draw
    # Z: Win
    
    if opponent == 'A':
        if desired_result == 'X':
            return 'Z'
        elif desired_result == 'Y':
            return 'X'
        elif desired_result == 'Z':
            return 'Y'
        else:
            raise ValueError

    # Paper
    elif opponent == 'B':
        if desired_result == 'X':
            return 'X'
        elif desired_result == 'Y':
            return 'Y'
        elif desired_result == 'Z':
            return 'Z'
        else:
            raise ValueError

    # Scissors
    elif opponent == 'C':
        if desired_result == 'X':
            return 'Y'
        elif desired_result == 'Y':
            return 'Z'
        elif desired_result == 'Z':
            return 'X'
        else:
            raise ValueError

    else:
        raise ValueError


def new_calculate_score(game_txt):
    total_score = 0
    hand_scores = {'X': 1, 'Y': 2, 'Z': 3}

    for game in game_txt:
        opponent = game.split()[0]
        desired_outcome = game.split()[1]
        you = determine_hand(opponent, desired_outcome)
        score = determine_outcome(opponent, you)
        total_score += score + hand_scores[you]

    return total_score

print(new_calculate_score(test_input))
print(new_calculate_score(real_input))
# 12
# 9541 --> solution
