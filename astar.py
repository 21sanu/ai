import heapq

goal=[[1,2,3],
    [4,5,6],
    [7,8,0]]
    
def h(state):
    dist = 0
    
    for i in range(3):
        for j in range(3):
            
            value=state[i][j]
            
            if value !=0:
                goalrow=(value -1) //3
                goalcol=(value -1) %3

                dist += abs(goalrow -i)+ abs(goalcol-j)
    return dist
    
def astar(start):
    pq = []
    # (f, g, state, path)
    heapq.heappush(pq, (h(start), 0, start, []))
    
    while pq:
        
        f,g,cur,path= heapq.heappop(pq)
        
        if cur == goal:
            return path + [cur]
            
        for i in range(3):
            for j in range(3):
                if cur[i][j] == 0:
                    x = i
                    y = j

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            
            nx = x+dx
            ny = y+dy
            
            if nx >= 0 and nx<3 and ny >=0 and ny <3:
                
                new = [row[:] for row in cur]

                new[x][y],new[nx][ny] = new[nx][ny],new[x][y]
                
                newg = g+1
                newf =newg+h(new)
                
                heapq.heappush(pq,(newf,newg,new,path+[cur]))
        
start = [[1,2,3],
         [4,0,6],
         [7,5,8]]              
         
ans= astar(start)         

for step,state in enumerate(ans):
    print("Step",step)
    for row in state:
        print(row)
    print()
    
print("Moves: ",len(ans)-1)    
                
                
                
                
                