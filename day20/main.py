def read_in():
    with open("input.txt", "r") as f:
        lines = [int(i.strip()) for i in f.readlines()]
    return lines


def mix(numbers_original, numbers=None):
    if numbers is None:
        numbers = [(i, numbers_original[i]) for i in range(len(numbers_original))]
    for n in range(len(numbers_original)):
        move = (n, numbers_original[n % len(numbers_original)])
        ind = numbers.index(move)
        numbers.remove(move)
        numbers.insert((ind + move[1]) % len(numbers), move)
    return numbers


def grove(numbers_original, numbers):
    zero_at = numbers.index((numbers_original.index(0), 0))
    return numbers[(zero_at + 1000) % len(numbers)][1] + numbers[(zero_at + 2000) % len(numbers)][1] + numbers[
        (zero_at + 3000) % len(numbers)][1]


def p1(numbers_original):
    numbers = mix(numbers_original)
    return grove(numbers_original, numbers)


def p2(numbers_original):
    numbers_original = [811589153 * i for i in numbers_original]
    numbers = mix(numbers_original)
    for i in range(9):
        numbers = mix(numbers_original, numbers)
        # print(numbers)
    return grove(numbers_original, numbers)


def main():
    numbers_original = read_in()
    print(p1(numbers_original))
    print(p2(numbers_original))


if __name__ == "__main__":
    main()
