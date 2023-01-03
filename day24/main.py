import functools
import math
import sys

sys.setrecursionlimit(2000)  # will work at default recursion depth (1000) for part 1 (set MINUTE_LIMIT to 300)
MINUTE_LIMIT = 900  # chosen as an upper limit to avoid reaching maximum recursion limit


class States:
    def __init__(self, initial_grid):
        self.states = [initial_grid]
        self.repeats_after = math.lcm(len(initial_grid) - 2, len(initial_grid[0]) - 2)
        for _ in range(self.repeats_after):
            self.next_state()

    # def get(self, n):
    #     if n < len(self.states) - 1:
    #         return self.states[n]
    #     else:
    #         for _ in range(len(self.states), n + 1):
    #             self.next_state()
    #         return self.states[-1]

    def get(self, n):
        return self.states[n % self.repeats_after]

    def next_state(self):
        grid = self.states[-1]
        new_grid = [[[] for _ in row] for row in grid]

        for r, row in enumerate(grid):
            for c, column in enumerate(row):
                for ch in column:
                    if ch == '#':
                        new_grid[r][c] = ['#']
                    elif ch == '<':
                        if c != 1:
                            new_grid[r][c - 1].append('<')
                        else:
                            new_grid[r][len(row) - 2].append('<')
                    elif ch == '>':
                        if c != len(row) - 2:
                            new_grid[r][c + 1].append('>')
                        else:
                            new_grid[r][1].append('>')
                    elif ch == '^':
                        if r != 1:
                            new_grid[r - 1][c].append('^')
                        else:
                            new_grid[len(grid) - 2][c].append('^')
                    elif ch == 'v':
                        if r != len(grid) - 2:
                            new_grid[r + 1][c].append('v')
                        else:
                            new_grid[1][c].append('v')

        self.states.append(new_grid)

    def display_all(self):
        for state in self.states:
            for line in state:
                print(line)
            print()

    def display_one(self, n):
        for line in self.get(n):
            print(line)


def read_in():
    with open("input.txt", "r") as f:
        lines = [[[j] if j not in ['.', 'E'] else [] for j in i.strip()] for i in f.readlines()]
    return lines


global grid_states


def p1(grid):
    exp = (0, 1)
    target = (len(grid) - 1, len(grid[0]) - 2)
    return search(0, exp, target)

#
# @functools.cache
# def search(minute, exp, target):
#     if exp == target or minute > MINUTE_LIMIT:
#         return minute
#     m = math.inf
#     if not grid_states.get(minute + 1)[exp[0]][exp[1]]:
#         m = search(minute + 1, exp, target)
#     if not grid_states.get(minute + 1)[exp[0] - 1][exp[1]]:
#         m = min(m, search(minute + 1, (exp[0] - 1, exp[1]), target))
#     if exp[0] < len(grid_states.get(minute)) - 1 and not grid_states.get(minute + 1)[exp[0] + 1][exp[1]]:
#         m = min(m, search(minute + 1, (exp[0] + 1, exp[1]), target))
#     if not grid_states.get(minute + 1)[exp[0]][exp[1] - 1]:
#         m = min(m, search(minute + 1, (exp[0], exp[1] - 1), target))
#     if not grid_states.get(minute + 1)[exp[0]][exp[1] + 1]:
#         m = min(m, search(minute + 1, (exp[0], exp[1] + 1), target))
#     return m


def search(start_minute, start_pos, target):
    queue = [(start_minute, start_pos)]
    visited = set()

    while queue:
        minute, pos = queue.pop(0)

        if (minute, pos) in visited:
            continue
        visited.add((minute, pos))

        if pos == target:
            return minute

        g = grid_states.get(minute + 1)
        if not g[pos[0]][pos[1]]:
            queue.append((minute + 1, pos))
        if pos[0]+1 < len(g) and not g[pos[0] + 1][pos[1]]:
            queue.append((minute + 1, (pos[0] + 1, pos[1])))
        if pos[0]-1 >= 0 and not g[pos[0] - 1][pos[1]]:
            queue.append((minute + 1, (pos[0] - 1, pos[1])))
        if pos[1]+1 < len(g[0]) and not g[pos[0]][pos[1] + 1]:
            queue.append((minute + 1, (pos[0], pos[1] + 1)))
        if pos[1]-1 >= 0 and not g[pos[0]][pos[1] - 1]:
            queue.append((minute + 1, (pos[0], pos[1] - 1)))


def p2(grid):
    exp = (0, 1)
    target = (len(grid) - 1, len(grid[0]) - 2)
    minute = search(0, exp, target)
    print(minute, exp, target)

    exp, target = target, exp
    minute = search(minute, exp, target)
    print(minute, exp, target)

    exp, target = target, exp
    minute = search(minute, exp, target)
    print(minute, exp, target)
    return minute


def main():
    grid = read_in()
    global grid_states
    grid_states = States(grid)
    # for line in values:
    #     print(line)
    import time
    t = time.time()
    print(p1(grid))
    print(time.time() - t)
    import time
    t = time.time()
    print(p2(grid))
    print(time.time() - t)


if __name__ == "__main__":
    main()
