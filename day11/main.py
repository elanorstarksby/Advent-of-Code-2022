import math


class Monkey:
    monkeys = []
    lcm = 1

    def __init__(self, monkey_input):
        self.item_queue = [int(i) for i in monkey_input[1].split(': ')[1].split(', ')]
        self.operation = monkey_input[2].split(' ')[-3:]
        self.division_test = int(monkey_input[3].split(' ')[-1])
        self.true_monkey = int(monkey_input[-2].split(' ')[-1])
        self.false_monkey = int(monkey_input[-1].split(' ')[-1])
        self.inspections = 0
        # print(self.item_queue, self.division_test, self.true_monkey, self.false_monkey, self.operation)

    def do_operation(self, item):
        right = item if self.operation[2] == 'old' else int(self.operation[2])
        if self.operation[1] == '*':
            return item * right
        else:
            return item + right

    def throw_all_p1(self):
        for item in self.item_queue:
            item = self.do_operation(item)
            item //= 3
            if item % self.division_test == 0:
                give_to = self.true_monkey
            else:
                give_to = self.false_monkey
            Monkey.monkeys[give_to].receive(item)
            self.inspections += 1
        self.item_queue = []

    def receive(self, item):
        self.item_queue.append(item)

    def throw_all_p2(self):
        for item in self.item_queue:
            item = self.do_operation(item)
            if item % self.division_test == 0:
                give_to = self.true_monkey
            else:
                give_to = self.false_monkey
            item %= Monkey.lcm
            Monkey.monkeys[give_to].receive(item)
            self.inspections += 1
        self.item_queue = []


def read_in():
    with open("input.txt", "r") as list_input:
        values = [monkey.split('\n') for monkey in list_input.read().split('\n\n')]
    return values


def monkey_business():
    busy = [monkey.inspections for monkey in Monkey.monkeys]
    busy.sort(reverse=True)
    return busy[0] * busy[1]


def p1(values):
    Monkey.monkeys = []
    for monkey_input in values:
        Monkey.monkeys.append(Monkey(monkey_input))

    for _ in range(20):
        for monkey in Monkey.monkeys:
            monkey.throw_all_p1()
    return monkey_business()


def p2(values):
    Monkey.monkeys = []
    for monkey_input in values:
        Monkey.monkeys.append(Monkey(monkey_input))
    Monkey.lcm = math.lcm(*[monkey.division_test for monkey in Monkey.monkeys])  # requires Python 3.9

    for _ in range(10000):
        for monkey in Monkey.monkeys:
            monkey.throw_all_p2()
    return monkey_business()


def main():
    values = read_in()
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()
