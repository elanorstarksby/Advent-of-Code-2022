SPACE_TOTAL = 70000000
SPACE_NEEDED = 30000000


def read_in():
    with open("input.txt", "r") as list_input:
        values = list_input.read().split('\n')
    return values


def calculate_sizes(values):
    path = []  # tracks the path of the directory we're looking at
    sizes = {}  # map from directory (full path) to its size
    for i in range(len(values)):
        line = values[i]  # get next line of terminal output
        if line[0] == "$" and line[2:4] == "cd":  # if cd instruction
            if line[5:] == "..":  # go up one level
                path.pop()
            elif line[5:] == "/":  # go to root
                path = []
            else:
                path.append(line[5:])  # add the next directory to the list for path
        elif line[0] != '$' and not line.startswith("dir"):  # this means it's a file
            for d in range(len(path) + 1):  # iterate through index of directories in path so
                size = int(line.split(' ')[0])  # this will be the size of file on the current line
                this_path = '/' + '/'.join(path[0:d])  # this is key for sizes dict
                if this_path not in sizes:  # path not already in dictionary so initialise
                    sizes[this_path] = 0
                sizes[this_path] += size  # add the size of this file to the size of the directory
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
