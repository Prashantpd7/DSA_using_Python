n = 1634
num = n
nod = len(str(n))
result = 0
while num>0:
    last_digit = num%10
    result = result + (last_digit ** nod)
    num = num//10

print(n==result)