import math
def prime(n):
	for i in range(2,abs(int(math.sqrt(n)))+1):
		if n%i==0:
			break
	else:
		return(1)
def nearestPrimeOf(n):
    found = False
    next = n+1
    before = n-1
    while not found:
    	if prime(next):
    		print(next)
    		break
    	if prime(before):
    		print(before)
    		break
    	before -= 1
    	next  += 1
   
n = int(input("Enter a number : "))
nearestPrimeOf(n)
