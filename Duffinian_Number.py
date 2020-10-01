import math 
def divSum(n):
    result = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            if (i == (n // i)):  
                result += i  
            else: 
                result += (i + n / i)  
    return (result + n + 1)  
def isDuffinian(n):
    sumDivisors = int(divSum(n)) 
    if (sumDivisors == n + 1):
        return False
    hcf = math.gcd(n, sumDivisors)  
    return hcf == 1
n = int(input("Enter a number :")) 
if (isDuffinian(n)):  
    print("Duffinian Number ")  
else: 
    print("Not Duffinian Number")  
  
