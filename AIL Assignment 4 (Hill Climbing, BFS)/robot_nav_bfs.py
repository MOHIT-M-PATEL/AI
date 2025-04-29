import heapq 
 
 
def manhattan(p1, p2): 
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) 
 
 
def best_first_search_robot(grid, start, goal): 
    rows, cols = len(grid), len(grid[0]) 
    visited = set() 
    pq = [(manhattan(start, goal), start)] 
 
    while pq: 
        h, (x, y) = heapq.heappop(pq) 
        print(f"Visiting: ({x}, {y}), Heuristic: {h}") 
 
        if (x, y) == goal: 
            print("Goal reached!") 
            return 
 
        visited.add((x, y)) 
 
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            nx, ny = x + dx, y + dy 
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited: 
                heapq.heappush(pq, (manhattan((nx, ny), goal), (nx, ny))) 
 
 
grid = [ 
    [0, 1, 0, 0], 
    [0, 0, 0, 1], 
    [1, 0, 1, 0], 
    [0, 0, 0, 0] 
] 
 
start = (0, 0) 
goal = (3, 3) 
best_first_search_robot(grid, start, goal) 