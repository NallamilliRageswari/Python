def isPrime(n):
    if n <= 3:
    	return n>1
    if n % 2 == 0:
        return False
    for i in range(2,int(n**0.5) + 1,2):
    	if n % i == 0:
    		return False
    return True
def SuperPrime(n):
    cnt = 1
    if isPrime(n):
        while n>0:
            n -= 2
            if isPrime(n):
                cnt += 1
    return isPrime(cnt)

n = int(input("Enter a number : "))
print(SuperPrime(n))
