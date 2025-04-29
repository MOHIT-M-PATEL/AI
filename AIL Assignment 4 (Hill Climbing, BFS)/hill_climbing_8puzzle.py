import random
import numpy as np

def manhattan_distance(state, goal):
    distance = 0
    for num in range(1, 9):  # Numbers 1-8 in the puzzle
        x1, y1 = np.where(state == num)
        x2, y2 = np.where(goal == num)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance[0]

def get_possible_moves(state):
    x, y = np.where(state == 0)  # Find blank tile
    x, y = x[0], y[0]
    moves = []
    if x > 0: moves.append((x - 1, y))  # Move Up
    if x < 2: moves.append((x + 1, y))  # Move Down
    if y > 0: moves.append((x, y - 1))  # Move Left
    if y < 2: moves.append((x, y + 1))  # Move Right
    return moves, (x, y)

def apply_move(state, move, blank_pos):
    new_state = state.copy()
    x, y = move
    bx, by = blank_pos
    new_state[bx, by], new_state[x, y] = new_state[x, y], new_state[bx, by]
    return new_state

def hill_climbing(start, goal):
    current = start
    steps = [current]
    while True:
        moves, blank_pos = get_possible_moves(current)
        next_state = None
        min_distance = manhattan_distance(current, goal)
        
        for move in moves:
            new_state = apply_move(current, move, blank_pos)
            new_distance = manhattan_distance(new_state, goal)
            if new_distance < min_distance:
                min_distance = new_distance
                next_state = new_state
        
        if next_state is None or np.array_equal(current, goal):
            return steps  # Return the list of steps taken to reach the goal
        
        current = next_state  # Move to better state
        steps.append(current)

# Example usage
start_state = np.array([[1, 2, 4], [5, 0, 7], [3, 6, 8]])
goal_state = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])

solution_steps = hill_climbing(start_state, goal_state)
print("Steps to reach goal state:")
for step in solution_steps:
    print(step, "\n")