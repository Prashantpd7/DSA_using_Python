n = 587355872395
num = n
count = 0
while num>0:
    last_digit = num%10
    num = num//10
    count += 1

print(count)