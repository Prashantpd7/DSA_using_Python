n = 1234
num = n
r = 0
while num>0:
    last_digit = num%10
    r = last_digit+(r*10)
    num = num//10
print(n == r)