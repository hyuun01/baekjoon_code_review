a = int(input())
b = int(input())
c = int(input())
value = a*b*c
data = str(value)
for x in range(0, 10):
    print(data.count(chr(x + ord('0'))))
