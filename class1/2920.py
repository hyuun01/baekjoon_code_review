ascending = [x for x in range(1, 9)]
descending = [x for x in range(8, 0, -1)]

data = list(map(int, input().split()))

if data == ascending:
    print('ascending')
elif data == descending:
    print('descending')
else:
    print('mixed')