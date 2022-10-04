# dictionary
# del dict[key] : remove item with the key
# dict.clear()
# dict.get(key) : value
# dict.get(key, default) : value if exists key, else default
# dict[key] : value
# itme in dict : return True OR False if there is the item in dict
# dict.keys() : [key1, ...]
# dict.values() : [value1, ...]
# dict.items() : [(key1, value1), ...]

# stringData.upper() : aBc -> ABC
# stringData.lower() : aBc -> abc
# stringData.swapcase() : aBc -> AbC
# stringData.capitalize() : aBc -> Abc

# list.count(value) : list 속 value값인 것 개수
 
# ord('A') : 'A'의 아스키코드값
# chr(26) : 아스키코드값 26인 문자

data = input().upper()

# 2nd code : x-'A' can not be calculated
counts = [0 for _ in range(26)]
for x in data:
    counts[ord(x)-ord('A')] += 1  # 에러 발생 : index out of range : ????????????????

answer = max(counts)
if counts.count(answer) >= 2:
    print('?')
else :
    print(chr(counts.index(answer) + ord('A')))


'''
# 1st code : time-out
dict = {}
for x in data:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

answer = max(dict, key=dict.get)
max1 = dict.get(answer)

del dict[answer]
temp = max(dict, key=dict.get)
max2 = dict.get(temp)

if max1 == max2:
    print('?')
else:
    print(answer)
'''

