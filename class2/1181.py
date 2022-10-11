n = int(input())
data = []
for _ in range(n):
    word = input()
    data.append((len(word), word))
    
'''
data = sorted(list(set(data)))
data.sort(key=len)

for x in data:
    print(x)
'''

data = list(set(data))
data.sort()
for x in data:
    print(x[1])

    
