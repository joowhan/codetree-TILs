n = int(input())
temp = {}
for i in range(n):
    cows = list(input().split())
    cows.sort()
    cows = tuple(cows)
    if cows in temp.keys():
        temp[cows] += 1
    else:
        temp[cows] = 1
answer = sorted(temp.items(), key=lambda x:x[1], reverse=True)
print(answer[0][1])