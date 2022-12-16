import math
from itertools import combinations, chain
import re
from time import time


def read_in():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    pattern = re.compile(r"^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$")
    graph = {}
    for line in lines:
        m = pattern.match(line)
        valve = m.group(1)
        flow_rate = int(m.group(2))
        valves = m.group(3).split(", ")
        graph[valve] = {'flow_rate': flow_rate, 'edges': valves}
    return graph


# from itertools recipe
def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def build_table(graph, start_valve, max_time):
    non_zero_valves = [valve for valve in graph if graph[valve]["flow_rate"]]
    open_valve_sets = [frozenset(s) for s in powerset(non_zero_valves)]

    # table[minute][valve][open valves] = max pressure released
    table = [{valve: {open_valves: -math.inf for open_valves in open_valve_sets} for valve in graph} for _ in
             range(max_time + 1)]
    table[0][start_valve][frozenset()] = 0

    for minute in range(1, max_time + 1):
        # print(minute)
        for valve in graph:
            for open_valves in open_valve_sets:
                max_pressure_released = -math.inf

                # opening the valve
                if valve in open_valves:
                    without_this_valve_open = open_valves - {valve}
                    new_pressure = table[minute - 1][valve][without_this_valve_open] + sum(
                        graph[v]["flow_rate"] for v in without_this_valve_open)
                    max_pressure_released = max(max_pressure_released, new_pressure)

                # moving
                for previous_valve in graph[valve]["edges"]:
                    new_pressure = table[minute - 1][previous_valve][open_valves] + sum(
                        graph[v]["flow_rate"] for v in open_valves)
                    max_pressure_released = max(max_pressure_released, new_pressure)

                table[minute][valve][open_valves] = max_pressure_released

    return table


def p1(table, minutes):
    after_time = table[minutes]
    max_pressure = -math.inf
    for value in after_time.values():
        for v in value.values():
            max_pressure = max(max_pressure, v)
    return max_pressure


def p2(table, minutes):
    after_time = table[minutes]
    max_for_open_valve_sets = {}
    for value in after_time.values():
        for open_valves, max_pressure in value.items():
            if open_valves in max_for_open_valve_sets:
                max_for_open_valve_sets[open_valves] = max(max_for_open_valve_sets[open_valves], max_pressure)
            else:
                max_for_open_valve_sets[open_valves] = max_pressure

    max_for_both = -math.inf
    for human_valves, human_pressure in max_for_open_valve_sets.items():
        if human_pressure < 0:
            continue

        for elephant_valves, elephant_pressure in max_for_open_valve_sets.items():
            if len(human_valves) >= len(elephant_valves) and human_valves.isdisjoint(elephant_valves):
                max_for_both = max(max_for_both, human_pressure + elephant_pressure)

    return max_for_both


def main():
    graph = read_in()

    start = time()
    table = build_table(graph, 'AA', 30)
    print("Table time: {:.3f}s".format(time() - start))

    start = time()
    print(p1(table, 30))
    print("Part 1 time: {:.3f}s".format(time() - start))

    start = time()
    print(p2(table, 26))
    print("Part 2 time: {:.3f}s".format(time() - start))


if __name__ == "__main__":
    main()
