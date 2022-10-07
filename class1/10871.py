n, x = map(int, input().split())
data = list(map(int, input().split()))

# answer = [item for item in data if item < x]

for item in data:
    if item < x:
        print(item, end=' ')