def read_in():
    # Read lines from the input file
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    # Find the coordinates of the S and E characters
    coords = [
        (i, j)
        for i, line in enumerate(lines)
        for j, ch in enumerate(line)
        if ch in ("S", "E")
    ]

    # Replace the S and E characters with a and z
    for coord in coords:
        i, j = coord
        lines[i] = (
            lines[i][:j] + ("a" if lines[i][j] == "S" else "z") + lines[i][j + 1 :]
        )

    # to ord of each character
    values = [[ord(ch) - 97 for ch in line] for line in lines]
    return values, coords


def search(grid, starts_coords, target):

    # Set the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Set of visited nodes
    visited_nodes = set()

    # queue of coords to visit
    queue = [(0, start) for start in starts_coords]

    while queue:
        distance, coord = queue.pop(0)
        if coord == target:
            return distance
        if coord not in visited_nodes:
            r, c = coord
            visited_nodes.add(coord)
            height = grid[r][c]

            if r > 0 and grid[r - 1][c] - height <= 1:
                queue.append((distance + 1, (r - 1, c)))

            if r < rows - 1 and grid[r + 1][c] - height <= 1:
                queue.append((distance + 1, (r + 1, c)))

            if c > 0 and grid[r][c - 1] - height <= 1:
                queue.append((distance + 1, (r, c - 1)))

            if c < cols - 1 and grid[r][c + 1] - height <= 1:
                queue.append((distance + 1, (r, c + 1)))

            queue.sort()


def all_a(grid):
    return [
        (i, j) for i, line in enumerate(grid) for j, ch in enumerate(line) if ch == 0
    ]


def main():
    grid, coords = read_in()

    print(search(grid, [coords[0]], coords[1]))

    print(search(grid, all_a(grid), coords[1]))


if __name__ == "__main__":
    main()
