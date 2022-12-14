def read_in():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    rocks = [line.split(' -> ') for line in lines]
    rocks_co_ords = []
    for rock in rocks:
        rock_coord = []
        for corner in rock:
            rock_coord.append(tuple([int(a) for a in corner.split(',')]))
        rocks_co_ords.append(rock_coord)
    return rocks_co_ords


def map_out_rocks(rocks):
    obstacles = {}
    max_y = 0
    for rock in rocks:
        nx, ny = rock[0]
        for i in range(len(rock) - 1):
            cx, cy = nx, ny
            max_y = max(max_y, cy)
            nx, ny = rock[i + 1]

            if cx == nx:
                for y in range(min(cy, ny), max(cy, ny) + 1):
                    obstacles[(cx, y)] = 'r'
            else:
                for x in range(min(cx, nx), max(cx, nx) + 1):
                    obstacles[(x, cy)] = 'r'
    return obstacles, max_y


def p1(rocks):
    obstacles, max_y = map_out_rocks(rocks)
    void = False
    while not void:
        sx, sy = (500, 0)
        while True:
            if sy == max_y:
                void = True
                break
            elif (sx, sy + 1) not in obstacles:
                sy += 1
            elif (sx - 1, sy + 1) not in obstacles:
                sx += -1
                sy += 1
            elif (sx + 1, sy + 1) not in obstacles:
                sx += 1
                sy += 1
            else:
                obstacles[(sx, sy)] = 's'
                break

    sand = 0
    for c, o in obstacles.items():
        if o == 's':
            sand += 1
    return sand


def map_out_rocks_floor(rocks):
    obstacles = {}
    max_y = 0
    for rock in rocks:
        nx, ny = rock[0]
        for i in range(len(rock) - 1):
            cx, cy = nx, ny
            max_y = max(max_y, cy)
            nx, ny = rock[i + 1]

            if cx == nx:
                for y in range(min(cy, ny), max(cy, ny) + 1):
                    obstacles[(cx, y)] = 'r'
            else:
                for x in range(min(cx, nx), max(cx, nx) + 1):
                    obstacles[(x, cy)] = 'r'
    for x in range(0, 1000):
        obstacles[(x, max_y+2)] = 'f'
    return obstacles


def p2(rocks):
    obstacles = map_out_rocks_floor(rocks)
    source = False
    while not source:
        sx, sy = (500, 0)
        while True:
            if (500, 0) in obstacles:
                source = True
                break
            elif (sx, sy + 1) not in obstacles:
                sy += 1
            elif (sx - 1, sy + 1) not in obstacles:
                sx += -1
                sy += 1
            elif (sx + 1, sy + 1) not in obstacles:
                sx += 1
                sy += 1
            else:
                obstacles[(sx, sy)] = 's'
                break

    sand = 0
    for c, o in obstacles.items():
        if o == 's':
            sand += 1
    return sand


def main():
    values = read_in()
    # print(values)
    print(p1(values))
    print(p2(values))


if __name__ == "__main__":
    main()
