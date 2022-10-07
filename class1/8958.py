n = int(input())
answer = []
for _ in range(n):
    data = input()
    
    value = 0
    count = 0
    for i in range(len(data)):
        curr = data[i]
        if curr == 'X':
            count = 0
        else:
            count += 1
            value += count
    
    answer.append(value)
            

for i in range(n):
    print(answer[i])