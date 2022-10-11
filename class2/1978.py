n = int(input())
data = list(map(int, input().split()))

h_bound = max(data)

num_list = [[x, True] for x in range(h_bound + 1)]
for i in range(2, h_bound + 1):
    if num_list[i][1] == True:
        for j in range(i*2, h_bound+1, i):
            num_list[j][1] = False

prime_list = set([x[0] for x in num_list[2:] if x[1] == True])

count = 0
for x in data:
    if x in prime_list:
        count += 1

print(count)



