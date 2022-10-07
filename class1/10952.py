ans = []

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    ans.append(a+b)
    
for x in ans:
    print(x)