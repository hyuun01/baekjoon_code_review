from operator import truediv


def isPalen(data):
    answer = True
    length = len(data)
    for i in range(length // 2):
        if data[i] != data[length - 1 - i]:
            answer = False
            break
        
    return answer
    

while True:
    data = input()
    if data == '0':
        break
    
    if isPalen(data):
        print('yes')
    else:
        print('no')
        