# M명의 유저, N개의 구역 -> 4가지 존재, 두 개의 구역이 주어지면 얻는 아이템을 겹치지 않게 
# N개의 구역에서 어떤 아이템이 나와야 하는지?
N,M = map(int, input().split())
# 각 구역에서 나와야 하는 아이템
# 겹치지 않게 1,2,3,4 배치
graph=[[] for _ in range(N+1)]
visited = [0] *(N+1)
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 1
for i in range(len(graph)):
    for j in range(len(graph[i])):
        visited[graph[i][j]] = cnt+1