import math 
def checkSemiprime(n): 
    cnt = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0: 
            n /= i 
            cnt += 1 
        if cnt >= 2:  
            break
    if(n > 1): 
        cnt +=1
    return cnt == 2
def Semiprime(n): 
    if(checkSemiprime(n) == True): 
        print("Semi prime") 
    else: 
        print("Not semi prime")
num=int(input("Entera number : "))
Semiprime(num)
