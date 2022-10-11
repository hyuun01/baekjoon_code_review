'''
n = int(input())
# list 생성에서 시간 초과
queue = [x for x in range(n, 0, -1)]
front = len(queue) - 1
while len(queue) > 1:
    queue.pop(front)
    front -= 2
    front %= len(queue)

print(queue[0])   
'''

import sys
import collections
n = int(sys.stdin.readline().rstrip())
card = collections.deque([i for i in range(1, n + 1)])
while len(card) > 1:
    card.popleft()
    card.append(card[0])
    card.popleft()
print(card[0])
