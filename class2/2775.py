t = int(input())
data = [[int(input()), int(input())] for _ in range(t)]

# [a][b] = [a][b-1] + [a-1][b]
max_r = max(data, key=lambda x:x[0])[0] # 층
max_c = max(data, key=lambda x:x[1])[1] # 호

# 0층~, 1층~
ans_list = []
temp = list(range(max_c + 1))
ans_list.append(temp)
# 각 층에 대하여 : 1층~max_r 층
for i in range(1, max_r + 1):
    data = [1]  # 1호에는 무조건 1명 거주
    for j in range(1, max_c + 1):
        new = data[j - 1] + ans_list[i - 1][j]
        data.append(new)

for x in data:
    print(ans_list[x[0]][x[1] - 1])
