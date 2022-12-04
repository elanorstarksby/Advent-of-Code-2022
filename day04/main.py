def read_in():
    values = []
    with open("input.txt", "r") as list_input:
        for line in list_input:
            # split into pairs and then start and end of ranges
            v = [[int(j) for j in i.split('-')] for i in line.strip().split(',')]
            values.append(v)
    return values


def contains(v0, v1):
    return v0[0] <= v1[0] and v0[1] >= v1[1]


def p1(values):
    count = 0
    for v in values:
        if contains(v[0], v[1]) or contains(v[1], v[0]):
            count += 1
    return count


def p2(values):
    overlapping = 0
    for pair in values:
        # find intersection of sets made from ranges
        pair_set1 = set(range(pair[0][0], pair[0][1] + 1))
        pair_set2 = set(range(pair[1][0], pair[1][1] + 1))
        inters = pair_set1.intersection(pair_set2)
        if len(inters) > 0:
            overlapping += 1
    return overlapping


def main():
    values = read_in()
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
