SPACE_TOTAL = 70000000
SPACE_NEEDED = 30000000


def read_in():
    with open("input.txt", "r") as list_input:
        values = list_input.read().split('\n')
    return values


def calculate_sizes(values):
    path = []
    sizes = {}
    for i in range(len(values)):
        line = values[i]
        if line[0] == "$" and line[2:4] == "cd":
            if line[5:] == "..":
                path.pop()
            elif line[5:] == "/":
                path = []
            else:
                path.append(line[5:])
        elif line[0] != '$' and not line.startswith("dir"):
            for d in range(len(path) + 1):  # iterate through index of directories in path
                size = int(line.split(' ')[0])
                this_path = '/' + '/'.join(path[0:d])
                if this_path not in sizes:
                    sizes[this_path] = 0
                sizes[this_path] += size
    return sizes


def p1(sizes):
    total = 0
    for size in sizes.values():
        if size <= 100000:
            total += size
    return total


def p2(sizes):
    space_used = sizes['/']
    min_delete = space_used - (SPACE_TOTAL - SPACE_NEEDED)
    best_found = SPACE_TOTAL
    for size in sizes.values():
        if best_found > size >= min_delete:
            best_found = size
    return best_found


def main():
    values = read_in()
    sizes = calculate_sizes(values)
    print(p1(sizes))
    print(p2(sizes))


if __name__ == '__main__':
    main()
