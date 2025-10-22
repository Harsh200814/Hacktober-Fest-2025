def add_two_numbers(num1, num2):
    num1 = a 
    num2 = b
    res = 0 
    carry = 0
    place = 0
    while num1>0 or num2>0 or carry>0:
        l1 = num1%10
        l2 = num2%10
        total = carry + l1 + l2 
        carry = total//10
        res = res + (total%10) * (10**place)
        place+=1
        num1//=10
        num2//=10
    return res
