def read_in():
    with open("input.txt", "r") as list_input:
        values = list_input.read()
    return values


def find_start_of_message(values, characters):
    for i in range(len(values)):
        char_set = set()  # use a set because items won't repeat
        for j in range(0, characters):  # check item at i and the next 14 characters
            char_set.add(values[i + j])
        if len(char_set) == characters:  # this means all items must have been added so must be different
            return i + characters


def p1(values):
    # original p1 implementation:
    # for i in range(len(values)):
    #     if len({values[i], values[i + 1], values[i + 2], values[i + 3]}) == 4:
    #         return i + 4
    return find_start_of_message(values, 4)


def p2(values):
    return find_start_of_message(values, 14)


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
