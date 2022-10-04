data = list(map(int, input().split()))
answer = sum([x*x for x in data]) % 10

print(answer)