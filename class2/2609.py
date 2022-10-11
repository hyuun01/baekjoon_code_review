# 최대공약수와 최소공배수
# n * m = 최대공약수 * 최소공배수

n, m = map(int, input().split())

# 최대공약수: 유클리드 호제법
def gcd(a, b):
    if a < b:
        a, b = b, a
        
    while b != 0: 
        temp = a % b 
        a, b = b, temp    
        
    return a

ans1 = gcd(n, m)
ans2 = int(n * m / ans1)
print(ans1)
print(ans2)
