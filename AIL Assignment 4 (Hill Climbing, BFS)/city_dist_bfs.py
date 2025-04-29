import heapq 
 
 
def best_first_search_cities(graph, heuristics, start, goal): 
    visited = set() 
    pq = [(heuristics[start], start)] 
 
    while pq: 
        h, node = heapq.heappop(pq) 
        print(f"Visiting: {node}, Heuristic: {h}") 
 
        if node == goal: 
            print("Goal reached!") 
            return 
 
        visited.add(node) 
 
        for neighbor in graph[node]: 
            if neighbor not in visited: 
                heapq.heappush(pq, (heuristics[neighbor], neighbor)) 
 
 
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': ['G'], 
    'F': [], 
'G': [] 
} 
heuristics = { 
'A': 6, 
'B': 4, 
'C': 5, 
'D': 2, 
'E': 3, 
'F': 6, 
'G': 0 
} 
best_first_search_cities(graph, heuristics, 'A', 'G')