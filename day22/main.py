import re


def read_in():
    with open("input.txt", "r") as f:
        lines = f.read().split('\n')
    lines.remove('')
    print(lines[-1])
    return lines


def board_get(board, row, col):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
        return ' '
    return board[row][col]


def find_next_wrap(board, pos, direction):
    if direction == (-1, 0) and board_get(board, pos[0] - 1, pos[1]) == ' ':
        # wrap to bottom
        return max(row for row in range(len(board)) if board_get(board, row, pos[1]) != ' '), pos[1]
    elif direction == (1, 0) and board_get(board, pos[0] + 1, pos[1]) == ' ':
        # wrap to top
        return min(row for row in range(len(board)) if board_get(board, row, pos[1]) != ' '), pos[1]
    elif direction == (0, -1) and board_get(board, pos[0], pos[1] - 1) == ' ':
        # wrap to right side
        return pos[0], max(col for col in range(len(board[pos[0]])) if board_get(board, pos[0], col) != ' ')
    elif direction == (0, 1) and board_get(board, pos[0], pos[1] + 1) == ' ':
        # wrap to left side
        return pos[0], min(col for col in range(len(board[pos[0]])) if board_get(board, pos[0], col) != ' ')
    else:
        return pos[0] + direction[0], pos[1] + direction[1]


def p1(values):
    board = [[_ for _ in row] for row in values[:-1]]
    # board = values[:-1]
    print(board)

    instructions = re.findall(r"\d+|[A-Z]", values[-1])

    up = (-1, 0)
    right = (0, 1)
    down = (1, 0)
    left = (0, -1)
    current_direction = right
    direction_order = [right, down, left, up]

    # first_wall = board[0].index('#')
    first_empty = board[0].index('.')
    current_position = (0, first_empty)
    print(first_empty, current_position)

    for i in instructions:
        if i.isdigit():
            next_position = find_next_wrap(board, current_position, current_direction)
            print('!', next_position)
            n = int(i)
            while board[next_position[0]][next_position[1]] not in {'#', ' '} and n > 0:
                current_position = next_position
                next_position = find_next_wrap(board, current_position, current_direction)

                n -= 1

        else:
            current_direction = direction_order[
                (direction_order.index(current_direction) + (1 if i == 'R' else -1)) % 4]
            print(current_position, current_direction)
    print(current_position)

    return 1000 * (current_position[0] + 1) + 4 * (current_position[1] + 1) + direction_order.index(current_direction)


def find_next_cube(board, pos, direction):
    if direction == (-1, 0) and board_get(board, pos[0] - 1, pos[1]) == ' ':  # up
        if pos[0] == 0 and pos[1] in range(100, 150):  # l edge
            print("l up")
            return (199, pos[1] - 100), direction
        elif pos[0] == 0 and pos[1] in range(50, 100):  # b edge
            print("b up")
            return (pos[1] + 100, 0), (0, 1)
        elif pos[0] == 100 and pos[1] in range(0, 50):  # e edge
            print("e up")
            return (pos[1] + 50, 50), (0, 1)
        print("oops up")
    elif direction == (1, 0) and board_get(board, pos[0] + 1, pos[1]) == ' ':  # down
        if pos[0] == 49 and pos[1] in range(100, 150):  # f edge
            print("f down")
            return (pos[1] - 50, 99), (0, -1)
        if pos[0] == 199 and pos[1] in range(0, 50):  # l edge
            print("l down")
            return (0, pos[1] + 100), direction
        if pos[0] == 149 and pos[1] in range(50, 100):  # j edge
            print("j down")
            return (pos[1] + 100, 49), (0, -1)

        print("oops down")
    elif direction == (0, -1) and board_get(board, pos[0], pos[1] - 1) == ' ':  # left
        if pos[0] in range(0, 50) and pos[1] == 50:  # a edge 1 to 4
            print("a1 left")
            return (149 - pos[0], 0), (0, 1)
        if pos[0] in range(100, 150) and pos[1] == 0:  # a edge 4 to 1
            print("a4 left")
            return (149 - pos[0], 50), (0, 1)
        if pos[0] in range(150, 200) and pos[1] == 0:  # b edge
            print("b left")
            return (0, pos[0] - 100), (1, 0)
        if pos[0] in range(50, 100) and pos[1] == 50:  # e edge 3 to 4
            print("e left")
            return (100, pos[0] - 50), (1, 0)
        print("oops left", direction, pos)
    elif direction == (0, 1) and board_get(board, pos[0], pos[1] + 1) == ' ':  # right
        if pos[0] in range(0, 50) and pos[1] == 149:  # i edge 2 to 5
            print("i2 right")
            return (149 - pos[0], 99), (0, -1)
        if pos[0] in range(100, 150) and pos[1] == 99:  # i edge 5 to 2
            print("i5 right")
            return (149 - pos[0], 149), (0, -1)
        if pos[0] in range(50, 100) and pos[1] == 99:  # f edge 3 to 2
            print("f right")
            return (49, pos[0] + 50), (-1, 0)
        if pos[0] in range(150, 200) and pos[1] == 49:  # j edge 6 to 5
            print("j right")
            return (149, pos[0] - 100), (-1, 0)
        print("oops right")

    else:
        print("not edge")
        return (pos[0] + direction[0], pos[1] + direction[1]), direction


#  100 -> 50, 149 -> 99

def p2(values):
    board = [[_ for _ in row] for row in values[:-1]]
    # board = values[:-1]
    # print(board)

    instructions = re.findall(r"\d+|[A-Z]", values[-1])

    up = (-1, 0)
    right = (0, 1)
    down = (1, 0)
    left = (0, -1)
    current_direction = right
    direction_order = [right, down, left, up]

    # first_wall = board[0].index('#')
    first_empty = board[0].index('.')
    current_position = (0, first_empty)
    print(first_empty, current_position)

    for i in instructions:
        if i.isdigit():
            next_position, next_direction = find_next_cube(board, current_position, current_direction)
            print('!', next_position)
            if next_position == (151, 46):
                print("HERE")
            n = int(i)
            while board[next_position[0]][next_position[1]] not in {'#', ' '} and n > 0:
                current_position = next_position
                current_direction = next_direction
                next_position, next_direction = find_next_cube(board, current_position, current_direction)
                if next_position[0] < 0 or next_position[1] < 0:
                    print("HERE 2")

                n -= 1

        else:
            current_direction = direction_order[
                (direction_order.index(current_direction) + (1 if i == 'R' else -1)) % 4]
            print(current_position, current_direction)
    print(current_position)

    return 1000 * (current_position[0] + 1) + 4 * (current_position[1] + 1) + direction_order.index(current_direction)
# not edge
# (151, 45) (0, 1)
# not edge
# ! (151, 46)
# not edge
# not edge
# not edge

def main():
    values = read_in()
    print(p2(values))


if __name__ == "__main__":
    main()
