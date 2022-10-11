n = int(input())
# data1을 list로 하면 시간초과
# list의 search : O(n)
# set의 search : O(1)
data1 = set(map(int, input().split()))

m = int(input())
data2 = list(map(int, input().split()))

for x in data2:
    if x in data1:
        print(1)
    else:
        print(0)

