import heapq
import math

class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def add_vertex(self, label):
        if not isinstance(label, str): #label must be a string
            raise ValueError("Label must be a string.")
        self.adj_list[label] = {} #dic에 label을 새로운 키로 추가
        return self

    def add_edge(self, src, dest, w): #src,dest == start & end  vertices of the edge
        if src not in self.adj_list or dest not in self.adj_list or not isinstance(w, (int, float)):
            raise ValueError("Invalid edge parameters.")
        self.adj_list[src][dest] = w #  adds dest as a key, assigns the weight w
        return self

    def get_weight(self, src, dest):
        if src not in self.adj_list or dest not in self.adj_list:
            raise ValueError("Invalid vertices.")
        return self.adj_list[src].get(dest, math.inf) #get으로 dest로의 edge weight갖고온다.
    
    def dfs(self, starting_vertex):
        if starting_vertex not in self.adj_list:
            raise ValueError("Starting vertex not found.")
        visited = set()
        stack = [starting_vertex] #시작 vertex point는 스택으로넣고
        while stack: #스택이 빌떄까지
            vertex = stack.pop() #vertex 꺼냄
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in sorted(self.adj_list[vertex], reverse=True): 
                    #해당 정점, 인접한 vertex 축가. 
                    # 인접한 곳으로 가서 탐색 그리고 다시 돌아옴
                    stack.append(neighbor)
                yield vertex #generator(수업자료) 따라함

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
        min_heap = [(0, src, [])] #cost, vertex, path
        visited = set()
        while min_heap:
            (cost, current, path) = heapq.heappop(min_heap) #mh에서 cost가 가장 작은 튜플
            if current not in visited:
                visited.add(current)
                path = path + [current] #path 에 current추가
                if current == dest: #같으면 최단거리
                    return cost, path
                for neighbor, weight in self.adj_list[current].items():
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (cost + weight, neighbor, path))
                        #adjacent reach하기 위한 비용, cos는cost to reach the current vertex
        #weight is the weight of the edge between the current vertex and the neighboring vertex
        return math.inf, []

    
    def dsp_all(self, src): #shortest 경로 찾기
        result = {src : (0, [src])} #src==키, 비용==0 경로==[src]
        for vertex in self.adj_list:
            if vertex != src:
                result[vertex] = self.dsp(src, vertex) #start vertex src부터 현재 ver 경로 계산
        return result


    def __str__(self):
        result = "digraph G {\n"
        for src, edges in self.adj_list.items():
            for dest, weight in edges.items(): #iterate the edges connected to the current vertex, Each edge consists of a destination vertex (dest) and its weight (weight).
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
    for vertex, (_, path) in sorted(all_shortest_paths.items(), key=lambda x: x[0]): #dic key를 기준으로 정렬
        print(f"{{{vertex}: {path}}}", end=" ") #각 ver과 해당 path
    print()

if __name__ == "__main__":
    main()
