def read_in_1d():
    lines = []
    cumulative = 0
    with open("input.txt", "r") as list_input:
        for line in list_input:
            if line != '\n':
                cumulative += int(line.strip())
            else:
                lines.append(cumulative)
                cumulative = 0
    return lines


def main():
    values = read_in_1d()
    print(values)
    values.sort()
    print(sum(values[-3:]))


if __name__ == '__main__':
    main()
