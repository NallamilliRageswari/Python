lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))
def prime(n):
    for i in range(2,n):  
           if (n % i) == 0:  
               break
    else:
        print(n)
if(lower<upper):
    for num in range(lower,upper + 1):
        prime(num)
else:
    for num in range(lower,upper + 1,-1):
        prime(num)
    
