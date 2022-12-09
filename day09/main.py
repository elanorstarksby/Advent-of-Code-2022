def read_in():
    with open("input.txt", "r") as list_input:
        values = list_input.read().split('\n')
    return values


def p1(values):
    visited = set()
    h = [0, 0]
    t = [0, 0]
    visited.add((0, 0))
    for move in values:
        direction, distance = move.split(' ')
        for step in range(int(distance)):
            h = [h[0] + (1 if direction == "U" else -1 if direction == "D" else 0),
                 h[1] + (1 if direction == "R" else -1 if direction == "L" else 0)]
            if not (abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1):
                if h[0] - t[0] >= 1:  # head is right of tail
                    t[0] += 1
                elif t[0] - h[0] >= 1:  # head is left of tail
                    t[0] -= 1

                if h[1] - t[1] >= 1:
                    t[1] += 1
                elif t[1] - h[1] >= 1:
                    t[1] -= 1
            visited.add((t[0], t[1]))
    return len(visited)


def p2(values):
    visited = set()
    h = [0, 0]
    tails = [[0, 0] for _ in range(9)]
    visited.add((0, 0))
    for move in values:
        direction, distance = move.split(' ')
        for step in range(int(distance)):
            h = [h[0] + (1 if direction == "U" else -1 if direction == "D" else 0),
                 h[1] + (1 if direction == "R" else -1 if direction == "L" else 0)]
            last_t = h
            for t in tails:
                if not (abs(last_t[0] - t[0]) <= 1 and abs(last_t[1] - t[1]) <= 1):
                    if last_t[0] - t[0] >= 1:  # last tail is right of tail
                        t[0] += 1
                    elif t[0] - last_t[0] >= 1:  # last tail is left of tail
                        t[0] -= 1

                    if last_t[1] - t[1] >= 1:  # above
                        t[1] += 1
                    elif t[1] - last_t[1] >= 1:  # below
                        t[1] -= 1
                last_t = t
            visited.add((tails[-1][0], tails[-1][1]))
            # print(h, t)
    return len(visited)


def main():
    values = read_in()
    # print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
