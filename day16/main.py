import re


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node, flow_rate):
        self.nodes[node] = {'flow_rate': flow_rate, 'edges': set()}

    def add_edge(self, node1, node2):
        self.nodes[node1]['edges'].add(node2)
        self.nodes[node2]['edges'].add(node1)


def read_in():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    pattern = re.compile(
        r"^Valve (?P<name>\w+)\s+has flow rate=(?P<flow_rate>\d+);"
        r"\s+tunnel(?:s)? lead(?:s)? to valve(?:s)? (?P<valves>.+)$")
    g = Graph()
    edges = {}
    for line in lines:
        m = pattern.match(line)
        valve = m.group(1)
        flow_rate = int(m.group(2))
        valves = m.group(3).split(", ")
        g.add_node(valve, flow_rate)
        edges[valve] = valves
    for valve, valves in edges.items():
        for vs in valves:
            g.add_edge(valve, vs)
    return g


def p1(graph):
    time_left = 30
    return 0


def main():
    graph = read_in()
    print(graph.nodes)
    print(p1(graph))
    # print(p2(values))


if __name__ == "__main__":
    main()
