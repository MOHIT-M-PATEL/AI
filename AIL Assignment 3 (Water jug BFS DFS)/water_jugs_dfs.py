def dfs(capacity_x, capacity_y, target):
    stack = [(0, 0)]
    visited = set()
    path = []
    
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        path.append((x, y))
        
        if x == target or y == target:
            return path
        
        moves = [
            (capacity_x, y), (x, capacity_y), (0, y), (x, 0),
            (x - min(x, capacity_y - y), y + min(x, capacity_y - y)),
            (x + min(y, capacity_x - x), y - min(y, capacity_x - x))
        ]
        
        for move in moves:
            if move not in visited:
                stack.append(move)
    return None

capacity_x = 4
capacity_y = 3
target = 2

dfs_solution = dfs(capacity_x, capacity_y, target)
print("DFS Path:", dfs_solution)