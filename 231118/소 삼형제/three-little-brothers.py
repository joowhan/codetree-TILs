n = int(input())
temp = []
for i in range(n):
    cows = list(input().split())
    cows.sort()
    if cows not in temp:
        temp.append(cows)
print(len(temp))