from string import ascii_lowercase
alpha = list(ascii_lowercase)
data = input()
for x in alpha:
    print(data.find(x), end=' ')