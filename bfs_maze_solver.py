import collections
def bfs(maze,start,end):
    queue=collections.deque([[start]])
    visited=set([start])
    while queue:
        path = queue.popleft()
        current = path[-1]
        if current ==end:
            return path
        for dr,dc in[(-1,0),(1,0),(0,-1),(0,1)]:
            r,c=current[0]+dr,current[1]+dc
            if 0<=r<len(maze) and 0<=c<len(maze[0]) and maze[r][c]==0 and (r,c) not in visited:
                queue.append(path+[(r,c)])
                visited.add((r,c))
    return None
    
maze=[
    [0,1,1,1,1],
    [0,0,0,1,0],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,0,0,1]]
start=(1,1)
end=(4,3)
path=bfs(maze,start,end)
if path:
    print("found",path)
else:
    print("not found")