# ---------------------------------------------
# 5.1 SELECTION SORT
# ---------------------------------------------

def selection_sort(arr):
    # Get length of array
    n = len(arr)
    for i in range(n):  # Loop through array
        min_index = i  # Assume current index is minimum
        for j in range(i + 1, n):  # Search remaining array
            if arr[j] < arr[min_index]:  # Find smaller element
                min_index = j  # Update minimum index
        # Swap smallest element with current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    arr = []  # Initialize array
    while True:
        print("\n----- Menu -----")
        print("1. Enter elements")
        print("2. Sort using Selection Sort")
        print("3. Display array")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            arr = []  # Reset array
            n = int(input("How many numbers do you want to enter? "))
            for i in range(n):
                num = int(input(f"Enter number {i+1}: "))
                arr.append(num)  # Add number to list

        elif choice == '2':
            selection_sort(arr)  # Call sort function
            print("Array sorted successfully.")

        elif choice == '3':
            print("Current array:", arr)  # Display array contents

        elif choice == '4':
            print("Exiting program.")
            break  # Exit loop

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

# ---------------------------------------------
# 5.2 PRIM'S MINIMUM SPANNING TREE
# ---------------------------------------------

def find_min_vertex(key, visited, V):
    # Find vertex with minimum key value not yet visited
    min_val = float('inf')
    min_index = -1
    for i in range(V):
        if not visited[i] and key[i] < min_val:
            min_val = key[i]
            min_index = i
    return min_index

def prim_mst(graph, V):
    key = [float('inf')] * V  # Store min weights
    parent = [-1] * V  # Store MST tree
    visited = [False] * V  # Track visited nodes

    key[0] = 0  # Start from vertex 0

    for _ in range(V):
        u = find_min_vertex(key, visited, V)  # Select minimum key vertex
        visited[u] = True  # Mark visited

        for v in range(V):
            # Check adjacency & update if smaller weight found
            if graph[u][v] != 0 and not visited[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    print("\n Minimum Spanning Tree (MST):")
    print("Edge\tWeight")
    total = 0
    for i in range(1, V):
        print(f"{parent[i]+1} - {i+1}\t{graph[i][parent[i]]}")  # Print edges
        total += graph[i][parent[i]]
    print("Total weight of MST:", total)

def main():
    graph = []  # Adjacency matrix input
    V = 0

    while True:
        print("\n----- Menu -----")
        print("1. Enter Graph (Adjacency Matrix)")
        print("2. Find Minimum Spanning Tree")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            graph = []
            V = int(input("Enter number of vertices: "))
            print("Enter adjacency matrix row by row (use 0 if no edge):")
            for i in range(V):
                row_input = input(f"Row {i+1}: ").split()
                if len(row_input) != V:
                    print("Please enter exactly", V, "values.")
                    break
                graph.append(list(map(int, row_input)))  # Convert to int list
            else:
                print("Graph saved successfully.")

        elif choice == '2':
            if not graph:
                print("Graph not entered yet. Please enter graph first.")
            else:
                prim_mst(graph, V)  # Call Prim’s algorithm

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

# ---------------------------------------------
# 5.3 KRUSKAL'S MINIMUM SPANNING TREE
# ---------------------------------------------

def find_parent(parent, node):
    # Find root parent using recursion
    if parent[node] == node:
        return node
    return find_parent(parent, parent[node])

def union(parent, u, v):
    # Union two sets by root
    parent_v = find_parent(parent, v)
    parent_u = find_parent(parent, u)
    parent[parent_v] = parent_u

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    parent = {v: v for v in vertices}  # Parent set
    mst = []  # Store final MST
    total_weight = 0

    for u, v, w in edges:
        if find_parent(parent, u) != find_parent(parent, v):
            mst.append((u, v, w))  # Add edge to MST
            total_weight += w
            union(parent, u, v)  # Join sets

    return mst, total_weight

def main():
    vertices = []
    edges = []

    while True:
        print("\n--- MENU ---")
        print("1. Add Vertex")
        print("2. Add Edge")
        print("3. Show Graph")
        print("4. Find MST (Kruskal's Algorithm)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            v = input("Enter vertex: ")
            if v not in vertices:
                vertices.append(v)
                print("Vertex added.")
            else:
                print("Vertex already exists.")

        elif choice == '2':
            u = input("Enter first vertex: ")
            v = input("Enter second vertex: ")
            w = int(input("Enter edge weight: "))
            edges.append((u, v, w))  # Store edge triplet
            print("Edge added.")

        elif choice == '3':
            print("Vertices:", vertices)
            print("Edges:")
            for edge in edges:
                print(edge)

        elif choice == '4':
            if len(vertices) == 0 or len(edges) == 0:
                print("Graph is empty. Please add vertices and edges.")
            else:
                mst, weight = kruskal(vertices, edges)
                print("\nMinimum Spanning Tree:")
                for u, v, w in mst:
                    print(f"{u} -- {v} : {w}")
                print("Total Weight:", weight)

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

# ---------------------------------------------
# 5.4 JOB SCHEDULING (GREEDY)
# ---------------------------------------------

def job_scheduling(jobs, max_deadline):
    jobs.sort(key=lambda job: job[2], reverse=True)  # Sort by profit
    slots = [None] * max_deadline  # Time slots
    total_profit = 0
    scheduled_jobs = []

    for job_id, deadline, profit in jobs:
        # Try latest free slot <= deadline
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                scheduled_jobs.append(job_id)
                break  # Job placed

    return scheduled_jobs, total_profit

def main():
    jobs = []  # Store jobs list

    while True:
        print("\n--- Job Scheduling Menu ---")
        print("1. Add Job")
        print("2. Schedule Jobs")
        print("3. Show All Jobs")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            job_id = input("Enter Job ID: ")
            deadline = int(input("Enter Deadline: "))
            profit = int(input("Enter Profit: "))
            jobs.append((job_id, deadline, profit))  # Store job tuple

        elif choice == '2':
            if not jobs:
                print("No jobs to schedule. Add jobs first.")
                continue
            max_deadline = int(input("Enter maximum deadline: "))
            scheduled, profit = job_scheduling(jobs, max_deadline)
            print("\nScheduled Jobs:", scheduled)
            print("Total Profit:", profit)

        elif choice == '3':
            if not jobs:
                print("No jobs added yet.")
            else:
                for job in jobs:
                    print(f"ID:{job[0]}, Deadline:{job[1]}, Profit:{job[2]}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Enter 1-4.")

if __name__ == "__main__":
    main()

# ---------------------------------------------
# 5.5 DIJKSTRA SHORTEST PATH (MST-style input)
# ---------------------------------------------

def dijkstra(graph, start):
    visited = set()  # Track visited nodes
    distances = {v: float('inf') for v in graph}  # Init distances
    distances[start] = 0

    while visited != set(graph.keys()):
        min_vertex = None
        for v in graph:
            if v not in visited and (min_vertex is None or distances[v] < distances[min_vertex]):
                min_vertex = v

        if distances[min_vertex] == float('inf'):
            break

        visited.add(min_vertex)

        for neighbor, weight in graph[min_vertex].items():
            if neighbor not in visited:
                new_distance = distances[min_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

def main():
    graph = {}  # Store graph as adjacency list

    while True:
        print("\nMenu:")
        print("1. Add edge")
        print("2. Show graph")
        print("3. Find shortest path (Dijkstra)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            u = input("Enter start vertex: ")
            v = input("Enter end vertex: ")
            w = float(input("Enter weight: "))
            if u not in graph: graph[u] = {}
            if v not in graph: graph[v] = {}
            graph[u][v] = w  # Directed edge

        elif choice == '2':
            for u in graph:
                for v in graph[u]:
                    print(f"{u} --{graph[u][v]}--> {v}")

        elif choice == '3':
            start = input("Enter start vertex: ")
            if start not in graph:
                print("Vertex not found!")
            else:
                dist = dijkstra(graph, start)
                for v in dist:
                    print(f"{v}: {dist[v]}")

        elif choice == '4':
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

# ---------------------------------------------
# 5.6 SINGLE-SOURCE SHORTEST PATH (DIJKSTRA)
# ---------------------------------------------

def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}  # Init
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_vertex = None
        for v in graph:
            if v not in visited and (min_vertex is None or distances[v] < distances[min_vertex]):
                min_vertex = v

        if distances[min_vertex] == float('inf'):
            break

        visited.add(min_vertex)

        for neighbor, weight in graph[min_vertex].items():
            if neighbor not in visited:
                new_dist = distances[min_vertex] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist

    return distances

def main():
    graph = {}  # Adjacency list

    while True:
        print("\nMenu:")
        print("1. Add edge")
        print("2. Show graph")
        print("3. Find shortest path from source")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            u = input("Enter start vertex: ")
            v = input("Enter end vertex: ")
            w = float(input("Enter weight: "))
            if u not in graph: graph[u] = {}
            if v not in graph: graph[v] = {}
            graph[u][v] = w

        elif choice == '2':
            for u in graph:
                for v in graph[u]:
                    print(f"{u} --{graph[u][v]}--> {v}")

        elif choice == '3':
            start = input("Enter source vertex: ")
            if start not in graph:
                print("Source not found!")
            else:
                dist = dijkstra(graph, start)
                for v,d in dist.items():
                    print(f"{v}: {d}")

        elif choice == '4':
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()





































# ---------------------------------------------
# NOTES & THEORY FOR ORAL / VIVA
# ---------------------------------------------

# 1. SELECTION SORT
# -----------------
# - Selection Sort is a comparison-based sorting algorithm.
# - Algorithm:
#   1. Traverse the array.
#   2. Find the minimum element in unsorted part.
#   3. Swap it with the first element of unsorted part.
#   4. Repeat until array is sorted.
# - Time Complexity: O(n^2)
# - Space Complexity: O(1) (in-place)
# - Stable: No, because swapping may change order of equal elements.
# - Used for: small arrays or educational purposes.

# 2. PRIM'S MINIMUM SPANNING TREE
# -------------------------------
# - Finds MST (Minimum Spanning Tree) of a connected weighted graph.
# - Starts from any vertex, adds edges with minimum weight connecting visited and unvisited vertices.
# - Data structures used:
#   - key[]: store minimum weight edge to a vertex.
#   - parent[]: store parent vertex to print MST edges.
#   - visited[]: track included vertices in MST.
# - Time Complexity: O(V^2) for adjacency matrix (can be improved with heap)
# - Output: MST edges and total weight.

# 3. KRUSKAL'S MINIMUM SPANNING TREE
# -----------------------------------
# - Finds MST using edge list.
# - Algorithm:
#   1. Sort all edges by weight.
#   2. Pick smallest edge and check if it forms a cycle (using Union-Find).
#   3. Include edge if no cycle; else skip.
#   4. Repeat until MST has (V-1) edges.
# - Union-Find is used to efficiently check cycles.
# - Time Complexity: O(E log E) due to sorting.
# - Space Complexity: O(V) for parent array.
# - Good for sparse graphs.

# 4. JOB SCHEDULING (GREEDY APPROACH)
# -----------------------------------
# - Problem: Schedule jobs to maximize profit with deadlines.
# - Algorithm:
#   1. Sort jobs in decreasing order of profit.
#   2. Place each job in latest available slot before its deadline.
#   3. Skip if slot not available.
# - Uses greedy strategy (chooses locally optimal for max profit)
# - Time Complexity: O(n log n) for sorting + O(n * d) for scheduling (d = max deadline)
# - Output: Scheduled jobs and total profit.

# 5. DIJKSTRA'S SHORTEST PATH (SINGLE SOURCE)
# --------------------------------------------
# - Finds shortest paths from a source vertex to all other vertices in a weighted graph (non-negative weights).
# - Algorithm:
#   1. Initialize distances to infinity; distance[source] = 0.
#   2. Pick unvisited vertex with smallest distance.
#   3. Update distances of adjacent vertices if new distance is smaller.
#   4. Mark vertex as visited and repeat.
# - Data structures:
#   - distances dict: stores shortest path cost.
#   - visited set: marks processed vertices.
# - Time Complexity: O(V^2) with simple array (can be O(E + V log V) with min-heap)
# - Output: Shortest distance from source to all vertices.

# 6. COMMON FUNCTIONS USED
# ------------------------
# - len(arr): Returns number of elements in array/list.
# - input(): Read input from user.
# - int()/float(): Type casting user input to numbers.
# - append(): Add element to list.
# - sort(): Sort list; in job scheduling, sorted() with key parameter.
# - min()/max(): Find minimum or maximum value.
# - dict(): Store graph as adjacency list (vertex: {neighbor: weight})
# - list comprehension: For initializing board, arrays, or adjacency matrices.
# - set(): Store visited vertices for uniqueness.
# - heapq (in other MST / search algos): Priority queue for selecting min value.
# - tuple: Store edge or job data as (u, v, weight) or (id, deadline, profit).

# 7. TERMINOLOGY
# ---------------
# - MST (Minimum Spanning Tree): Connect all vertices with minimum total edge weight without cycles.
# - Greedy Algorithm: Makes locally optimal choice hoping global optimum achieved.
# - Backtracking / Branch & Bound: Systematically explore all solutions while pruning invalid ones.
# - Vertex/Node: A point in graph.
# - Edge: Connection between vertices.
# - Weight: Cost associated with an edge.
# - Deadline: Latest time a job can be scheduled.
# - Profit: Reward for completing a job.
# - Distance: Shortest path value from source vertex.

# 8. HOW TO EXPLAIN OUTPUT
# -------------------------
# - Selection Sort: Prints sorted array after sorting.
# - Prim's MST: Prints each edge in MST and total weight.
# - Kruskal's MST: Prints edges in MST and total weight.
# - Job Scheduling: Prints scheduled jobs and total profit.
# - Dijkstra: Prints shortest distance from source to all vertices.
# - All programs use menu-driven interface for interactive input.
# - User enters graph/array/jobs, chooses algorithm, and sees results dynamically.
