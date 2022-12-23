import math


def read_in():
    with open("input.txt", "r") as f:
        lines = [i.strip() for i in f.readlines()]
    coords = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                coords.add((x, y))
    return coords


def no_elves_north(elf, coords):
    return not (
            (elf[0] - 1, elf[1] - 1) in coords or  # NW
            (elf[0], elf[1] - 1) in coords or  # N
            (elf[0] + 1, elf[1] - 1) in coords  # NE
    )


def no_elves_south(elf, coords):
    return not (
            (elf[0] - 1, elf[1] + 1) in coords or  # SW
            (elf[0], elf[1] + 1) in coords or  # S
            (elf[0] + 1, elf[1] + 1) in coords  # SE
    )


def no_elves_east(elf, coords):
    return not (
            (elf[0] + 1, elf[1] - 1) in coords or  # NE
            (elf[0] + 1, elf[1]) in coords or  # E
            (elf[0] + 1, elf[1] + 1) in coords  # SE
    )


def no_elves_west(elf, coords):
    return not (
            (elf[0] - 1, elf[1] - 1) in coords or  # NW
            (elf[0] - 1, elf[1]) in coords or  # W
            (elf[0] - 1, elf[1] + 1) in coords  # SW
    )


def coords_to_grid(coords, width, height):
    grid = [['.' for _ in range(width * 2)] for _ in range(height * 2)]
    grid[height][width] = '@'
    for x, y in coords:
        grid[y + height][x + width] = '#'

    return grid


def rectangle(coords):
    min_x = math.inf
    max_x = -math.inf
    min_y = math.inf
    max_y = -math.inf
    for x, y in coords:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    count = 0
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if (x, y) not in coords:
                count += 1
    return count


def p1(coords, times=10):
    movement = {'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}
    order = ['N', 'S', 'W', 'E']
    no_elves_dir = {'N': no_elves_north, 'S': no_elves_south, 'W': no_elves_west, 'E': no_elves_east}
    for t in range(times):
        proposed = {}
        for i, elf in enumerate(coords):
            first_empty = ''
            all_empty = True
            for d in range(t, t + 4):
                direction = order[d % 4]
                if no_elves_dir[direction](elf, coords):
                    if first_empty == '':
                        first_empty = direction
                else:
                    all_empty = False
            if all_empty or not first_empty:
                propose = elf
            else:
                propose = (elf[0] + movement[first_empty][0], elf[1] + movement[first_empty][1])
            if propose in proposed:
                proposed[propose].append(elf)
            else:
                proposed[propose] = [elf]
        last_coords = coords.copy()
        coords = set()
        for new, olds in proposed.items():
            if len(olds) == 1:
                coords.add(new)
            else:
                for old in olds:
                    coords.add(old)

        # grid = coords_to_grid(coords, 20, 20)
        # for g in grid:
        #     print(''.join(g))
        # print()
        if last_coords == coords:
            return None, t+1
    return rectangle(coords), None


def main():
    coords = read_in()
    print(coords)
    print(p1(coords, 10))
    print(p1(coords, 1500))


if __name__ == "__main__":
    main()
