def poweroftwo(n):
    if n<=0:
        return False
    if n%2!=0:
        return False
    if n%2==0:
        return True
    return poweroftwo(n//2)

print(poweroftwo(15))