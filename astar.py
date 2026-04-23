import heapq

goal = [[1,2,3],[4,5,6],[7,8,0]]

def h(s):
    d = 0
    for i in range(3):
        for j in range(3):
            v = s[i][j]
            if v != 0:
                d += abs((v-1)//3 - i) + abs((v-1)%3 - j)
    return d

def astar(start):
    pq = [(h(start), 0, start, [])]   # (f, g, state, path)

    while pq:
        f, g, cur, path = heapq.heappop(pq)

        if cur == goal:
            return path + [cur]

        # find blank
        for i in range(3):
            for j in range(3):
                if cur[i][j] == 0:
                    x, y = i, j

        # moves
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<3 and 0<=ny<3:
                new = [r[:] for r in cur]
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]

                heapq.heappush(pq, (g+1+h(new), g+1, new, path+[cur]))

start = [[1,2,3],[4,0,6],[7,5,8]]
ans = astar(start)

for i, s in enumerate(ans):
    print("Step", i)
    for r in s:
        print(r)
    print()

print("Moves:", len(ans)-1)