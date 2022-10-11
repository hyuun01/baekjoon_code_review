# m 이상 n 이하 소수 한 줄에 하나씩 출력
m, n = map(int, input().split())

list = [[x, True] for x in range(0, n + 1)]

for i in range(2, n + 1):
    if list[i][1]:
        for j in range(i * 2, n + 1, i):
            list[j][1] = False

answer = [x[0] for x in list if x[1] == True]

for i in range(2, len(answer)):
    if answer[i] < m:
        continue
    if answer[i] > n:
        break
    print(answer[i])