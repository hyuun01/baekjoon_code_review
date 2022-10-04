data = []
for _ in range(9):
    data.append(int(input()))

maxValue = max(data)
answer = data.index(maxValue) + 1
print(maxValue)
print(answer)
