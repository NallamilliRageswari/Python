#Happy number - when sum of number is equal to 1 or 7 .
#program for happy number with recursion.
n=int(input("Enter a number : "))
sum1=0
def Happy(n):
    sum1=0
    if(n==1 or n==7):
        return ("Happy number")
    elif(n<10):
        return("Not a Happy Number")
    else:
        while(n>0):
            num=n%10
            sum1+=num**2
            n=n//10
        return(Happy(sum1))
print(Happy(n))
