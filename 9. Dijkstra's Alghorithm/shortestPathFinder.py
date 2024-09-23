from heapq import heappop, heappush
from collections import defaultdict

class ShortestPath():
    def __init__(self) -> None:
        pass
    
    def makeGraph(self, edges) -> dict:
        g = defaultdict(dict)
        for s, e, w in edges:
            g[s][e] = w
            g[e][s] = w
        return g
    
    def dijkstra(self, start, graph) -> dict:
        dist = {node: float("inf") for node in graph}
        dist[start] = 0

        q, visited = [(0, start)], set()
        
        while q:
            curr_dist, node = heappop(q)
            if node in visited:
                continue

            visited.add(node)
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    new_dist = curr_dist + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heappush(q, (new_dist, neighbor))
        return dist


if __name__ == "__main__":
    # start, end, weight
    edges = [
        (1, 2, 7),
        (1, 4, 5),
        (2, 3, 8),
        (2, 4, 9),
        (2, 5, 7),
        (3, 5, 5),
        (4, 5, 7),
        (4, 6, 6),
        (5, 6, 8),
        (5, 7, 9),
        (6, 7, 11)
    ]
    
    g = ShortestPath()
    graph = g.makeGraph(edges)
    distances = g.dijkstra(1, graph)

    print("Shortest Distances:", distances)