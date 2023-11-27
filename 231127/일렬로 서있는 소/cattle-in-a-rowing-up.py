# x<y<z, y-x <=z-y <=2*(y-x)
N = int(input())
cows =[]
for _ in range(N):
    cows.append(int(input()))

cows.sort()
answer = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if cows[j]- cows[i] <= cows[k]-cows[j] <= 2*(cows[j]-cows[i]):
                answer +=1
print(answer)