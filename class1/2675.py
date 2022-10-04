t = int(input())
answer = []
for _ in range(t):
    temp, data = input().split()
    n = int(temp)
    newstr = [x*n for x in data]
    answer.append(''.join(newstr))
    
for x in answer:
    print(x)