def read_in():
    with open("input.txt", "r") as f:
        lines = f.read()
    return lines


def fall_one(chamber, rock):
    new_rock = tuple([(x, y - 1) for x, y in rock])
    for coord in new_rock:
        if coord in chamber or coord[1] < 0:
            return rock
    return new_rock


def move_left(chamber, rock):
    new_rock = tuple([(x - 1, y) for x, y in rock])
    for coord in new_rock:
        if coord in chamber or coord[0] < 0:
            return rock
    return new_rock


def move_right(chamber, rock):
    new_rock = tuple([(x + 1, y) for x, y in rock])  # position of rock if moved
    for coord in new_rock:
        if coord in chamber or coord[0] > 6:  # if new coordinate is already occupied or if wall
            return rock  # keep old rock position
    return new_rock


def initialise_rock(rock_shape, height):
    y0 = height + 3
    return tuple([(x + 2, y + y0) for x, y in rock_shape])


def p1(jets, rocks):
    jet = 0
    jet_count = len(jets)
    chamber = set()
    height = 0

    for rock_count in range(2022):
        rock_coords = initialise_rock(rocks[rock_count % len(rocks)], height)
        # print(rock_coords)

        still_falling = True
        while still_falling:
            if jets[jet] == "<":
                rock_coords = move_left(chamber, rock_coords)
            else:
                rock_coords = move_right(chamber, rock_coords)
            old_rock = rock_coords
            rock_coords = fall_one(chamber, rock_coords)
            still_falling = rock_coords != old_rock
            jet = (jet + 1) % jet_count
            # print(rock_coords)

        height = max(height, max(coord[1] for coord in rock_coords) + 1)

        chamber.update(rock_coords)

        # print_chamber(chamber, 7, highest_point)
        # print()
    return height


def p2(jets, rocks):
    jet = 0
    jet_count = len(jets)
    chamber = set()
    height = 0

    for rock_count in range(2022):
        rock_coords = initialise_rock(rocks[rock_count % len(rocks)], height)
        # print(rock_coords)

        still_falling = True
        while still_falling:
            if jets[jet] == "<":
                rock_coords = move_left(chamber, rock_coords)
            else:
                rock_coords = move_right(chamber, rock_coords)
            old_rock = rock_coords
            rock_coords = fall_one(chamber, rock_coords)
            still_falling = rock_coords != old_rock
            jet = (jet + 1) % jet_count
            # print(rock_coords)

        height = max(height, max(coord[1] for coord in rock_coords) + 1)

        chamber.update(rock_coords)

        # print_chamber(chamber, 7, highest_point)
        # print()
    return height


def print_chamber(fallen_rocks, chamber_width, chamber_height):
    chamber = []
    for i in range(chamber_height + 1):
        chamber.append(['.'] * chamber_width)

    for (x, y) in fallen_rocks:
        chamber[y][x] = '#'

    chamber.reverse()
    for row in chamber:
        print(''.join(row))


def main():
    jets = read_in()
    rocks = (((0, 0), (1, 0), (2, 0), (3, 0)),
             ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
             ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
             ((0, 0), (0, 1), (0, 2), (0, 3)),
             ((0, 0), (0, 1), (1, 0), (1, 1))
             )
    height = p1(jets, rocks)
    print(height)
    # print(p2())


if __name__ == "__main__":
    main()
