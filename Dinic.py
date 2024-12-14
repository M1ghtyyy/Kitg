from collections import deque, defaultdict

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list) 
        self.capacity = defaultdict(lambda: defaultdict(int)) 

    def add_edge(self, u, v, cap):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[u][v] += cap
        self.capacity[v][u] += 0 

    def bfs(self, source, sink, level):
        for i in range(self.n):
            level[i] = -1
        level[source] = 0
        queue = deque([source])

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if level[v] == -1 and self.capacity[u][v] > 0:
                    level[v] = level[u] + 1
                    queue.append(v)

        return level[sink] != -1

    def dfs(self, u, sink, flow, level, ptr):
        if u == sink:
            return flow
        while ptr[u] < len(self.graph[u]):
            v = self.graph[u][ptr[u]]
            if level[v] == level[u] + 1 and self.capacity[u][v] > 0:
                pushed = self.dfs(v, sink, min(flow, self.capacity[u][v]), level, ptr)
                if pushed > 0:
                    self.capacity[u][v] -= pushed
                    self.capacity[v][u] += pushed
                    return pushed
            ptr[u] += 1
        return 0

    def max_flow(self, source, sink):
        total_flow = 0
        level = [-1] * self.n

        while self.bfs(source, sink, level):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(source, sink, float('inf'), level, ptr)
                if pushed == 0:
                    break
                total_flow += pushed

        return total_flow


if __name__ == "__main__":
    n = 6 
    dinic = Dinic(n)

    dinic.add_edge(0, 1, 10)
    dinic.add_edge(0, 2, 10)
    dinic.add_edge(1, 2, 2)
    dinic.add_edge(1, 3, 4)
    dinic.add_edge(1, 4, 8)
    dinic.add_edge(2, 4, 9)
    dinic.add_edge(3, 5, 10)
    dinic.add_edge(4, 3, 6)
    dinic.add_edge(4, 5, 10)

    source = 0
    sink = 5

    print("Максимальный поток:", dinic.max_flow(source, sink)) # output -> 19
