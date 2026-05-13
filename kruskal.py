n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (use 0 if no edge):")
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

edges = []

# Store all edges
for i in range(n):
    for j in range(i + 1, n):

        if graph[i][j] != 0:
            edges.append([graph[i][j], i, j])

# Sort edges
edges.sort()

parent = [i for i in range(n)]

# Find parent
def find(i):

    while parent[i] != i:
        i = parent[i]

    return i

# Union
def union(i, j):

    parent[find(i)] = find(j)

count = 0
total_cost = 0

print("\nEdge \t Weight")

for edge in edges:

    weight = edge[0]
    x = edge[1]
    y = edge[2]

    # Check cycle
    if find(x) != find(y):

        union(x, y)

        print(f"{x} - {y} \t {weight}")

        total_cost += weight
        count += 1

    if count == n - 1:
        break

print("Total cost of MST:", total_cost)