# -------- Graph Creation --------
graph = {}

n = int(input("Number of vertices: "))
for i in range(n):
    v = input(f"Enter vertex {i+1}: ").strip()
    graph[v] = []

e = int(input("Number of edges: "))
print("Enter edges (v1 v2):")
for i in range(e):
    u, v = input(f"Edge {i+1}: ").split()
    u, v = u.strip(), v.strip()
    graph[u].append(v)
    graph[v].append(u)   # undirected


# -------- DFS (Recursive) --------
def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")
    
    for nbr in graph[node]:
        if nbr not in visited:
            dfs(nbr, visited)


# -------- BFS (Recursive) --------
def bfs(queue, visited):
    if not queue:
        return
    
    node = queue.pop(0)
    print(node, end=" ")
    
    for nbr in graph[node]:
        if nbr not in visited:
            visited.add(nbr)
            queue.append(nbr)
    
    bfs(queue, visited)


# -------- Driver --------
start = input("Starting vertex: ").strip()

print("\nDFS:")
dfs(start, set())

print("\nBFS:")
bfs([start], set([start]))