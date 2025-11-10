# Depth First Search (DFS) and Breadth First Search (BFS) on an undirected graph
# Implemented in Python with user menu for dynamic graph creation

from collections import deque  # Required for BFS queue

# ------------------------- DFS Implementation -------------------------
# Recursive DFS function
def dfs(graph, node, visited, traversal):
    """
    Perform Depth First Search recursively.

    Parameters:
    graph     : dict  : adjacency list representation of graph
    node      : str   : current node being visited
    visited   : set   : set of visited nodes
    traversal : list  : list storing the DFS traversal order
    """
    visited.add(node)            # Mark current node as visited
    traversal.append(node)       # Add node to traversal path

    # Explore all neighbors of current node
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal)  # Recursive call for unvisited neighbor

# ------------------------- BFS Implementation -------------------------
def bfs(graph, start):
    """
    Perform Breadth First Search iteratively using a queue.

    Parameters:
    graph : dict : adjacency list representation of graph
    start : str  : starting node for BFS

    Returns:
    traversal : list : list storing BFS traversal order
    """
    visited = set()              # Track visited nodes
    traversal = []               # Store BFS traversal order
    queue = deque([start])       # Queue for BFS, starting with the start node
    visited.add(start)

    while queue:
        node = queue.popleft()   # Dequeue node
        traversal.append(node)   # Add to traversal

        # Explore all neighbors of current node
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)  # Mark as visited
                queue.append(neighbor) # Enqueue for future exploration

    return traversal

# ------------------------- Main Program -------------------------
def main():
    graph = {}  # Dictionary to store adjacency list of undirected graph

    while True:
        # Display menu to the user
        print("\nGraph Traversal Menu:")
        print("1. Add edge (undirected)")
        print("2. Show graph")
        print("3. Perform DFS Traversal")
        print("4. Perform BFS Traversal")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # ---------------- Add edge ----------------
        if choice == '1':
            u = input("Enter vertex 1: ")
            v = input("Enter vertex 2: ")

            # Initialize adjacency lists if nodes not present
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            # Add edge both ways for undirected graph
            graph[u].append(v)
            graph[v].append(u)
            print(f"Edge added between {u} and {v}")

        # ---------------- Show graph ----------------
        elif choice == '2':
            print("Graph adjacency list:")
            for node in graph:
                print(f"{node}: {graph[node]}")

        # ---------------- DFS Traversal ----------------
        elif choice == '3':
            start = input("Enter starting vertex for DFS: ")
            if start not in graph:
                print("Vertex not found in graph.")
            else:
                visited = set()  # Keep track of visited nodes
                traversal = []   # Store DFS traversal order
                dfs(graph, start, visited, traversal)
                print("DFS Traversal Order:", traversal)

        # ---------------- BFS Traversal ----------------
        elif choice == '4':
            start = input("Enter starting vertex for BFS: ")
            if start not in graph:
                print("Vertex not found in graph.")
            else:
                traversal = bfs(graph, start)
                print("BFS Traversal Order:", traversal)

        # ---------------- Exit ----------------
        elif choice == '5':
            print("Exiting program...")
            break

        # Invalid choice
        else:
            print("Invalid choice. Please try again.")

# Execute main program
if __name__ == "__main__":
    main()

































# ------------------------- Theory Notes -------------------------
# 1. Graph: A collection of vertices (nodes) connected by edges.
# 2. DFS: Depth First Search explores as far as possible along a branch before backtracking.
# 3. BFS: Breadth First Search explores neighbors level by level.
# 4. DFS uses recursion (or an explicit stack), BFS uses a queue.
# 5. Visited set prevents infinite loops in cyclic graphs.
# 6. Adjacency list: Dictionary where keys are nodes, values are lists of neighbors.
# 7. Undirected graph: Edges have no direction, meaning connections go both ways.
# 8. DFS is useful for path finding, topological sorting, and connectivity checking.
# 9. BFS is useful for shortest path in unweighted graphs, level-order traversal.
# 10. Traversal: Visiting every node of the graph in a specific order.

# Viva/Oral Questions for DFS & BFS Practical

# 1. What is a graph?
#    A graph is a data structure consisting of vertices (nodes) and edges (connections between nodes).
#    It is used to represent relationships such as social networks, maps, or networks of computers.

# 2. What is DFS?
#    DFS (Depth First Search) is a graph traversal algorithm that explores a path fully before moving to the next path.
#    It goes deep into one branch until no further nodes are available, then backtracks.

# 3. What is BFS?
#    BFS (Breadth First Search) is a graph traversal algorithm that visits nodes level by level.
#    It explores all neighbors of a node before moving to the next level.

# 4. Data structure used in DFS?
#    DFS uses a stack. In recursive DFS, the call stack is used automatically by the system.

# 5. Data structure used in BFS?
#    BFS uses a queue to ensure nodes are processed in First-In-First-Out order.

# 6. Why use recursion in DFS?
#    DFS is naturally depth-oriented, and recursion simplifies the process by automatically managing the backtracking steps.

# 7. Difference between DFS and BFS?
#    DFS goes deep first and backtracks later. BFS explores level by level.
#    DFS finds long paths, suitable for problems like maze solving. BFS is better for shortest path problems.

# 8. Why maintain a visited set?
#    To avoid revisiting nodes, prevent infinite loops, and ensure each node is processed only once.

# 9. What is an undirected graph?
#    A graph where edges do not have a direction. If A is connected to B, then B is also connected to A.

# 10. What is an adjacency list?
#     A way of storing a graph where each vertex stores a list of its adjacent vertices.
#     It is efficient in terms of memory for sparse graphs.

# 11. Why is adjacency list used here instead of adjacency matrix?
#     Adjacency lists use less memory and are easier to manage when the graph has fewer edges.

# 12. What is traversal?
#     The process of visiting every node in a graph in some order.

# 13. When is DFS preferred?
#     Used when exploring depth completely, useful in backtracking problems, solving mazes, or checking connectivity.

# 14. When is BFS preferred?
#     Used when shortest path is required, such as in routing, networking, and level-order exploration.

# 15. Why do we break loops after finishing DFS/BFS?
#     To indicate completion of traversal and avoid unnecessary iterations once the graph is fully explored.

# 16. What happens if we do not mark visited nodes?
#     The algorithm may fall into infinite loops, especially in cyclic graphs, and nodes will be visited repeatedly.

# 17. What type of graph is used in this program?
#     An undirected graph represented using an adjacency list.

# 18. Why user input for edges?
#     To allow dynamic graph creation and to simulate real-time graph construction rather than hard-coded values.
