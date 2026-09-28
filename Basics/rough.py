def printnumber(i,n):
    # base case
    if i>n:
        return
    # recursive case
    print(i, end = " ")
    printnumber(i+1,n)

printnumber(1,5)
