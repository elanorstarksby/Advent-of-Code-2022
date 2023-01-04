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


def find_next(board, pos, direction):
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
            next_position = find_next(board, current_position, current_direction)
            print('!', next_position)
            n = int(i)
            while board[next_position[0]][next_position[1]] not in {'#', ' '} and n > 0:
                current_position = next_position
                next_position = find_next(board, current_position, current_direction)

                n -= 1

        else:
            current_direction = direction_order[
                (direction_order.index(current_direction) + (1 if i == 'R' else -1)) % 4]
            print(current_position, current_direction)
    print(current_position)

    return 1000 * (current_position[0] + 1) + 4 * (current_position[1] + 1) + direction_order.index(current_direction)


def main():
    values = read_in()
    print(p1(values))


if __name__ == "__main__":
    main()
