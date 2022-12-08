def read_in():
    with open("input.txt", "r") as list_input:
        values = list_input.read().split('\n')
    return values


def visible_above(values, row, col):
    height = values[row][col]
    for i in range(row):
        if values[i][col] >= height:
            return False
    return True


def visible_below(values, row, col):
    height = values[row][col]
    for i in range(row + 1, len(values)):
        if values[i][col] >= height:
            return False
    return True


def visible_left(values, row, col):
    height = values[row][col]
    for i in range(col):
        if values[row][i] >= height:
            return False
    return True


def visible_right(values, row, col):
    height = values[row][col]
    for i in range(col + 1, len(values[row])):
        if values[row][i] >= height:
            return False
    return True


def edge(values, row, col):
    return row == 0 or col == 0 or row == len(values) - 1 or col == len(values[row]) - 1


def p1(values):
    count_visible = 0
    for row in range(len(values)):
        for col in range(len(values[row])):
            if edge(values, row, col) or visible_above(values, row, col) or visible_below(values, row, col) \
                    or visible_left(values, row, col) or visible_right(values, row, col):
                count_visible += 1
    return count_visible


def view_up(values, row, col):
    height = values[row][col]
    for i in range(row - 1, -1, -1):
        if values[i][col] >= height:
            return row - i
    return row


def view_down(values, row, col):
    height = values[row][col]
    for i in range(row + 1, len(values)):
        if values[i][col] >= height:
            return i - row
    return len(values) - (row + 1)


def view_left(values, row, col):
    height = values[row][col]
    for i in range(col - 1, -1, -1):
        if values[row][i] >= height:
            return col - i
    return col


def view_right(values, row, col):
    height = values[row][col]
    for i in range(col + 1, len(values[row])):
        if values[row][i] >= height:
            return i - col
    return len(values[row]) - (col + 1)


def p2(values):
    max_score = 0
    for row in range(1, len(values) - 1):
        for col in range(1, len(values[row]) - 1):
            max_score = max(max_score, view_up(values, row, col) * view_down(values, row, col)
                            * view_left(values, row, col) * view_right(values, row, col))
    return max_score


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
