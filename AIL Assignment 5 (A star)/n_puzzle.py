import heapq

class Node:
    """Represents a node in the search graph."""
    def __init__(self, state, parent=None, move=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        if self.f == other.f:
            return self.h < other.h
        return self.f < other.f

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(self.state)

def reconstruct_path(node):
    moves = []
    current = node
    while current and current.parent:
        moves.append(current.move)
        current = current.parent
    moves.reverse()
    return moves

def reconstruct_states(node):
    states = []
    current = node
    while current:
        states.append(current.state)
        current = current.parent
    states.reverse()
    return states

def print_matrix(state, size):
    for i in range(size):
        row = state[i*size:(i+1)*size]
        print(' '.join(str(x) if x != 0 else '_' for x in row))
    print()

def find_blank(state, size):
    blank_idx = state.index(0)
    return blank_idx // size, blank_idx % size

def get_neighbors(state, size):
    neighbors = []
    blank_r, blank_c = find_blank(state, size)
    moves = [("UP", -1, 0), ("DOWN", 1, 0), ("LEFT", 0, -1), ("RIGHT", 0, 1)]
    
    for move_name, dr, dc in moves:
        new_r, new_c = blank_r + dr, blank_c + dc
        if 0 <= new_r < size and 0 <= new_c < size:
            new_state = list(state)
            blank_idx = blank_r * size + blank_c
            new_idx = new_r * size + new_c
            new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
            neighbors.append((tuple(new_state), move_name))
    return neighbors

def manhattan_distance(state, goal_state, size):
    distance = 0
    goal_positions = {}
    for i, val in enumerate(goal_state):
        if val != 0:
            goal_positions[val] = (i // size, i % size)
    for i, val in enumerate(state):
        if val != 0:
            curr_r, curr_c = i // size, i % size
            goal_r, goal_c = goal_positions[val]
            distance += abs(curr_r - goal_r) + abs(curr_c - goal_c)
    return distance

def a_star_search(start_state, goal_state, size):
    start_node = Node(start_state, g=0, h=manhattan_distance(start_state, goal_state, size))
    open_set = [start_node]
    closed_set = set()
    g_costs = {start_state: 0}
    
    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.state == goal_state:
            return current_node
        closed_set.add(current_node.state)
        
        for neighbor_state, move in get_neighbors(current_node.state, size):
            if neighbor_state in closed_set:
                continue
            tentative_g = current_node.g + 1
            if neighbor_state not in g_costs or tentative_g < g_costs[neighbor_state]:
                g_costs[neighbor_state] = tentative_g
                h_cost = manhattan_distance(neighbor_state, goal_state, size)
                neighbor_node = Node(state=neighbor_state, parent=current_node, move=move, g=tentative_g, h=h_cost)
                heapq.heappush(open_set, neighbor_node)
    return None

def is_solvable(state, size):
    """Check if the n-puzzle is solvable."""
    inv_count = 0
    state_list = [x for x in state if x != 0]
    for i in range(len(state_list)):
        for j in range(i + 1, len(state_list)):
            if state_list[i] > state_list[j]:
                inv_count += 1
    if size % 2 == 1:
        # Odd grid: solvable if inversion count is even
        return inv_count % 2 == 0
    else:
        # Even grid: blank row from bottom and inversion count determine solvability
        blank_row = size - (state.index(0) // size)
        if blank_row % 2 == 0:
            return inv_count % 2 == 1
        else:
            return inv_count % 2 == 0

def main():
    try:
        k = int(input("Enter the matrix size:\n"))
        if k <= 0:
            print("Invalid puzzle size")
            return
        initial_state = [int(input("Enter the matrix:\n")) for _ in range(k * k)]
        if len(initial_state) != k * k:
            print("Invalid number of inputs")
            return
        goal_state = tuple(i for i in range(k * k))
    except Exception as e:
        print("Invalid input")
        return

    if not is_solvable(initial_state, k):
        print("No solution found")
        return

    final_node = a_star_search(tuple(initial_state), goal_state, k)

    if final_node:
        states = reconstruct_states(final_node)
        print(len(states) - 1)
        for i, state in enumerate(states):
            print(f"Step {i}:")
            print_matrix(state, k)
        moves_list = reconstruct_path(final_node)
        for move in moves_list:
            print(move)
    else:
        print("No solution found")

if __name__ == "__main__":
    main()
