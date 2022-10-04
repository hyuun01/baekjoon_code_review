n = int(input())
data = list(map(int, input().split()))

maxValue = max(data)
for i in range(len(data)):
    data[i]  = data[i]/maxValue*100
answer = sum(data) / n

print(answer)