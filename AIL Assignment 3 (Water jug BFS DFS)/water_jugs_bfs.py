from collections import deque

def water_jug_problem(capacity1, capacity2, target):
    queue = deque([(0, 0, [])])
    visited = set((0, 0))

    while queue:
        jug1, jug2, path = queue.pop()
        path = path + [(jug1, jug2)]

        if jug2 == target:
            return path

        for next_state in get_next_states(jug1, jug2, capacity1, capacity2):
            if next_state not in visited:
                queue.append((*next_state, path))
                visited.add(next_state)

    return None

def get_next_states(jug1, jug2, capacity1, capacity2):
    states = []

    # Fill jug1
    if jug1 < capacity1:
        states.append((capacity1, jug2))

    # Fill jug2
    if jug2 < capacity2:
        states.append((jug1, capacity2))

    # Empty jug1
    if jug1 > 0:
        states.append((0, jug2))

    # Empty jug2
    if jug2 > 0:
        states.append((jug1, 0))

    # Pour jug1 to jug2
    pour_amount = min(jug1, capacity2 - jug2)
    if pour_amount > 0:
        states.append((jug1 - pour_amount, jug2 + pour_amount))

    # Pour jug2 to jug1
    pour_amount = min(jug2, capacity1 - jug1)
    if pour_amount > 0:
        states.append((jug1 + pour_amount, jug2 - pour_amount))

    return states

# Test the function
capacity1 = 3
capacity2 = 5
target = 4
result = water_jug_problem(capacity1, capacity2, target)

if result:
    print("Solution found:")
    for i, (jug1, jug2) in enumerate(result):
        print(f"Step {i+1}: Jug1 = {jug1}L, Jug2 = {jug2}L")
else:
    print("No solution found")