def read_in():
    with open("input.txt", "r") as list_input:
        values = list_input.read().split('\n')
    return values


def p1(values):
    x = 1
    cycles = 0
    sum_signals = 0
    sum_at = [20, 60, 100, 140, 180, 220]
    for instruction in values:
        if instruction == "noop":
            cycles += 1
            if cycles in sum_at:
                sum_signals += x * cycles
        else:
            cycles += 1
            if cycles in sum_at:
                sum_signals += x * cycles
            cycles += 1
            if cycles in sum_at:
                sum_signals += x * cycles
            x += int(instruction.split(' ')[1])

    return sum_signals


def x_at_cycle_list(values):
    x = 1
    cycles = 0
    x_at = []
    for instruction in values:
        if instruction == "noop":
            cycles += 1
            x_at.append(x)
        else:
            cycles += 1
            x_at.append(x)
            cycles += 1
            x_at.append(x)
            x += int(instruction.split(' ')[1])
    return x_at


def print_screen(screen):
    for row in screen:
        print(''.join(row))


def p2(values, width, height):
    x_at = x_at_cycle_list(values)
    screen = [["." for _ in range(width)] for _ in range(height)]
    for i in range(len(x_at)):
        draw_at = (i // width, i % width)
        if x_at[i] - 1 <= draw_at[1] <= x_at[i] + 1:
            screen[draw_at[0]][draw_at[1]] = "#"
    print_screen(screen)


def main():
    values = read_in()
    print(values)
    print(p1(values))
    print(p2(values, 40, 6))


if __name__ == '__main__':
    main()
