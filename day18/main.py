def read_in():
    with open("input.txt", "r") as f:
        lines = set(tuple(int(a) for a in l.strip().split(',')) for l in f.readlines())
    return lines


def adjacent(coords, c1):
    x, y, z = c1
    count = 0
    if (x - 1, y, z) in coords:
        count += 1
    if (x + 1, y, z) in coords:
        count += 1
    if (x, y - 1, z) in coords:
        count += 1
    if (x, y + 1, z) in coords:
        count += 1
    if (x, y, z - 1) in coords:
        count += 1
    if (x, y, z + 1) in coords:
        count += 1
    return count


def p1(coords):
    surface_area = 0
    for c in coords:
        surface_area += 6 - adjacent(coords, c)

    return surface_area


def p2():
    return


def main():
    coords = read_in()
    print(p1(coords))
    print(p2())


if __name__ == "__main__":
    main()
