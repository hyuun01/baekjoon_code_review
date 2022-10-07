data = []
for _ in range(10):
    value = int(input())
    data.append(value % 42)
    
print(len(set(data)))