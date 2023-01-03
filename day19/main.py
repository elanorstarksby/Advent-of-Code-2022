import math
import re
import functools


def read_in():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    pattern = re.compile(
        r"^Blueprint (-?\d+): Each ore robot costs (-?\d+) ore. Each clay robot costs (-?\d+) ore. Each obsidian robot "
        r"costs (-?\d+) ore and (-?\d+) clay. Each geode robot costs (-?\d+) ore and (-?\d+) obsidian.$")
    values = []
    for line in lines:
        m = pattern.match(line)
        values.append(tuple([int(m.group(x)) for x in range(2, 8)]))
    return values


@functools.cache
def max_pos(geodes, geode_bot, remaining_time):
    max_possible = geodes
    g = geode_bot

    for t in range(remaining_time+1):
        max_possible += g
        g += 1
    return max_possible


@functools.cache
def search(bp, minute, max_minutes, ore_bot, clay_bot, obsidian_bot, geode_bot, ore, clay, obsidian, geode, msf):
    max_ore_bots = max(bp[0], bp[1], bp[2], bp[4])
    max_clay_bots = bp[3]
    max_obsidian_bots = bp[5]
    if minute > max_minutes:
        return geode

    if max_pos(geode, geode_bot, max_minutes - minute) <= msf:
        return 0

    if ore >= bp[4] and obsidian >= bp[5]:
        return search(bp, minute + 1, max_minutes, ore_bot, clay_bot, obsidian_bot, geode_bot + 1,
                      ore + ore_bot - bp[4], clay + clay_bot, obsidian + obsidian_bot - bp[5], geode + geode_bot, msf)

    m = 0
    if ore >= bp[2] and clay >= bp[3] and obsidian_bot < max_obsidian_bots:
        m = max(m, search(bp, minute + 1, max_minutes, ore_bot, clay_bot, obsidian_bot + 1, geode_bot,
                          ore + ore_bot - bp[2], clay + clay_bot - bp[3], obsidian + obsidian_bot,
                          geode + geode_bot, max(m, msf)))

    if ore >= bp[1] and clay_bot < max_clay_bots:
        m = max(m, search(bp, minute + 1, max_minutes, ore_bot, clay_bot + 1, obsidian_bot, geode_bot,
                          ore + ore_bot - bp[1], clay + clay_bot, obsidian + obsidian_bot, geode + geode_bot,
                          max(m, msf)))

    if ore >= bp[0] and ore_bot < max_ore_bots:
        m = max(m, search(bp, minute + 1, max_minutes, ore_bot + 1, clay_bot, obsidian_bot, geode_bot,
                          ore + ore_bot - bp[0], clay + clay_bot, obsidian + obsidian_bot, geode + geode_bot,
                          max(m, msf)))

    return max(m, search(bp, minute + 1, max_minutes, ore_bot, clay_bot, obsidian_bot, geode_bot, ore + ore_bot,
                         clay + clay_bot, obsidian + obsidian_bot, geode + geode_bot, max(m, msf)))


def p1(blueprints=None, max_minutes=24):
    if blueprints is None:  # example input
        blueprints = [(4, 2, 3, 14, 2, 7), (2, 3, 3, 8, 3, 12)]
    quality = []
    for i, bp in enumerate(blueprints):
        quality.append(((i + 1), search(bp, 1, max_minutes, 1, 0, 0, 0, 0, 0, 0, 0, 0)))
        # print(quality)
    return quality


def main():
    values = read_in()
    print(values)
    print("Example P1:", sum([x * y for (x, y) in p1(None, 24)]))  # expect 33
    print("Part 1:", sum([x * y for x, y in p1(values, 24)]))  # expect 1528
    print("Example P2:", math.prod([x[1] for x in p1(None, 32)]))  # expect 56 * 62 = 3472
    print("Part 2:", math.prod([x[1] for x in p1(values[:3], 32)]))  # expect 13 * 31 * 42 = 16926


if __name__ == "__main__":
    main()
