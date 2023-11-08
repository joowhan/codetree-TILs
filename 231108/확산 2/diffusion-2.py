import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [[10**7] * m for _ in range(n)]

# 먼저 시작점인 1인 곳들을 queue에 집어넣는다. 이때 움직이지 않았으니 cost = 0도 함께 넣어준다.
# queue에서 하나씩 꺼낸다. 그리고 주변을 탐색해서 방문가능한 지역인지 확인하고 방문이 가능할 때 visited에서 그 위치의 값 보다 cost+1이 작다면 방문한다.
# visited는 무한대로 초기화되어 있는데, 이때 첫 방문이면 cost+1 값이 저장되고 queue에도 똑같이 저장한다. 그러면 이제 턴이 지날 때 방문 값은 1,2,3,..하고 커지게 된다. 
# 모든 탐색이 끝났으면 max 값을 찾는다. 근데 이때 visited 안에 무한대 값이 존재한다면 -1을 return 해야 한다. 
queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            visited[i][j] = 0   
            queue.append([i,j,0])
        elif graph[i][j] == -1:
            visited[i][j] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    x,y, cost = queue.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx>=n or nx<0 or ny >=m or ny < 0:
            continue
        # 방문 가능한 땅일 때
        if graph[nx][ny] == 0:
            if visited[nx][ny] > cost+1:
                visited[nx][ny] = cost+1
                queue.append([nx,ny, cost+1])

answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == -1:
            continue
        elif visited[i][j] == 10**7:
            answer = -1
            break
        if visited[i][j] > answer:
            answer = visited[i][j]
    if answer == -1:
        break
print(answer)