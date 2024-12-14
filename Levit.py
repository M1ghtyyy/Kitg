from collections import deque, defaultdict
from math import inf

def levit_shortest_path(graph, start):
    distances = {v: inf for v in graph}
    distances[start] = 0


    m0 = deque([start])  
    m1 = set()          
    m2 = set(graph.keys())
    m2.remove(start)


    while m0:
        u = m0.popleft()  

        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

                if v in m2:
                    m0.append(v)
                    m2.remove(v)
                elif v in m1:
                    m0.appendleft(v) 

        m1.add(u)

    return distances


graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

start_vertex = 0
shortest_paths = levit_shortest_path(graph, start_vertex)
print("Кратчайшие расстояния от вершины", start_vertex, ":", shortest_paths) # output -> {0: 0, 1: 3, 2: 1, 3: 4}
