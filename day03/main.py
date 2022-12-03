def priority_of(item):  # a = 1, A = 27
    return ord(item) - 96 if ord(item) >= 97 else ord(item) - 38


def p1():
    cumulative = 0
    with open("input.txt", "r") as list_input:
        for line in list_input:
            items = [i for i in line.strip()]  # array from the line
            done = []  # items already counted from the first half of the list
            for item in items[0:len(items) // 2]:  # iterate over first half of the list
                if item not in done and item in items[len(items) // 2:]:  # not counted already and is in 2nd half
                    cumulative += priority_of(item)
                    done.append(item)  # don't count again
    return cumulative


def p2():
    elves = []  # to keep track of last two lines
    cumulative = 0  # sum of priorities
    with open("input.txt", "r") as list_input:
        for line in list_input:
            items = [i for i in line.strip()]
            if len(elves) < 2:  # still counting up to the next three elves
                elves.append(items)
            else:  # this is the third in a group
                for item in items:
                    if item in elves[0] and item in elves[1]:  # common across all three
                        cumulative += priority_of(item)
                        elves = []  # reset list for current group
                        break  # avoid counting twice if common item appears more than once
    return cumulative


def main():
    print(p1())
    print(p2())


if __name__ == '__main__':
    main()
