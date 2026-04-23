
n = int(input("Enter number of vertices: ")) 
 
print("Enter adjacency matrix (use 0 if no edge):") 
graph = [] 
for i in range(n): 
    graph.append(list(map(int, input().split()))) 
 
selected = [False] * n 
selected[0] = True  # start from vertex 0 
 
edges = 0 
total_cost = 0 
 
print("\nEdge \t Weight") 
 
while edges < n - 1: 
    minimum = float('inf') 
    x = 0 
    y = 0 
 
    for i in range(n): 
        if selected[i]: 
            for j in range(n): 
                if not selected[j] and graph[i][j] != 0: 
                    if graph[i][j] < minimum: 
                        minimum = graph[i][j] 
                        x = i 
                        y = j 
 
    print(f"{x} - {y} \t {graph[x][y]}") 
    total_cost += graph[x][y] 
    selected[y] = True 
    edges += 1 
 
print("Total cost of MST:", total_cost) 
 
 
 
 
 
 
 
 