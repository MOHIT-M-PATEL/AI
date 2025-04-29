from collections import deque 
# Define the goal state 
GOAL_STATE = ((1, 2, 3), 
(4, 5, 6), 
(7, 8, 0)) 
# Directions: Up, Down, Left, Right 
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
def is_valid(pos): 
    """Check if the position is within the grid boundaries.""" 
    return 0 <= pos[0] < 3 and 0 <= pos[1] < 3 

def get_neighbors(state): 
    """Generate all possible states from the current state by moving the 
    blank tile.""" 
    neighbors = [] 
    # Find the position of the blank tile (0) 
    for i in range(3): 
        for j in range(3): 
            if state[i][j] == 0: 
                x, y = i, j 
                break 
 
    for dx, dy in DIRECTIONS: 
        nx, ny = x + dx, y + dy 
        if is_valid((nx, ny)): 
            # Create a new state by swapping the blank with the adjacent tile 
            new_state = [list(row) for row in state] 
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y] 
            neighbors.append(tuple(tuple(row) for row in new_state)) 
 
    return neighbors 
 
 
def bfs(start_state): 
    """Perform BFS to find the shortest path from the start state to the 
    goal state.""" 
    start_state = tuple(tuple(row) for row in start_state) 
 
    if start_state == GOAL_STATE: 
        return [start_state] 
 
    queue = deque() 
    queue.append((start_state, [start_state])) 
    visited = set() 
    visited.add(start_state) 
 
    while queue: 
        current_state, path = queue.popleft() 
 
        for neighbor in get_neighbors(current_state): 
            if neighbor not in visited: 
                if neighbor == GOAL_STATE: 
                    return path + [neighbor] 
                queue.append((neighbor, path + [neighbor])) 
                visited.add(neighbor) 
 
    return None  # No solution found 
 
 
# Example usage 
if __name__ == "__main__": 
    # Define the start state 
    start_state = [ 
        [2, 1, 3], 
        [8, 6, 4], 
        [7, 0, 5] 
    ] 
 
    solution = bfs(start_state) 
 
    if solution: 
        print(f"Solution found in {len(solution) - 1} moves:") 
        for step in solution: 
            for row in step: 
                print(row) 
            print() 
    else: 
        print("No solution exists for the given start state.") 