num = int(input("Enter a number \n"))
sqr = num*num
sum_of_Digit = 0
while sqr>0:
    sum_of_Digit =sum_of_Digit + sqr%10
    sqr = sqr//10
if (num == sum_of_Digit):
    print("Neon Number \n")
else:
    print("Not a Neon Number \n")
