import json
import functools


def read_in():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    lines = list(filter(None, lines))  # removes items that are empty, needed for empty lines ''
    return [json.loads(line) for line in lines]


def in_order(left, right):
    if isinstance(left, list) and isinstance(right, list):
        shortest = min(len(left), len(right))
        for i in range(shortest):
            item_order = in_order(left[i], right[i])
            if item_order is not None:
                return item_order
        return None if len(left) == len(right) else len(left) < len(right)
    elif isinstance(left, list):
        return in_order(left, [right])
    elif isinstance(right, list):
        return in_order([left], right)
    else:
        return None if left == right else left < right


def p1(values):
    i = 1
    sum_ordered = 0
    while i < len(values):
        left = values[i - 1]
        right = values[i]
        if in_order(left, right):
            sum_ordered += (i + 1) // 2
        i += 2

    return sum_ordered


def wrap_in_order(left, right):
    v = in_order(left, right)
    return 0 if v is None else 1 if v else -1


def p2(values):
    sorted_packets = sorted(values, key=functools.cmp_to_key(wrap_in_order), reverse=True)
    print(sorted_packets)
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


def main():
    values = read_in()
    print(values)
    print(p1(values))
    values += [[[2]], [[6]]]
    print(p2(values))


if __name__ == "__main__":
    main()
