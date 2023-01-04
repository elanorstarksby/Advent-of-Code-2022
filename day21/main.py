def read_in():
    with open("input.txt", "r") as f:
        lines = {i.strip().split(': ')[0]: i.strip().split(': ')[1] for i in f.readlines()}
    return lines


def calc(monkey, monkeys):
    m = monkeys[monkey]
    if m.isdigit():
        return int(m)
    operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y,
                  '=': lambda x, y: x == y}

    first = calc(m[:4], monkeys)
    operation = m[5]
    second = calc(m[7:], monkeys)

    return operations[operation](first, second)


def p1(monkeys):
    print(monkeys)
    return calc('root', monkeys)


def p2(monkeys):
    # have to manually keep changing the values in here to get closer and closer to 0
    # to get close to the answer without running forever, make root subtract and look for approximate value where
    # subtraction drops below 0. Start by incrementing by high number
    monkeys['root'] = monkeys['root'].replace('+', '-')
    print(monkeys['root'])
    monkeys['humn'] = '3699945358500'  # start with this at 0 and lower values at 100000000 and
    # 100000000000 ish to help bound
    root_zero = False
    while not root_zero:
        root = calc('root', monkeys)
        root_zero = root == 0  # make this root < 0 to find when result drops below 0
        monkeys['humn'] = str(int(monkeys['humn']) + 1)  # change 1 to larger values to help bound
        if int(monkeys['humn']) % 10 == 0:  # change 10 to larger values to help bound
            print(int(monkeys['humn']), root)
    return int(monkeys['humn']) - 1


def test_p2(monkeys):
    monkeys['root'] = monkeys['root'].replace('+', '-')
    print(monkeys['root'])
    monkeys['humn'] = '3699945358564'
    return calc('root', monkeys)


def main():
    monkeys = read_in()
    # monkeys = {'root': 'abcd = humn', 'abcd': '1', 'humn': '1'}
    # print(p1(monkeys))
    print(p2(monkeys))


if __name__ == "__main__":
    main()
