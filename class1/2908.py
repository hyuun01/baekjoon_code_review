a, b = input().split()

alen = len(a)
blen = len(b)
n1 = [a[alen -1 - x] for x in range(alen)]
n2 = [b[blen - 1 - x] for x in range(blen)]

x = int(''.join(n1))
y = int(''.join(n2))

print(max(x, y))