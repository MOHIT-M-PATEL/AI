import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def isValid(graph, color, v, c, V):
    """Check if color c is valid for vertex v"""
    for i in range(V):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def mColoring(graph, m_colors, color, v, V):
    """Use backtracking to assign colors"""
    # Base case: If all vertices are assigned a color
    if v == V:
        return True
    
    # Try different colors for vertex v
    for c in range(1, m_colors + 1):
        # Check if assignment of color c to v is valid
        if isValid(graph, color, v, c, V):
            color[v] = c
            
            # Recur to assign colors to the rest of the vertices
            if mColoring(graph, m_colors, color, v + 1, V):
                return True
            
            # If assigning color c doesn't lead to a solution, remove it
            color[v] = 0
    
    # If no color can be assigned to this vertex
    return False

def solve_and_visualize_graph_coloring(graph, m_colors):
    """Solve the graph coloring problem and visualize it"""
    V = len(graph)
    color = [0] * V  # Initialize all vertices with color 0
    
    # Try to color the graph using m_colors
    if not mColoring(graph, m_colors, color, 0, V):
        print("Solution does not exist with", m_colors, "colors.")
        return None
    
    print("Assigned Colors are:")
    print(" ".join(str(c) for c in color))
    
    # Create a graph for visualization
    G = nx.Graph()
    
    # Add nodes and edges
    for i in range(V):
        G.add_node(i)
    
    for i in range(V):
        for j in range(i+1, V):
            if graph[i][j] == 1:
                G.add_edge(i, j)
    
    # Define color map
    color_map = {
        0: 'white',
        1: 'red',
        2: 'green',
        3: 'blue',
        4: 'yellow',
        5: 'purple',
        6: 'orange'
    }
    
    # Map numeric colors to actual colors for visualization
    node_colors = [color_map[color[i]] for i in range(V)]
    
    # Position nodes in a circle layout
    pos = nx.circular_layout(G)
    
    # Create figure
    plt.figure(figsize=(10, 8))
    
    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color=node_colors, 
            node_size=3000, font_size=16, font_weight='bold',
            edge_color='black', width=2, font_color='black')
    
    # Add title and legend
    plt.title(f"Graph Coloring with {m_colors} Colors", fontsize=16)
    
    # Create legend
    used_colors = set(color)
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', 
                                 markerfacecolor=color_map[c], markersize=15, 
                                 label=f'Color {c}') for c in used_colors if c > 0]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    plt.axis('off')
    
    return plt.gcf()

# Example from provided code
V = 4
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]
m_colors = 3  # Number of colors

# Solve and visualize
fig = solve_and_visualize_graph_coloring(graph, m_colors)
plt.show()