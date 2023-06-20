import heapq
import math

class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def add_vertex(self, label):
        if not isinstance(label, str):
            raise ValueError("Label must be a string.")
        self.adj_list[label] = {}
        return self

    def add_edge(self, src, dest, w):
        if src not in self.adj_list or dest not in self.adj_list or not isinstance(w, (int, float)):
            raise ValueError("Invalid edge parameters.")
        self.adj_list[src][dest] = w
        return self

    def get_weight(self, src, dest):
        if src not in self.adj_list or dest not in self.adj_list:
            raise ValueError("Invalid vertices.")
        return self.adj_list[src].get(dest, math.inf)
    
    def dfs(self, starting_vertex):
        if starting_vertex not in self.adj_list:
            raise ValueError("Starting vertex not found.")
        visited = set()
        stack = [starting_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in sorted(self.adj_list[vertex], reverse=True):
                    stack.append(neighbor)
                yield vertex

    def bfs(self, starting_vertex):
        if starting_vertex not in self.adj_list:
            raise ValueError("Starting vertex not found.")
        visited = set()
        queue = [starting_vertex]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in sorted(self.adj_list[vertex]):
                    queue.append(neighbor)
                yield vertex
                
    def dsp(self, src, dest):
        min_heap = [(0, src, [])]
        visited = set()
        while min_heap:
            (cost, current, path) = heapq.heappop(min_heap)
            if current not in visited:
                visited.add(current)
                path = path + [current]
                if current == dest:
                    return cost, path
                for neighbor, weight in self.adj_list[current].items():
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (cost + weight, neighbor, path))
        return math.inf, []

    
    def dsp_all(self, src):
        result = {src : (0, [src])}
        for vertex in self.adj_list:
            if vertex != src:
                result[vertex] = self.dsp(src, vertex)
        return result


    def __str__(self):
        result = "digraph G {\n"
        for src, edges in self.adj_list.items():
            for dest, weight in edges.items():
                result += f'   {src} -> {dest} [label="{weight:.1f}",weight="{weight:.1f}"];\n'
        result += "}"
        return result


def main():
    G = Graph()
    G.add_vertex("A").add_vertex("B").add_vertex("C").add_vertex("D").add_vertex("E").add_vertex("F")
    G.add_edge("A", "B", 2).add_edge("A", "F", 9).add_edge("B", "C", 8).add_edge("B", "D", 15).add_edge("B", "F", 6)
    G.add_edge("C", "D", 1).add_edge("E", "C", 7).add_edge("E", "D", 3).add_edge("F", "B", 6).add_edge("F", "E", 3)

    print(G)

    print("Starting BFS with Vertex A")
    for vertex in G.bfs("A"):
        print(vertex, end="")
    print()

    print("Starting DFS with Vertex A")
    for vertex in G.dfs("A"):
        print(vertex, end="")
    print()

    print("Dijkstra's Shortest Path from A to F")
    print(G.dsp("A", "F"))
    
    print("Dijkstra's Shortest Path from A to all vertices")
    all_shortest_paths = G.dsp_all("A")
    for vertex, (_, path) in sorted(all_shortest_paths.items(), key=lambda x: x[0]):
        print(f"{{{vertex}: {path}}}", end=" ")
    print()

if __name__ == "__main__":
    main()
