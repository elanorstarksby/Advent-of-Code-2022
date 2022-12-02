def read_in_two_values():
    rps = {"A": "rock", "X": "rock", "B": "paper", "Y": "paper", "C": "scissors", "Z": "scissors"}
    values = []
    with open("input.txt", "r") as list_input:
        for line in list_input:
            values.append([rps[player] for player in line.strip().split(' ')])
    return values


def read_in_two_values_2():
    rps = {"A": "rock", "X": "lose", "B": "paper", "Y": "draw", "C": "scissors", "Z": "win"}
    values = []
    with open("input.txt", "r") as list_input:
        for line in list_input:
            values.append([rps[player] for player in line.strip().split(' ')])
    return values


item_scores = {"rock": 1, "paper": 2, "scissors": 3}
what_it_beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
what_it_loses_to = {"rock": "paper", "paper": "scissors", "scissors": "rock"}


def calc_score_1(values):
    score = 0
    for a, b in values:
        if a == b:
            score += 3 + item_scores[b]  # draw
        elif what_it_beats[a] == b:
            score += item_scores[b]  # lose
        else:
            score += 6 + item_scores[b]  # win
    return score


def calc_score_2(values):
    score = 0
    for a, b in values:
        if b == "draw":
            score += 3 + item_scores[a]  # draw
        elif b == "lose":
            score += item_scores[what_it_beats[a]]  # lose
        else:
            score += 6 + item_scores[what_it_loses_to[a]]  # win
    return score


def main():
    values = read_in_two_values()
    print(values)
    score = calc_score_1(values)
    print(score)
    values_2 = read_in_two_values_2()
    score_2 = calc_score_2(values_2)
    print(score_2)


if __name__ == '__main__':
    main()
