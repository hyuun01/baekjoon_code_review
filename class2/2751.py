import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()

for x in data:
    print(x)

