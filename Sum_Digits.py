def Sum_Digits(n):
    x=0
    while n>0:
        rem = n%10
        x+=rem
        n //=10
    return x
n = int(input("Enter a number"))
print("Sum of digits :",Sum_Digits(n))
