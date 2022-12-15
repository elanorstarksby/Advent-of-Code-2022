import re


def read_in():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    pattern = re.compile(r"^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$")
    values = []
    for line in lines:
        m = pattern.match(line)
        values.append(tuple([int(m.group(x)) for x in range(1, 5)]))
    return values


def mark_row(sensor, row_y, row_blocked):
    sx, sy, bx, by = sensor
    distance = abs(sx - bx) + abs(sy - by)
    diff = abs(row_y - sy)
    if diff > distance:
        return

    min_x = sx - (distance - diff)
    max_x = sx + (distance - diff)
    for x in range(min_x, max_x + 1):
        row_blocked.add(x)


def p1(values, row_y):
    row_blocked = set()
    beacons = set()
    for sensor in values:
        _, _, bx, by = sensor
        if by == row_y:
            beacons.add(bx)
        mark_row(sensor, row_y, row_blocked)
    no_beacons_at = row_blocked - beacons
    return len(no_beacons_at)


def sensor_interval(sensor, row_y):
    sx, sy, bx, by = sensor
    distance = abs(sx - bx) + abs(sy - by)
    diff = abs(row_y - sy)
    if diff > distance:
        return

    min_x = sx - (distance - diff)
    max_x = sx + (distance - diff)
    return min_x, max_x


def combine_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    combined = [intervals[0]]
    for current in intervals[1:]:
        if current[0] <= combined[-1][1]:
            combined[-1] = (combined[-1][0], max(combined[-1][1], current[1]))
        else:
            combined.append(current)

    return combined


def p2(values, max_xy):
    for row_y in range(max_xy):
        intervals = []
        for sensor in values:
            interval = sensor_interval(sensor, row_y)
            if interval:
                intervals.append(interval)
        intervals = combine_intervals(intervals)
        if len(intervals) > 1:
            return (intervals[0][1] + 1) * 4000000 + row_y


def main():
    values = read_in()
    # print(values)
    print(p1(values, 2000000))
    print(p2(values, 4000000))


if __name__ == "__main__":
    main()
